from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SubmitField 
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User 


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')


	def validate_username(self, username):#prevents duplication of usernames
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):#prevents duplication of email addresses
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')

class EditMeasurementsForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	waist = TextAreaField('Waist', validators=[Length(min = 0, max = 10)])
	bust = TextAreaField('Chest', validators=[Length(min = 0, max = 10)])
	hips = TextAreaField('Hips', validators=[Length(min = 0, max = 10)])
	w2k = TextAreaField('Waist to knee', validators=[Length(min = 0, max = 10)])
	k2a = TextAreaField('Knee to ankle', validators=[Length(min = 0, max = 10)])
	submit = SubmitField('Submit')
	
