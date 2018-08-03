import requests


GOOGLE_API_KEY = 'AIzaSyCrBdeuM-QHwP-tRxlF8Il9XB9WgBcnOro'
BASE_URL = 'https://www.googleapis.com/customsearch/v1/siterestrict?key={key}&cx={cx}&q={query}'
AZLYRICS_CX = '004866776918846137660:g-xyfvdi1va' # AZLyrics search engine code
YOUTUBE_CX = '004866776918846137660:kta603plkba' # YouTube search engine code


def get_lyrics_results(input):
    r = requests.get(BASE_URL.format(key=GOOGLE_API_KEY, cx=AZLYRICS_CX, query=input))
    results = r.json() # Loads json into dictionary
    return results

def get_youtube_result(input): # Gets link of first result
    r = requests.get(
        BASE_URL.format(key=GOOGLE_API_KEY, cx=YOUTUBE_CX, query=input) + 
        '&fields=items(link)',
        headers={
            'Accept-Encoding': 'gzip',
            'User-Agent': 'engine(gzip)'
        }
    )
    results = r.json() # Loads json into dictionary
    if results.get('error') is not None: # Reached maximum quota for Google API
        return None
    link = results['items'][0]['link']
    return link
