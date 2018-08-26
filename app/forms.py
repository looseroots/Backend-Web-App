from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired, Optional

class UserForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	bio = StringField('Bio', validators=[DataRequired()])
	profile_picture = FileField('Profile Picture', validators=[FileRequired()])