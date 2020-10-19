from wtforms import SubmitField,BooleanField, StringField, PasswordField, validators, ValidationError,DateTimeField, TextField, IntegerField
from flask_wtf import Form
from wtforms.validators import Required, NumberRange
import datetime


class Patients_form(Form):
    name = TextField('name', validators = [Required()])
    surname =  TextField('surname', validators = [Required()])
    addr =  TextField('addr', validators = [Required()])
    diagnosis =  TextField('diagnosis', validators = [Required()])
    age = IntegerField('age', validators = [Required()])
    submit = SubmitField('Add')



def _get_date():
    return datetime.datetime.now()


class Exams_form(Form):
    name = TextField('name', validators=[Required()])
    price = IntegerField('price', validators=[Required(), NumberRange(min=0, max=8000)])
    description = TextField('description', validators=[Required()])
    submit = SubmitField('Add Exam')