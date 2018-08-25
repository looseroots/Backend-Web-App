from flask import redirect, url_for, render_template, request, jsonify
from app.forms import UserForm
from app import app, gmaps, cred

import firebase_admin
from firebase_admin import db

default_app = firebase_admin.initialize_app(cred)

@app.route('/', methods=['GET', 'POST'])
def index():
	userform = UserForm()
	if userform.validate_on_submit():
		username = userform.username.data
		bio = userform.bio.data

		users_ref = db.child('users')

		users_ref.set({
		    'username': username,
		    'bio': bio
		})

		return 'Successfully submitted form data with username {}, bio {}'.format(username, bio)


	return render_template("index.html", userform=userform)