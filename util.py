def split_name_str(title):
    name = title.split(' Lyrics - ')
    return dict(zip(['artist', 'title'], name))

print(split_name_str("Gavin DeGraw Lyrics - Not Over You"))
