from app import db
db.create_all()
from app import Fill
fill1 = Fill(5050, 10, 12)
db.session.add(fill1)
db.session.commit()
fill1 = Fill(5050, 3, 4)
db.session.add(fill1)
db.session.commit()
print Fill.query.filter_by(pet_id = 5050).order_by(Fill.date_time).all()
