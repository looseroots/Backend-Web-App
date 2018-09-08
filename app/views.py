from flask import redirect, url_for, render_template, request, jsonify, flash
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
	form = CreateUser()

	if form.validate_on_submit():
		user = auth.create_user(
			uid=form.username.data,
			email=form.email.data,
			email_verified=False,
			# phone_number=form.phone.data,
			password=str(form.password.data),
			display_name=form.username.data,
			disabled=False)
		return redirect(url_for('profile'))

	return render_template("user.html", title='Create User', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
	profileform = EditProfile()

	if profileform.validate_on_submit():
		user_id = profileform.username.data

		profile = {
			u'bio': profileform.bio.data,
		}
		db.collection(u'users').document(user_id).set(profile)
		return redirect(url_for('index'))

	return render_template("profile.html", title='Edit Profile', profileform=profileform)


@app.route('/create', methods=['GET', 'POST'])
def createUser():
	user = auth.create_user(
		uid=str("username"),
	    email='user@example.com',
	    email_verified=False,
	    phone_number='+15555550100',
	    password='secretPassword',
	    display_name='John Doe',
	    photo_url='http://www.example.com/12345678/photo.png',
	    disabled=False)

	return redirect(url_for('profile'))
