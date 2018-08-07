import requests
import time
from bs4 import BeautifulSoup
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
SEARCH_DOMAIN = {'azlyrics': 'https://www.google.com/search?q={}&num={}&hl={}&as_sitesearch=AZlyrics.com', 'youtube': 'https://www.google.com/search?q={}&num={}&hl={}&as_sitesearch=youtube.com'}
BASE_THUMBNAIL_URL = 'https://i.ytimg.com/vi/{id}/maxresdefault.jpg'

def _get_thumbnail_link(video_id):
    return BASE_THUMBNAIL_URL.format(id=video_id)

def _search_results(query, number_results, language, domain):
    assert isinstance(query, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    replaced_search_term = query.replace(' ', '+')
    url = SEARCH_DOMAIN[domain]
    google_url = url.format(replaced_search_term, number_results, language)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
 
    return query, response.text


def _parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        snippet = result.find('span', attrs={'class': 'st'})
        if link and title:
            link = link['href']
            title = title.get_text()
            thumbnail = _get_thumbnail_link(link[-11:])
            if snippet:
                snippet = snippet.get_text()
            if link != '#':
                found_results.append({'title': title, 'link': link, 'thumbnail': thumbnail, 'snippet': snippet})
    return found_results


def _scrape_google(search_term, number_results, language_code, domain):
    try:
        keyword, html = _search_results(search_term, number_results, language_code, domain)
        results = _parse_results(html, keyword)
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")


def search_list(keywords, number_of_results, domain):
    data = []
    try:
        results = _scrape_google(keywords, number_of_results, "en", domain)
        for result in results:
            data.append(result)
    except Exception as e:
        raise e
    
    return data
