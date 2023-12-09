https://github.com/elliott2232/CS4800-JAKE

To run our application, run the following command in the command line: ‘python app.py’. Within the command line, a port string is displayed like so: ‘http://111.0.0.1:5000'. Copy and paste this into the search bar in a browser and you will access our site.

templates files - this folder holds all of our html pages used for this project.
create_account.html - interface allowing users to create an account in our database with their name, email, and a password.
favorites.html - interface for showing a user's favorites and allows users to remove favorites with a click of a button.
home.html - interface for our homepage which consists of a welcome page, navigation bar, and clickable folders to articles on specific subjects.
landing_page.html - first page a user sees on first time visit. redirects to log in.
login.html - authenticates users with an email and password. also allows a redirect to create an account.
search.html - allows users to search and favorite articles. can redirect to home.
show_<subject>.html - these files show specific subject articles based on which folder on the homepage was clicked
user.html - shows the users information (except password)
static files - this folder contains the css pages that style all of the html pages. also contains all of the images used on our webpage.
User_Registration- Is a class to set all of the users info when they are creating and account and storing it in the database
User_login - Takes in the UserObject class and passes in the parameters to verify the user login from the info written to the database
app.py - contains all the flask routing needed for the application. Most importantly this is our runnable file. When you run our code, or type “python app.py” in the terminal while in our project’s directory, our application will start.
Article.py - is a class to hold article information incoming from our article database.
SearchController.py - is a class that handles searching in the back-end. It includes several search functionalities.
Boundaries.py - is a class meant for our boundary buttons. However, this file is unused in our final system.
test_search.py - is a python file meant to display the search controller’s functionalities including those used on the site and those not implemented as we were cut for time.


