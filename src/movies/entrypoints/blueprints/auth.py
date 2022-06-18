from flask import Blueprint, render_template, redirect, url_for, request
from movies.models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    pref1 = request.form.get('pref1')
    pref2 = request.form.get('pref2')
    pref3 = request.form.get('pref3')
    magic_number = 1
    new_user = User(email=email, name=name, password=password, magic_number=magic_number)

    db.add(new_user)
    db.commit()

    print(email, name, password)
    print(pref1, pref2, pref3)
    return redirect(url_for('auth.login'))

@auth.route('/login')
def logout():
    return 'logout'