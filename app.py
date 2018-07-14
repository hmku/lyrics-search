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
    print(results)
    songs = []
    for song in results['items']:
        song_name = util.split_name_str(song['title'])
        d = {
            'title': song_name['title'],
            'artist': song_name['artist'], 
            'link': song['link'],
        }
        songs.append(d)
    for songInfo in songs:
        artist_title = songInfo['artist'] + ' ' + songInfo['title']
        youtube_results = youtube_engine.get_youtube_results(artist_title)
        # temp1 = youtube_results['items']
        # temp2 = temp1[0]
        # for key in temp2.keys():
        #     print(key)
        # print(temp2['htmlFormattedUrl'])
        links.append(youtube_results['items'][0]['formattedUrl'])
    #return 'Top song: ' + songs[0]['title'] # TODO: Create template to return
    print(links)


if __name__ == "__main__":
    app.run()
