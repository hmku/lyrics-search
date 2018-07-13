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

def _strip_and_tokenize(s):
    s_stripped = re.sub("'|,|.", '', s).lower()
    s_tokenized = re.split(' |\n', s_stripped)
    return s_tokenized

def match_query(query, lyrics):
    maxscore = maxind = -1
    lyrics_tokens = _strip_and_tokenize(lyrics)
    query_tokens = _strip_and_tokenize(query)
    for i in range(0, len(lyrics_tokens)-2*len(query_tokens)):
        pass # TODO

print(_get_lyrics('https://www.azlyrics.com/lyrics/muramasa/firefly.html'))