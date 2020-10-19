
from flask import Flask, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, request, render_template, Response, jsonify

from .models import Patients, Exams
from .models import db, query_pat

from flask_bootstrap import Bootstrap
import time

context = {'now': int(time.time()),
           'strftime': time.strftime}  # Note there are no brackets () after strftime # This means we are passing in a function, # not the result of a function. self.response.write(jinja2.render_template('sometemplate.html', **context))
from wtforms import SubmitField,BooleanField, StringField, PasswordField, validators, ValidationError,DateTimeField, TextField, IntegerField
from flask_wtf import Form
from wtforms.validators import Required, NumberRange
import datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import SubmitField,BooleanField, StringField, PasswordField, validators, ValidationError,DateTimeField, TextField, IntegerField
from flask_wtf import Form
from wtforms.validators import Required, NumberRange
import datetime
from flask_sqlalchemy import SQLAlchemy
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from .forms import Patients_form, Exams_form
import datetime


from config import app_config

# db variable initialization

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)
db.init_app(app)
db.create_all(app=app)



@app.route('/patients', methods=['GET'])
def list_patients():
    pats = db.session.query(Patients).all()
    return render_template('patients.html', pats=pats)


@app.route('/exams', methods=['GET'])
def list_exams():
    exams = db.session.query(Exams).all()
    return render_template('exams.html', exams=exams)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/addpatient', methods=['GET', 'POST'])
def new_patient():
    form = Patients_form(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        patient = Patients(
            name=form.name.data,
            surname=form.surname.data,
            addr=form.addr.data,
            diagnosis=form.diagnosis.data,
            age=form.age.data

        )
        # add employee to the database
        db.session.add(patient)
        db.session.commit()
        flash('Succcess!')


        return redirect(url_for('list_patients'))
    else:
        return render_template('new_patient.html', form=form)


# local imports

@app.route('/addexam', methods=['GET', 'POST'])
def new_exam():
    form = Exams_form(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        exam =Exams(
            name = form.name.data,
        price = form.price.data,
        description = form.description.data,
        )
        # add employee to the database
        db.session.add(exam)
        db.session.commit()
        flash('Success!')

        return redirect(url_for('list_exams'))
    else:
        return render_template('new_exam.html', form=form)



