# Joey

from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from main import search_articles, connect_to_cluster, UserRegistration, UserLogin
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_hex(16) #creates a random secret key each run 

app.static_folder = 'static'  # flask only will display static files, so images and CSS pages needed to go in the static folder

user_registration = UserRegistration(
    mongodb_uri="mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Users?retryWrites=true&w=majority",
    database_name="Users", collection_name="Profiles")

user_login = UserLogin(
    mongodb_uri="mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Users?retryWrites=true&w=majority",
    database_name="Users", collection_name="Profiles")

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']  # Get the search query from the form
    client = connect_to_cluster(
        "mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
    results = search_articles(client, search_query, "Computer Science")

    return render_template('search.html', results = results)  # get results 

@app.route('/search', methods=['GET'])
def show_search_page():
    return render_template('search.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Authenticate user
        user = user_login.authenticate_user(email, password)

        if user:
            # Store user information in session 
            session['user_id'] = str(user.get('_id'))
            session['email'] = user.get('email')
            session['fname'] = user.get('First name')
            session['lname'] = user.get('Last name')

            return redirect(url_for('home'))
        else:
            return render_template('login.html', message='Invalid username or password')

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

        return redirect(url_for('login'))

    return render_template('create_account.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/add_favorite/<article_title>') #this is needed to add favorites and route them to fav page
def add_favorite(article_title):
    if 'favorites' not in session:
        session['favorites'] = []

    if article_title not in session['favorites']:
        session['favorites'].append(article_title)

    return redirect(url_for('favorites'))

@app.route('/remove_favorite/<article_title>') #removing favorites
def remove_favorite(article_title):
    if 'favorites' in session and article_title in session['favorites']:
        session['favorites'].remove(article_title)

    return redirect(url_for('favorites'))

@app.route('/favorites') #get the user's favorites and add them to the favorites html
def favorites():
    favorites_list = session.get('favorites', [])
    return render_template('favorites.html', favorites_list=favorites_list)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)

