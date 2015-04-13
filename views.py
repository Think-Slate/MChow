from flask import render_template, request
from app import app, db, Fill

@app.route('/')
def index():
    options = {}

    return render_template('index.html', **options)

@app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>')
def addinfoCurrent(pet_id, water_fill, food_fill):
	options = {}

	newfill = Fill(pet_id, water_fill, food_fill)
	db.session.add(newfill)
	db.session.commit()

	return render_template('index.html', **options)  

@app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>/<date_time>')
def addinfoPast(pet_id, date_time, water_fill, food_fill):
	options = {}

	newfill = Fill(pet_id, water_fill, food_fill)
	db.session.add(newfill)
	db.session.commit()

	return render_template('index.html', **options)   

@app.route('/petinfo/<int:pet_id>')
def getinfo(pet_id):
	options = {}

	options['fills'] = Fill.query.filter_by(pet_id = pet_id).order_by(Fill.date_time).all()

	return render_template('petinfo.html', **options)

@app.route('/petinfo/<int:pet_id>/<after_date_time>')
def getinfoAfter(pet_id, after_date_time):
	options = {}
	
	print after_date_time
	options['fills'] = Fill.query.filter_by(pet_id = pet_id).filter(Fill.date_time > after_date_time).order_by(Fill.date_time).all()

	return render_template('petinfo.html', **options)