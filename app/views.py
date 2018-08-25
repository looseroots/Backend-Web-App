from flask import redirect, url_for, render_template, request, jsonify
from app.events import get_events
from app import app, gmaps

@app.route('/')
def index():
	return jsonify(pingus='pongus')

@app.route('/events')
def events():
	location = request.args.get('location', None, type=int)

	return jsonify(eventlist=get_events(location))

@app.route('/profile')
def profile():
	pass