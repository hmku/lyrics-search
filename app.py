from flask import Flask, render_template, request, url_for, redirect
import util
from jinja2 import Template
import youtube_scraper, google_scraper, google_engine
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
<<<<<<< HEAD
<<<<<<< HEAD

    try:
        for description in lyrics_results:
            artist, title = util.split_name_str(description['title'])
            youtube_link, thumbnail = google_engine.get_youtube_result(artist + ' ' + title)
            if youtube_link is None: # Reached maximum quota for Google API
                raise RuntimeError('Reached maximum quota for Google API!')
            
            d = {
                'title': title,
                'artist': artist, 
                'link': description['link'],
                'youtube': 'https://www.youtube.com/embed/' + youtube_link[-11:] + '?rel=0' ,
                'thumbnail': thumbnail,
                'snippet': description['snippet'],
            }
            song_info.append(d)

    except RuntimeError: # Handle error
        return redirect('/error')

    else:
        print(song_info)
        return render_template('results.html', song_info=song_info)


@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')
=======
    for description in lyrics_results:
        artist, title = util.split_name_str(description['title'])
        youtube_link, thumbnail = google_engine.get_youtube_result(artist + ' ' + title)
        d = {
            'title': title,
            'artist': artist, 
            'link': description['link'],
            'youtube_link': youtube_link,
            'thumbnail': thumbnail,
            'snippet': description['snippet'],
        }
        song_info.append(d)
    print(song_info)
    return render_template('results.html')
>>>>>>> results page
=======
>>>>>>> TEST

    try:
        for description in lyrics_results:
            artist, title = util.split_name_str(description['title'])
            youtube_link, thumbnail = google_engine.get_youtube_result(artist + ' ' + title)
            if youtube_link is None: # Reached maximum quota for Google API
                raise RuntimeError('Reached maximum quota for Google API!')
            
            d = {
                'title': title,
                'artist': artist, 
                'link': description['link'],
                'youtube_link': youtube_link,
                'thumbnail': thumbnail,
                'snippet': description['snippet'],
            }
            song_info.append(d)

    except RuntimeError: # Handle error
        return redirect('/error')

    else:
        print(song_info)
        return str(song_info)


@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

if __name__ == "__main__":
    app.run()
