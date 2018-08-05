def split_name_str(title):
    if title.find('- AZLyrics') != -1:
        title = title[:-11] # Remove the ' - AZlyrics' part
    name = title.split(' Lyrics - ')
    return tuple(name)

def filter_snippet(snippet, title, artist):
    extra = 'Lyrics to "' + title + '" song by ' + artist + ': '
    print(extra)
    return snippet.replace(extra, '')