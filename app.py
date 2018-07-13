from flask import Flask, render_template, request
import engine
import util


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
        song_name = util.split_name_str(song['title'])
        d = {
            'title': song_name['title'],
            'artist': song_name['artist'], 
            'link': song['link'],
        }
        songs.append(d)

    return 'Top song: ' + songs[0]['title'] # TODO: Create template to return


if __name__ == "__main__":
    app.run()
