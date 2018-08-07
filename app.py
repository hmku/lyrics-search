from flask import Flask, render_template, request, url_for, redirect
import util
from jinja2 import Template
import google_scraper, google_engine
import os


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/search-results', methods=['POST'])
def search_lyrics():
    num_results = 10
    query = request.form['query']
    lyrics_results = google_scraper.search_list(query, num_results, 'azlyrics')
    song_info = []

    try:
        for description in lyrics_results:
            valid_title = 'Lyrics -'
            if description['title'].find(valid_title) != -1:
                try:
                    artist, title = util.split_name_str(description['title'])
                except ValueError: # Handle error in util.split_name_str (usually when AZLyrics result is not a song)
                                   # Example: query = 'lyrics search'
                    continue # Skip to next result
                
                youtube_link = google_engine.get_youtube_result(artist + ' ' + title)
                if youtube_link is None: # Reached maximum quota for Google API
                    raise RuntimeError('Reached maximum quota for Google API!')
                
                d = {
                    'title': artist + ' - ' + title,
                    'link': description['link'],
                    'youtube': 'https://www.youtube.com/embed/' + youtube_link[-11:] + '?rel=0' ,
                    'snippet': util.filter_snippet(description['snippet'], title, artist),
                }
                song_info.append(d)

    except RuntimeError: # Handle Google API error
        return redirect('/error')

    else:
        print(song_info)
        return render_template('results.html', song_info=song_info, query=query)


@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')


if __name__ == "__main__":
    app.run()
