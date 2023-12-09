#written by: Joey and Elliot
#Tested by: Joey and Elliot
#Debugged by: Joey and Elliot

from flask import Flask, request, render_template, flash, jsonify, redirect, url_for, session
from main import search_articles, connect_to_cluster
from bson import ObjectId
from SearchController import SearchController
from User_Login import UserLogin
from User_Registration import UserRegistration
from user import *
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

search_controller = SearchController()

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']  # Get the search query from the form
    results = search_controller.search_all_button(search_query)

    return render_template('search.html', results = results)

@app.route('/search_computer_science_folder')
def search_computer_science_folder():
    # Call the function to search computer science articles
    search_controller.show_all_computer_science_button()  
    article_list = search_controller.get_article_list()
    return render_template('show_computer_science.html', article_list=article_list)

@app.route('/search_math_folder')
def search_math_folder():
    # Call the function to search math articles
    search_controller.show_all_math_button()  
    article_list = search_controller.get_article_list()
    return render_template('show_math.html', article_list=article_list)

@app.route('/search_physics_folder')
def search_physics_folder():
    # Call the function to search physics articles
    search_controller.show_all_physics_button()  
    article_list = search_controller.get_article_list()
    return render_template('show_physics.html', article_list=article_list)

@app.route('/search_english_folder')
def search_english_folder():
    # Call the function to search english articles
    search_controller.show_all_english_button()  
    article_list = search_controller.get_article_list()
    return render_template('show_english.html', article_list=article_list)

@app.route('/search_history_folder')
def search_history_folder():
    # Call the function to search history articles
    search_controller.show_all_history_button()  
    article_list = search_controller.get_article_list()
    return render_template('show_history.html', article_list=article_list)

@app.route('/search_biology_folder')
def search_biology_folder():
    # Call the function to search biology articles
    search_controller.show_all_biology_button()  
    article_list = search_controller.get_article_list()
    return render_template('show_biology.html', article_list=article_list)

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
            flash('Invalid username or password', 'error')
            return render_template('login.html')
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
    if 'user_id' in session:
        user_id = session['user_id']
        user = user_registration.get_user_by_id(user_id)

        if user:
            user.add_favorite(article_title)
            user_registration.update_user(user_id, user.to_dict())

    return redirect(url_for('favorites'))

@app.route('/remove_favorite/<article_title>')
def remove_favorite(article_title):
    if 'user_id' in session:
        user_id = session['user_id']
        user = user_registration.get_user_by_id(user_id)

        if user:
            if article_title in user.favorite:
                user.remove_favorite(article_title)
                user_registration.update_user(user_id, user.to_dict())

    return redirect(url_for('favorites'))



@app.route('/favorites') #get the user's favorites and add them to the favorites html
def favorites():
    client = connect_to_cluster(
        "mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Users?retryWrites=true&w=majority")
    results = search_articles(client, "favorites", "Profiles")
    if 'user_id' in session:
        user_id = session['user_id']
        user = user_registration.get_user_by_id(user_id)

        if user:
            favorites_list = user.favorite
            return render_template('favorites.html', favorites_list=favorites_list)
        
    return redirect(url_for('login'))

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(debug=True)