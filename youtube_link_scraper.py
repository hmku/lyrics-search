import urllib.request
import urllib.parse
import re

query_input = "Alec Benjamin Let Me Down Slowly"
query_string = urllib.parse.urlencode({"search_query" : query_input})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("http://www.youtube.com/watch?v=" + search_results[0])


# https://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video