from flask import Flask, request, render_template, jsonify
from main import search_articles, connect_to_cluster

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']  # Get the search query from the form
    client = connect_to_cluster("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
    results = search_articles(client, search_query, "Computer Science")

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
