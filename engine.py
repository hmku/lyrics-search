import requests


GOOGLE_API_KEY = 'AIzaSyCrBdeuM-QHwP-tRxlF8Il9XB9WgBcnOro'
BASE_URL = 'https://www.googleapis.com/customsearch/v1/siterestrict?key={key}&cx={cx}&q={query}'
AZLYRICS_CX = '004866776918846137660:g-xyfvdi1va' # AZLyrics search engine code
YOUTUBE_CX = '004866776918846137660:kta603plkba' # YouTube search engine code
BASE_THUMBNAIL_URL = 'https://i.ytimg.com/vi/{id}/maxresdefault.jpg'


def get_lyrics_results(input):
    r = requests.get(BASE_URL.format(key=GOOGLE_API_KEY, cx=AZLYRICS_CX, query=input))
    results = r.json() # Loads json into dictionary
    return results

def get_youtube_result(input): # Gets link and thumbnail of first result
    r = requests.get(
        BASE_URL.format(key=GOOGLE_API_KEY, cx=YOUTUBE_CX, query=input) + 
        '&fields=items(link)'
    )
    results = r.json() # Loads json into dictionary
    link = results['items'][0]['link']
    return link, _get_thumbnail(link)

def _get_thumbnail(link):
    id = link.split('/watch?v=')[1]
    return BASE_THUMBNAIL_URL.format(id=id)
