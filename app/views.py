from flask import redirect, url_for, render_template, request, jsonify
from app.forms import CreateUser, EditProfile
from app import app, gmaps, cred

import firebase_admin #?
from firebase_admin import auth
from firebase_admin import firestore

default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://looseroots-7a373.firebaseio.com'})
db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def index():
	userform = CreateUser()
	profileform = EditProfile()

	if userform.validate_on_submit():
		user = auth.create_user(
			uid=str(userform.username.data),
			email=str(userform.email.data),
			email_verified=True,
			phone_number=str(userform.phone.data),
			password=str(userform.password.data),
			display_name=str(userform.display_name.data),
			disabled=False
		)
		print('Sucessfully created new user: {0}'.format(user.uid))

	if profileform.validate_on_submit():
		user_id = profileform.username.data

		profile = {
			u'bio': profileform.bio.data,
			u'profile_picture_link': profileform.profile_picture_link.data
		}

		db.collection(u'users').document(user_id).set(profile)


	return render_template("index.html", userform=userform, profileform=profileform)