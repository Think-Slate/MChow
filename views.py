from flask import render_template, request
from app import app

@app.route('/')
def index():
    options = {}

    return render_template('index.html', **options)

@app.route('/petinfo/<int:pet_id>')
def getinfo(pet_id):
	options = {}
	options['pet_id'] = pet_id

	return render_template('petinfo.html', **options)