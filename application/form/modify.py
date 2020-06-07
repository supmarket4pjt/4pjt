from wtforms import StringField, PasswordField
from wtforms.validators import Email, Length, InputRequired
from flask_wtf import FlaskForm


class ModForm(FlaskForm):
    name = StringField('name')
    email = StringField('email',  validators=[InputRequired(), Email(
        message='Invalid email'), Length(max=30)])
