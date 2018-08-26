from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CreateUser(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired()])
	password = StringField('Password', validators=[DataRequired()])
	first_name = StringField('First Name', validators=[DataRequired()])
	phone = StringField('Phone Number', validators=[DataRequired()])

class EditProfile(FlaskForm):
	pass
	# bio = StringField('')