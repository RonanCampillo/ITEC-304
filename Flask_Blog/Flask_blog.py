import app as app
from flask import Flask, render_template

from forms import LoginForm, RegistrationForm

import os


app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
#app.config['SECRET KEY'] = 'dec443d6f6d59f62154531861eaf6ed8'#

post = [
    dict(author='Oda Eiichiro', title='One Piece', content='Chapter 1061', date_posted='September 22,2022',),
    dict(author='Tabata Yuuki', title='Black Clover', content='Chapter 338', date_posted='September 16,2022')
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', post=post)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)


if __name__ == '__main__':
    app.run(debug=True)
