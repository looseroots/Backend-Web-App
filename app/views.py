from flask import redirect, url_for, render_template, request, jsonify, session
from app.storage import	upload_to_bucket, download_from_bucket
from werkzeug.utils import secure_filename
from app.forms import UserForm
from app import app

import os

@app.route('/', methods=['GET', 'POST'])
def index():
	userform = UserForm()
	if userform.validate_on_submit():
		username = userform.username.data
		bio = userform.bio.data

		profile_picture = userform.profile_picture.data
		profile_picture_filename = secure_filename(profile_picture.filename)
		file_path = os.path.join(app.config['UPLOAD_FOLDER'], profile_picture_filename)
		profile_picture.save(file_path)

		upload_to_bucket(file_path, profile_picture_filename)

		return 'Successfully submitted form data with username {}, bio {}'.format(username, bio)

	return render_template("index.html", userform=userform)