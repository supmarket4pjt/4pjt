from flask import Flask, render_template, request, redirect, url_for
from application.form.regform import RegForm
from application.form.modify import ModForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mongoengine import MongoEngine, Document
from application.models.User import LoginManager
from application.db.db import *
import datetime
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'ShoppingDB',
    'host': 'mongodb+srv://test:test@supmarket-o5fys.mongodb.net/ShoppingDB?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority'
}

db = MongoEngine(app)
app.config['SECRET_KEY'] = 'test'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Document):
    meta = {'collection': 'utilisateur'}
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    createDate = db.DateTimeField()
    number = db.StringField(max_length=20)
    address = db.StringField(max_length=60)


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            existing_user = User.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(
                    form.password.data, method='sha256')
                hey = User(name=form.name.data, email=form.email.data,
                           password=hashpass, createDate=datetime.datetime.utcnow(), address=form.address.data, number=form.number.data).save()
                login_user(hey)
                return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated == True:
        return redirect(url_for('index'))
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            check_user = User.objects(email=form.email.data).first()
            if check_user:
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('adminboard'))
    return render_template('login.html', form=form)


@app.route('/index')
@login_required
def index():
    item = myart.find()
    return render_template('index.html', user=current_user.name, articles=item)


@app.route('/admin', methods=['GET'])
@login_required
def adminboard():
    item = mycol.find()
    return render_template('adminboard.html', admin=current_user.name, users=item)


@app.route('/admin/<user>', methods=['POST', 'GET'])
@login_required
def usermodify(user):
    form = ModForm()
    # do your code here
    if request.method == 'POST':
        myquery = {"name": user}
        newvalues = {"$set": {"name": request.form.get('name'),
                              "email": request.form.get('email'),
                              "address": request.form.get('address'),
                              "number": request.form.get('number')}}

        result = mycol.update_one(myquery, newvalues)
        print("Data updated with id", result)

        # Print the new record
        cursor = mycol.find()
        for record in cursor:
            print(record)
        return redirect(url_for('adminboard'))

    item = mycol.find_one({'name': user})
    return render_template('detail.html', form=form, data=item)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/articles', methods=['GET'])
@login_required
def articleboard():
    item = myart.find()
    return render_template('articleboard.html', admin=current_user.name, articles=item)


@app.route('/articles/<title>', methods=['POST', 'GET'])
@login_required
def articlemodify(title):

    # do your code here
    if request.method == 'POST':
        myquery = {"title": title}
        newvalues = {"$set": {"title": request.form.get('title'),
                              "category": request.form.get('category'),
                              "price": request.form.get('price'),
                              "state": request.form.get('state')}}

        result = myart.update_one(myquery, newvalues)
        print("Data updated with id", result)
        return redirect(url_for('articleboard'))

    item = myart.find_one({'title': title})
    return render_template('detailart.html', data=item)


@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
