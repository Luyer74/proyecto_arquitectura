from flask import Blueprint, render_template, redirect, url_for, request, flash
from movies.models import db
from movies.user_class import User
from flask_login import login_user, login_required, logout_user

#Factory method for auth routes
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    user_query = db.query(User)
    user = user_query.filter_by(email=email).first()
    if not user or not password == user.password:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    remember = True if request.form.get('remember') else False
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template("signup.html")


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user_query = db.query(User)
    user = user_query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    pref1 = request.form.get('pref1')
    pref2 = request.form.get('pref2')
    pref3 = request.form.get('pref3')
    preference_dict = {"comedy": 1, "drama": 2,
                       "scifi": 3, "romantic": 4, "adventure": 5}
    pref1 = preference_dict[pref1]
    pref2 = preference_dict[pref2]
    pref3 = preference_dict[pref3]
    magic_number = (pref1 * pref2 * pref3) % 5 + 1
    new_user = User(email=email, name=name, password=password,
                    magic_number=magic_number)

    db.add(new_user)
    db.commit()

    print(email, name, password)
    print(pref1, pref2, pref3)
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
