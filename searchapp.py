#Joey

from flask import Flask, request, render_template_string, jsonify
from main import search_articles, connect_to_cluster

app = Flask(__name__)

app.static_folder = 'static' #flask only will display static files, so images and css pages needed to go in static folder

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='search_style.css') }}">
  <title>Search Page</title>
</head>
<body>
  <div class="container">
    <div class="left-side">
        <div class="filters">
        <h2>Filter by Topic</h2> <!--filters-->
        <label><input type="checkbox" name="topic" value="math"> Math</label>
        <label><input type="checkbox" name="topic" value="biology"> Biology</label>
        <label><input type="checkbox" name="topic" value="physics"> Physics</label>
        <label><input type="checkbox" name="topic" value="health"> Health</label>
        <label><input type="checkbox" name="topic" value="computer-science"> Computer Science</label>
        <label><input type="checkbox" name="topic" value="english"> English</label>
        <label><input type="checkbox" name="topic" value="statistics"> Statistics</label>
        <label><input type="checkbox" name="topic" value="environmentalism"> Environmentalism</label>
        <label><input type="checkbox" name="topic" value="psychology"> Psychology</label>
        
        <h2>Filter by Year</h2>
        <input type="range" name="year" min="1980" max="2023">
        
        <h2>Filter by Author</h2>
        <input type="text" name="author" placeholder="Type author's name">
        </div>
    </div>
    <div class="right-side">
        <div class="search-section">
            <form id="search-form" method="POST" action="/search">
              <div class="search-bar">
                  <img src="{{ url_for('static', filename='search.png') }}" width="30px" height="40px" alt="Search Icon">
                  <input type="text" id="search-input" name="search_query" placeholder="Type an article, topic, or subject to find articles">
                  <button type="submit">Search</button>
              </div>
            </form>
            <p id="search-message">Search results will be displayed here.</p>
            <div id="search-results">
                <!-- Hopefully the results will be here -->
            </div>
        </div>
    </div>
  </div>
  
  <div class="watermark">
    <p>&copy; The One Stop Research Shop - JAKE 2023</p>
  </div>

<script>
    document.getElementById("search-form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the form from reloading the page

        var searchQuery = document.getElementById("search-input").value;
        var xhr = new XMLHttpRequest();

        xhr.open("POST", "/search", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);

                if(response.results) {
                    var results = response.results;
                    displayResults(results);
                } else{
                    displayResults([]); 
                }

                
            }
        };

        xhr.send("search_query=" + searchQuery);
    });

    function displayResults(results) {
        var searchResults = document.getElementById("search-results");
        searchResults.innerHTML = ""; // Clear any previous results

        if (results.length === 0) {
            searchResults.innerHTML = "<p>No results found.</p>";
        } else {
            var resultHtml = "<ul>";
            for (var i = 0; i < results.length; i++) {
                resultHtml += "<li>" + results[i] + "</li>";
            }
            resultHtml += "</ul>";
            searchResults.innerHTML = resultHtml;
        }
    }
</script>
</body>
</html>

  <div class="watermark">
    <p>&copy; The One Stop Research Shop - JAKE 2023</p>
  </div>
</body>
</html>

"""

@app.route('/')
def index(): #render the html page from string above^^
    return render_template_string(html_template)

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']  # Get the search query from the form
    client = connect_to_cluster("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
    results = search_articles(client, search_query, "Computer Science")

    return jsonify({'results': results})# get results in json format

if __name__ == '__main__':
    app.run(debug=True)
