from flask import Flask, request
from blueprints.auth import auth as auth_blueprint
from blueprints.main import main as main_blueprint
from movies import models
from flask_login import LoginManager
from movies.models import db
from movies.user_class import User
from movies.movie_fetcher import get_movies, insert


# OCP principle, new functionalities can be adding or importing through other files but not by modyfing this existing code

#Initialize app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
models.start_mappers()

# search movies and obtain the csv
get_movies()
# pass the csv to postgresql
insert()

# manages sesions of log-in
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return db.query(User).get(int(user_id))


# register blueprints of the routes, uses dependency inversion since it is an abstraction
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
