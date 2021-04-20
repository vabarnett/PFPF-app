from app import app
from flask import render_template, flash, redirect, url_for, request
from app.form import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app import db
from app.form import RegistrationForm, EditMeasurementsForm


@app.route('/')
@app.route('/index')
@login_required 
def index():
	return render_template('index.html', title='Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
	#to prevent logged in users returning to the log in page
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user= User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))#directs to homepage
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	return render_template('user.html', user=user)

@app.route('/edit_measurements', methods=['GET', 'POST'])
@login_required
def edit_measurements():
	form = EditMeasurementsForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.waist = form.waist.data
		current_user.bust = form.bust.data
		current_user.hips = form.hips.data
		current_user.w2k = form.w2k.data
		current_user.k2a = form.k2a.data
		db.session.commit()
		flash('Your changes have been saved.')
		return redirect(url_for('edit_measurements'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.waist.data = current_user.waist
		form.bust.data = current_user.bust
		form.hips.data = current_user.hips
		form.w2k.data = current_user.w2k
		form.k2a.data = current_user.k2a
	return render_template('edit_measurements.html', title='Edit Profile',
		form=form)
@app.route('/light')#testing a little Javascript with buttons to change a GIF 
def light():
	return render_template('light.html', title='light')