from flask import redirect, url_for, render_template, request, jsonify, session
from app.forms import UserForm
from app import app, gmaps

@app.route('/', methods=['GET', 'POST'])
def index():
	userform = UserForm()
	if userform.validate_on_submit():
		username = userform.username.data
		bio = userform.bio.data
		print(username, bio)

		return 'Successfully submitted form data with username {}, bio {}'.format(username, bio)

	return render_template("index.html", userform=userform)