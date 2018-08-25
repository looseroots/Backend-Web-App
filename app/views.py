from flask import redirect, url_for, render_template, request, jsonify
from app.forms import UserForm
from app import app, gmaps, cred

import firebase_admin
from firebase_admin import firestore

default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://looseroots-7a373.firebaseio.com'})
# ref = db.reference(path="/", app=default_app)

db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def index():
	userform = UserForm()
	if userform.validate_on_submit():
		username = userform.username.data

		data = {
			u'firstname': str(userform.firstname.data),
			u'lastname' : str(userform.lastname.data),
			u'bio'		: str(userform.bio.data),
		}

		# users_ref = ref.child('users')
		user_id = db.collection(u'users').document(username).set(data)

		# users_ref.set({
		#     'username': username,
		#     'bio': bio
		# })

		return 'Successfully submitted form data with username'


	return render_template("index.html", userform=userform)