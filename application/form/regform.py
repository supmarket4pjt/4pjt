from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, InputRequired, Length
from wtforms.fields.simple import PasswordField
from wtforms.validators import Email, Length, InputRequired


class RegForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
