import config
from flask_mongoengine import MongoEngine
from flask_login.login_manager import LoginManager
from application import app


db = MongoEngine(app)
app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User():
    meta = {'collection': '<---YOUR_COLLECTION_NAME--->'}
    email = db.StringField(max_length=30)
    password = db.StringField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()
