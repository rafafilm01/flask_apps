#use of UserMixin for features such as login in users and authorizing  users 
#use of werkzeug for enctyption / decryption of passwords 

from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin

#once the user signs in - load him so he can see specific pages tied to their login, load_user method looks for the user_id our model and retrives a match 
@login_manager.user_loader
def load_user (user_id):
    return User.query.get(user_id)


#NOTE custom class inheriting from 2 classes at the same time 
class User(db.Model,UserMixin):
    
    __tablename__ ='users'
    
    id =db.Column(db.Integer, primary_key=True)
    #unique usernam and email ( 64 character limit), also , additional  functionality by setting email field and username as unique entries 
    email =db.Column(db.String(64), unique = True, index= True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash= db.Column(db.String(128))
    
    #initalize the table
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        #NOTE we are not saving the password itself but the hashed version of the password 
        self.password_hash = generate_password_hash(password)
        

#password check method, compare the password provided by the user earlier with the hasshed version of it 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)