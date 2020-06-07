from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired


class RegForm(FlaskForm):
    name = StringField('name')
    email = StringField('email',  validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=8, max=20)])
    verify = PasswordField('verify')
    address = StringField('address')
    number = StringField('number')
