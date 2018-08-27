def split_name_str(title):
    if title.find('AZLyrics.com') != -1:
        title = title[:-21] # Remove the ' - AZlyrics' part
    name = title.split(' - ')
    return tuple(name)

def filter_snippet(snippet, title, artist):
    extra = 'Lyrics to "' + title + '" song by ' + artist + ': '
    print(extra)
    return snippet.replace(extra, '')