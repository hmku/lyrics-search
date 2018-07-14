import urllib.request
import urllib.parse
import re


def get_youtube_link(query_input):
    query_string = urllib.parse.urlencode({"search_query" : query_input})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return ("http://www.youtube.com/watch?v=" + search_results[0])


#If the video URL is https://www.youtube.com/watch?v=xxxxxxxxxxxx
#The thumbnail URL is https://i.ytimg.com/vi/xxxxxxxxxxxx/maxresdefault.jpg


