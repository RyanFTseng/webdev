from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField

class FirstForm(Form):
    name = TextField("Enter Name")
    age = IntegerField("Enter Age")
    submit = SubmitField("Send")

