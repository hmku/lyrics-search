def split_name_str(title):
    name = title.split(' Lyrics - ')
    return dict(zip(['artist', 'title'], name))
