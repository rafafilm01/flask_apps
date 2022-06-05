
#use of  flask --> LoginManager for allowing users to sign in
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#create an instace of login manager 
login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mySecret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
Migrate(app,db)

#configure the application to have management of logged in users 
login_manager.init_app(app)
login_manager.login_view = 'login' #html redirection to login view 