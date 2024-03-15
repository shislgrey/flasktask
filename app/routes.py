from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Terry'}
    posts = [
        {
            'author': {'username': 'Kevin'},
            'body': 'Tiffany Aching kicks all the ass!'
        },
        {
            'author': {'username': 'Grey'},
            'body': 'I ship Polly and Maladict'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)