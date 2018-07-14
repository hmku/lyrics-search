from bs4 import BeautifulSoup
from urllib.request import urlopen
from fuzzywuzzy import fuzz
import re


def _get_html(link):
    page = urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def _get_lyrics(link):
    soup = _get_html(link)
    tags = soup.findAll('div', attrs={'class': None})
    lyrics = '\n'.join(tag.getText() for tag in tags)
    return lyrics


def _tokenize_by_word(s):
    s_tokenized = s.split()
    return s_tokenized


def _tokenize_by_line(s):
    s_lines = s.split('\n')
    return [line.split(' ') for line in s_lines]


def _strip(s):
    return re.sub(r'[^\w\s]', '', s).lower() # Remove all non-word, non-space chars
    

def _match_query(query, lyrics):
    max_score = max_ind = -1
    lyrics_words = _tokenize_by_word(lyrics)
    query_stripped = _strip(query)
    chunk_len = len(query_stripped.split()) # Chunk length is same as query length (for now)
    
    for i in range(0, len(lyrics_words)-chunk_len):
        lyrics_chunk = ' '.join(lyrics_words[i:(i+chunk_len)])
        lyrics_chunk_stripped = _strip(lyrics_chunk)
        curr_score = fuzz.token_set_ratio(lyrics_chunk_stripped, query_stripped)
        if curr_score > max_score:
            max_score = curr_score
            max_ind = i

    return (max_ind, chunk_len) # Return index of lyrics (word #) where query matches


def get_snippet(query, link):
    lyrics = _get_lyrics(link)
    lyrics_lines = _tokenize_by_line(lyrics)
    num_lines = len(lyrics_lines)
    ind, chunk_len = _match_query(query, lyrics)
    curr_ind, line_ind = 0, 0

    for i in range(0, num_lines):
        for word in lyrics_lines[i]:
            if len(word) == 0 or word.isspace(): continue
            if curr_ind == ind:
                line_ind = i
            curr_ind += 1
    
    snippet = []
    offset = 1
    while str(snippet).count(',')+1 < chunk_len:
        snippet = lyrics_lines[max(0, line_ind-offset):min(num_lines-1, line_ind+offset)+1]
        offset += 1

    return (snippet, ind, chunk_len)


# Test the snippet finder
snippet, ind, chunk_len = get_snippet('i hate goodbyes', 'https://www.azlyrics.com/lyrics/owlcity/fireflies.html')
print('\n'.join([' '.join(line) for line in snippet]))
