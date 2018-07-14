import urllib.request
import urllib.parse
import re


BASE_VIDEO_URL = 'https://www.youtube.com/watch?v={id}'
BASE_THUMBNAIL_URL = 'https://i.ytimg.com/vi/{id}/maxresdefault.jpg'


def _get_video_link(video_id):
    return BASE_VIDEO_URL.format(id=video_id)


def _get_thumbnail_link(video_id):
    return BASE_THUMBNAIL_URL.format(id=video_id)


def get_youtube_info(input):
    query = urllib.parse.urlencode({"search_query" : input})
    page = urllib.request.urlopen("http://www.youtube.com/results?" + query)
    top_video_id = re.search(r'href=\"\/watch\?v=(.{11})', page.read().decode())
    return (_get_video_link(top_video_id), _get_thumbnail_link(top_video_id))

print(get_youtube_info("let me down slowly"))