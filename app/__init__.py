from google.cloud.storage.client import Client
from firebase_admin import credentials
from firebase_admin import storage
from flask import Flask

import firebase_admin
import os

app = Flask(__name__)
app.config.from_object('config')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = app.config['GOOGLE_APPLICATION_CREDENTIALS_PATH']

cred = credentials.Certificate('looseroots-7a373-firebase-adminsdk-wwa1y-60d6bc043b.json')
firebase_admin.initialize_app(cred, {
	'storageBucket': 'looseroots-7a373.appspot.com'
})

cloud_storage_client = Client()

from app import views