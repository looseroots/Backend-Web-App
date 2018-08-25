import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

from flask import redirect, url_for, render_template, request, jsonify
from app.events import get_events
from app import app, gmaps

cred = credentials.Certificate('looseroots-7a373-firebase-adminsdk-wwa1y-60d6bc043b.json')
default_app = firebase_admin.initialize_app(cred)

# Get a database reference to server
ref = db.reference('server')

@app.route('/')
def index():

	users_ref = ref.child('users')

	users_ref.set({
	    'username': username
	    'bio': bio
	})

	return jsonify(pingus='pongus')

@app.route('/events')
def events():
	location = request.args.get('location', None, type=int)

	return jsonify(eventlist=get_events(location))

@app.route('/profile')
def profile():
	pass