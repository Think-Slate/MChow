from flask import render_template, request
from app import app, db, Fill

@app.route('/')
def index():
    options = {}

    return render_template('index.html', **options)

@app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>')
def addinfoCurrent(pet_id, water_fill, food_fill):
	options = {}
	db.create_all()

	newfill = Fill(pet_id, water_fill, food_fill)
	db.session.add(newfill)
	db.session.commit()

	return render_template('index.html', **options)  

@app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>/<date_time>')
def addinfoPast(pet_id, date_time, water_fill, food_fill):
	options = {}
	db.create_all()

	newfill = Fill(pet_id, water_fill, food_fill)
	db.session.add(newfill)
	db.session.commit()

	return render_template('index.html', **options)   

@app.route('/petinfo/<int:pet_id>')
def getinfo(pet_id):
	options = {}
	db.create_all()
	options['fills'] = Fill.query.filter_by(pet_id = pet_id).order_by(Fill.date_time).all()

	return render_template('petinfo.html', **options)