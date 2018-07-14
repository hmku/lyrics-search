import urllib.request
import urllib.parse
import re


def get_search_results(input): # TODO: Actually get results from Google
    query = urllib.parse.urlencode({"search_query" : input})
    page = urllib.request.urlopen("http://www.youtube.com/results?" + query)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', page.read().decode())
    return ("http://www.youtube.com/watch?v=" + search_results[0])
