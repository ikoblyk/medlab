from flask_sqlalchemy import SQLAlchemy

import datetime


db = SQLAlchemy()

class Patients(db.Model):
   id = db.Column('patient_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   surname = db.Column(db.String(100))
   addr = db.Column(db.String(200))
   diagnosis = db.Column(db.String(100))
   age = db.Column(db.Integer)





class Exams(db.Model):
   id = db.Column('exam_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   price = db.Column(db.Integer)
   description = db.Column(db.String(100))

def query_pat():
   return db.session.query(db.Patients).all()
