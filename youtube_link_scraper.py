import urllib.request
import urllib.parse
import re


def get_youtube_link(query_input):
    query_string = urllib.parse.urlencode({"search_query" : query_input})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return ("http://www.youtube.com/watch?v=" + search_results[0])


# Test scraper
print(get_youtube_link("Childish Gambino This is America"))
