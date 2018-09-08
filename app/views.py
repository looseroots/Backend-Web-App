from flask import redirect, url_for, render_template, request, jsonify
from app.forms import CreateUser, EditProfile
from app import app, gmaps, cred

import firebase_admin #?
from firebase_admin import auth
from firebase_admin import firestore

default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/user', methods=['GET', 'POST'])
def user():
	userform = CreateUser()

	if userform.validate_on_submit():
		user = auth.create_user(
			uid=str(userform.username.data),
			email=str(userform.email.data),
			email_verified=False,
			phone_number=str(userform.phone.data),
			password=str(userform.password.data),
			display_name=str(userform.display_name.data),
			disabled=False)
		print('Sucessfully created new user: {0}'.format(user.uid))

	return render_template("user.html", userform=userform)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
	profileform = EditProfile()

	if profileform.validate_on_submit():
		user_id = profileform.username.data

		profile = {
			u'bio': profileform.bio.data,
			u'profile_picture_link': profileform.profile_picture_link.data
		}

		db.collection(u'users').document(user_id).set(profile)

	return render_template("profile.html", profileform=profileform)


@app.route('/create', methods=['GET', 'POST'])
def createUser():
	user = auth.create_user(
		uid='username',
	    email='user@example.com',
	    email_verified=False,
	    phone_number='+15555550100',
	    password='secretPassword',
	    display_name='John Doe',
	    photo_url='http://www.example.com/12345678/photo.png',
	    disabled=False)

	return redirect(url_for('profile'))
