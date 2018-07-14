from flask import Flask, render_template, request
import engine
import util
import youtube_scraper
import snippet


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/search-results', methods=['POST'])
def search_lyrics():
    query = request.form['query']
    results = engine.get_search_results(query)
    songs = []

    for song in results['items']:
        artist, title = util.split_name_str(song['title'])
        youtube_query = artist + ' ' + title
        youtube_link, youtube_thumbnail = youtube_scraper.get_youtube_info(youtube_query)
        lyrics_snippet = snippet.get_snippet(query, song['link'])
        d = {
            'title': title,
            'artist': artist, 
            'link': song['link'],
            'youtube_link': youtube_link,
            'thumbnail': youtube_thumbnail,
            'snippet': lyrics_snippet,
        }
        songs.append(d)
    
    return 'Top song: ' + songs[0]['title'] # TODO: Create template to return


if __name__ == "__main__":
    app.run()
