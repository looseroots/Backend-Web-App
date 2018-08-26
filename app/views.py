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
	create_user_form = CreateUser()
	# edit_profile_form = EditProfile()

	if create_user_form.validate_on_submit():
		user = auth.create_user(
			uid=str(create_user_form.username.data),
			email=str(create_user_form.email.data),
			email_verified=True,
			phone_number=str(create_user_form.phone.data),
			password=str(create_user_form.password.data),
			display_name=str(create_user_form.display_name.data),
			disabled=False
		)
		print('Sucessfully created new user: {0}'.format(user.uid))


	# if edit_profile_form.validate_on_submit():
	# 	user_info = {
	# 		u'bio': profileform.bio.data,
	# 		u'profile_picture': profileform.profile_picture.data
	# 	}
	# 	db.collection(u'users').document(user.uid).set(user_info)


	return render_template("index.html", userform=create_user_form)