import config
from flask_mongoengine import MongoEngine
from flask_login.login_manager import LoginManager
from application import db


class User():
    meta = {'collection': 'utilisateur'}
    email = db.StringField(max_length=30)
    password = db.StringField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()
