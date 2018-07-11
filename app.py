from flask import Flask, render_template, request
import engine
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/search-results',methods=['POST'])
def get_search_results():
    search = request.form['searchKey']
    return engine.search_lyrics(search)

if __name__ == "__main__":
    app.run()
    