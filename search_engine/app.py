from flask import Flask, render_template, request
from search_engine import *

app = Flask(__name__)

articles = ''
bagOfWords = ''
termByDocument = ''

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search', methods=['POST'])
def searchRoute():
    query = request.form['query']
    result = search(query, termByDocument, bagOfWords)
    form = """
        <form action="/" method="get">
            <input type="submit" value="Go back">
        </form>
    """
    return form + getResultArticles(result, articles).replace('\n', '<br>')



if __name__ == "__main__":
    #running before the app acctually start working
    articles, bagOfWords = readDataSet('corpus.txt', 1000)
    termByDocument = getTermByDocumentMatrix(bagOfWords, articles)
    IDF(articles, termByDocument)

    app.run()