#Joey

from flask import Flask, request, render_template, jsonify
from main import search_articles, connect_to_cluster, UserRegistration 

app = Flask(__name__)

app.static_folder = 'static' #flask only will display static files, so images and css pages needed to go in static folder

user_registration=UserRegistration(mongodb_uri = "mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Users?retryWrites=true&w=majority", database_name = "Users", collection_name = "Profiles")

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']  # Get the search query from the form
    client = connect_to_cluster("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
    results = search_articles(client, search_query, "Computer Science")

    return jsonify({'results': results})# get results in json format

@app.route('/search', methods=['GET'])
def show_search_page():
    return render_template('search.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        # Get user input from the form
        email = request.form['email']
        first_name = request.form['fname']
        last_name = request.form['lname']
        password = request.form['psw']

        # Call the register_user method to register a new user
        user_registration.register_user(email, first_name, last_name, password)

        return "User registered successfully"

    return render_template('create_account.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/favorites')
def favorites():
    return render_template('favorites.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)

