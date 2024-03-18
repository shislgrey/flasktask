from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User
from flask_login import logout_user
from flask_login import login_required

@app.route('/')
@app.route('/index')
@login_required
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
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(user.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))