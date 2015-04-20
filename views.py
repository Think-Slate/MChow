from flask import render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func
from app import app, db, Fill
import time

@app.route('/')
def index():
    options = {}

    return render_template('index.html', **options)

@app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>')
def addinfoCurrent(pet_id, water_fill, food_fill):
	options = {}
	# db.create_all()
	try:
		newfill = Fill(pet_id, water_fill, food_fill)
		db.session.add(newfill)
		db.session.commit()
	except:
		db.session.rollback()

	return render_template('index.html', **options)  

@app.route('/petinfo/<int:pet_id>/<water_fill>/<food_fill>/<date_time>')
def addinfoPast(pet_id, date_time, water_fill, food_fill):
	options = {}
	# db.create_all()
	try:
		newfill = Fill(pet_id, water_fill, food_fill, date_time)
		db.session.add(newfill)
		db.session.commit()
	except:
		options['error'] = "Error adding fill, rolling back sesison"
		db.session.rollback()

	return render_template('index.html', **options)   

@app.route('/petinfo/<int:pet_id>')
def getinfo(pet_id):
	options = {}
	# db.create_all()
	options['fills'] = Fill.query.filter_by(pet_id = pet_id).order_by(Fill.date_time).all()

	return render_template('petinfo.html', **options)

@app.route('/petinfo/water/<int:pet_id>')
def getinfo_water(pet_id):
	options = {}
	# db.create_all()

	fQ = Fill.query.filter_by(pet_id = pet_id).order_by(Fill.date_time).all()
	consumedDailyMax = {}
	consumedDailyMin = {}
	for item in fQ:
		if item.date_time.date() not in consumedDailyMax or item.water_fill > consumedDailyMax[item.date_time.date()].water_fill:
			consumedDailyMax[item.date_time.date()] = item
		if item.date_time.date() not in consumedDailyMin or item.water_fill < consumedDailyMin[item.date_time.date()].water_fill:
			consumedDailyMin[item.date_time.date()] = item

	consumedDaily = {}
	for key in consumedDailyMax.keys():
		consumedDaily[key] = consumedDailyMax[key].water_fill - consumedDailyMin[key].water_fill

	options['fills'] = consumedDaily
	print options['fills']

	return render_template('petinfo_water.html', **options)

@app.route('/petinfo/food/<int:pet_id>')
def getinfo_food(pet_id):
	options = {}
	# db.create_all()
	fQ = Fill.query.filter_by(pet_id = pet_id).order_by(Fill.date_time).all()
	consumedDailyMax = {}
	consumedDailyMin = {}
	for item in fQ:
		if item.date_time.date() not in consumedDailyMax or item.food_fill > consumedDailyMax[item.date_time.date()].food_fill:
			consumedDailyMax[item.date_time.date()] = item
		if item.date_time.date() not in consumedDailyMin or item.food_fill < consumedDailyMin[item.date_time.date()].food_fill:
			consumedDailyMin[item.date_time.date()] = item

	consumedDaily = {}
	for key in consumedDailyMax.keys():
		consumedDaily[key] = consumedDailyMax[key].food_fill - consumedDailyMin[key].food_fill

	options['fills'] = consumedDaily
	print options['fills']

	return render_template('petinfo_food.html', **options)

@app.route('/petinfo/<int:pet_id>/<after_date_time>')
def getinfoAfter(pet_id, after_date_time):
	options = {}
	# db.create_all()
	print after_date_time
	options['fills'] = Fill.query.filter_by(pet_id = pet_id).filter(Fill.date_time > after_date_time).order_by(Fill.date_time).all()

	return render_template('petinfo.html', **options)

@app.route('/petinfo/water/<int:pet_id>/<after_date_time>')
def getinfoAfter_water(pet_id, after_date_time):
	options = {}
	# db.create_all()
	print after_date_time
	options['fills'] = Fill.query.filter_by(pet_id = pet_id).filter(Fill.date_time > after_date_time).order_by(Fill.date_time).all()

	return render_template('petinfo_water.html', **options)

@app.route('/petinfo/food/<int:pet_id>/<after_date_time>')
def getinfoAfter_food(pet_id, after_date_time):
	options = {}
	# db.create_all()
	print after_date_time
	options['fills'] = Fill.query.filter_by(pet_id = pet_id).filter(Fill.date_time > after_date_time).order_by(Fill.date_time).all()

	return render_template('petinfo_food.html', **options)





