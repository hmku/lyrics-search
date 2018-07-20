from flask import Flask, render_template, request
import util
import youtube_scraper
import snippet
import google_scraper


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/search-results', methods=['POST'])
def search_lyrics():
    num_results = 10
    query = request.form['query']
    lyrics_results = google_scraper.search_list(query, num_results, 'azlyrics')
    youtube_results = google_scraper.search_list(query, num_results, 'youtube')
    song_info = []
    for description, youtube_data in zip(lyrics_results, youtube_results):
        artist, title = util.split_name_str(description['title'])
        d = {
            'title': title,
            'artist': artist, 
            'link': description['link'],
            'youtube_link': youtube_data['link'],
            'thumbnail': youtube_data['thumbnail'],
            'snippet': description['snippet'],
        }
        song_info.append(d)
    print(song_info)
    return song_info[0]['title']


if __name__ == "__main__":
    app.run()
