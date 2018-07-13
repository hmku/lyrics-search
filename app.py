from flask import Flask, render_template, request
import engine
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/search-results', methods=['POST'])
def search_lyrics():
    query = request.form['query']
    results = engine.get_search_results(query)
    titles = [item['title'] for item in results['items']] # List of result titles
    return ', '.join(titles)

if __name__ == "__main__":
    app.run()
