# Luis Yerik Arambula Barrera A00825080
# Alejandro Lopez Ramones A01366287

from operator import is_
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from movies.models import Movie, db
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    is_rating = request.args.get("rating")

    # if rating parameter is found then order should be reversed
    if is_rating == 'false':
        reverse = False
    else:
        reverse = True
    movie_query = db.query(Movie)
    movies = movie_query.filter_by(preference_key=current_user.magic_number)
    data = []
    for movie in movies:
        datapoint = {}
        datapoint["movie_title"] = movie.movie_title
        datapoint["rating"] = movie.rating
        datapoint["link"] = movie.link
        data.append(datapoint)

    newlist = sorted(data, key=lambda data: data['rating'], reverse=reverse)
    return render_template('profile.html', name=current_user.name, data=newlist, is_rating=is_rating)
