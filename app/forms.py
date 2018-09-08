from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateUser(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	password = StringField('Password', validators=[DataRequired()])
	first_name = StringField('First Name', validators=[DataRequired()])
	phone = StringField('Phone Number', validators=[DataRequired()])
	submit = SubmitField('Sign In')

class EditProfile(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	bio = StringField('Bio', validators=[DataRequired()])
	submit = SubmitField('Submit')