from app import app
from flask import render_template, flash, redirect, url_for
from app.form import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Measurements


@app.route('/')
@app.route('/index')
@login_required 
def index():
	return render_template('index.html', title='Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
	#to prevent logged in users returning to the log in page
	if current_user.is_authenticated:
		return redirect(url_for('index'))#working
	form = LoginForm()
	if form.validate_on_submit():
		user= User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')#working
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != ' ':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))
