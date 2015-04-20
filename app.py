from flask import Flask, render_template, g, request
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_MIGRATE_REPO'] = SQLALCHEMY_MIGRATE_REPO
db = SQLAlchemy(app)

class Fill(db.Model):
	pet_id = db.Column(db.Integer)
	date_time = db.Column(db.DateTime, primary_key=True)
	water_fill = db.Column(db.Float)
	food_fill = db.Column(db.Float)

	def __init__(self, pet_id, water_fill, food_fill, date_time=None):
		self.pet_id = pet_id
		self.water_fill = water_fill
		self.food_fill = food_fill
		if date_time is None:
			self.date_time = datetime.now()
		else:
			self.date_time = date_time

	def __repr__(self):
		return '{ "id": ' + str(self.pet_id) + ', "water_fill": ' + str(self.water_fill) + ', "food_fill": ' + str(self.food_fill) + ', "time": "' + str(self.date_time) + '"}'

db.create_all()