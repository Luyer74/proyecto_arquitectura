from flask import Flask, request
from blueprints.auth import auth as auth_blueprint
from blueprints.main import main as main_blueprint
from movies import models
import pandas as pd
from flask_login import LoginManager
from movies.models import db, User
from movies.movie_fetcher import get_movies, insert

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
models.start_mappers()

#buscar peliculas y obtener csv
get_movies()
#pasar csv a postgresql  
insert()

#maneja sesiones de login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return db.query(User).get(int(user_id))

#registrar blueprints de rutas
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
