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
    query = request.form['query']
    results = google_scraper.search_list(query, 10) # MAGIC NUMBER
    songs = []

    for song in results:
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

    print(songs)

    #return 'Top song: ' + songs[0]['title'] # TODO: Create template to return


if __name__ == "__main__":
    app.run()
