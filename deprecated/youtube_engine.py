import requests


GOOGLE_API_KEY = 'AIzaSyCrBdeuM-QHwP-tRxlF8Il9XB9WgBcnOro'
BASE_URL = 'https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}'
CX = '004866776918846137660:kta603plkba' # Search engine code


def get_youtube_results(input):
    r = requests.get(BASE_URL.format(key=GOOGLE_API_KEY, cx=CX, query=input))
    results = r.json()
    return results
