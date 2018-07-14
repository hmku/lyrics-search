import requests
import time
from bs4 import BeautifulSoup
 
 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
 
 
def search_results(query, number_results, language):
    assert isinstance(query, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    replaced_search_term = query.replace(' ', '+')
 
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}&as_sitesearch=AZlyrics.com'.format(replaced_search_term, number_results, language)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
 
    return query, response.text


def parse_results(html, keyword):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        if link and title:
            link = link['href']
            title = title.get_text()
            if link != '#':
                found_results.append({'title': title, 'link': link})
    return found_results

def scrape_google(search_term, number_results, language_code):
    try:
        keyword, html = search_results(search_term, number_results, language_code)
        results = parse_results(html, keyword)
        return results
    except AssertionError:
        raise Exception("Incorrect arguments parsed to function")
    except requests.HTTPError:
        raise Exception("You appear to have been blocked by Google")
    except requests.RequestException:
        raise Exception("Appears to be an issue with your connection")

def search_list(keywords, number_of_results):
    data = []
    try:
        results = scrape_google(keywords, number_of_results, "en")
        for result in results:
            data.append(result)
    except Exception as e:
        print(e)
    finally:
        time.sleep(10)
    print(data[0])
 
if __name__ == '__main__':
    keywords = "Let me down slowly"
    results = 10
    search_list(keywords, results)