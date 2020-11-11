from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField, TextAreaField, PasswordField

class SampleWidgetsForm(FlaskForm):
    sample_radio_field = RadioField('Sample Radio Field',
                                    choices =[('button1','Button1'),
                                              ('button2', 'Button2')])
    sample_select_field = SelectField('Sample Select Field', choices = [ ('C Plus Language', 'C++'),
                                                                         ('Python Language', 'Python'),
                                                                         ('Java Language', 'Java')])
    sample_textarea_field = TextAreaField('Sample Text Area Field')
    
    sample_password_field = PasswordField('Sample Text password Field')

    submit = SubmitField("Submit")
    
