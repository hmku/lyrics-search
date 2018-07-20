def split_name_str(title):
    title = title[:-11] # Remove the ' - AZlyrics' part
    name = title.split(' Lyrics - ')
    return tuple(name)
