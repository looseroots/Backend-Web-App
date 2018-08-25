from flask import Flask
import googlemaps
import os

app = Flask(__name__)
app.config.from_object('config')

gmaps = googlemaps.Client(key=app.config['GMAPS_API_KEY'])

from app import views