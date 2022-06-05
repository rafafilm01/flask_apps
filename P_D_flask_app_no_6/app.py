
# flask relationships setting up DBs that relate to one another using the foreign_key 
#example of a boiler plate for flask app with SQL DB
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# !! boilerplate to setting up a flask app along with a DB 
basedir =os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# !! boilerplate to setting up a flask app along with a DB

#setting up tables 
class Puppy(db.Model):
    __tablename__ ='puppies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    #one to many relationship --> puppy can have many toys 
    toys =db.relationship('Toy', backref='puppy', lazy='dynamic') 
    #one to one relationship --> 1 oup can only have 1 owner
    # NOTE userlist is by default set up to true  which will enable one to many relationship, by setting it to false you are forcing the connection to be one to one 
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    
    #initialise to create the table 
    def __init__(self,name):
        self.name = name
    
    #create a reporting string to give back the search results    
    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and the owner is {self.owner.owner_name}"
        else:
            return f"Puppy name is {self.name} and it has no owner yet"
    
    #create a report on the number of toys a puppy has     
    def report_toys(self):
        print('Here are my toys: ')
        for toy in self.toys:
            print(toy.item_name)
           
         
            # ?? use a join method to better display the results 
    


class Toy(db.Model):
    
    __tablename__ = 'toys'
    
    id= db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    #reference to the puppy table to link the primary key from it as a foreign key in toys table 
    puppy_id =db.Column(db.Integer, db.ForeignKey('puppies.id'))
    
    #initialise to create the table 
    def __init__(self,item_name,puppy_id):
        self.item_name =item_name
        self.puppy_id=puppy_id
        
        

class Owner(db.Model):
    __tablename__  ='Owner'
    
    id =db.Column(db.Integer, primary_key=True)
    owner_name =db.Column(db.Text)
    #connect the owner to the puppy. primaryKey (puppies) - foreignKey (Owner)
    puppy_id=db.Column(db.Integer, db.ForeignKey('puppies.id'))
    
    #initialise to create the table
    def __init__(self, owner_name, puppy_id):
        self.owner_name =owner_name
        self.puppy_id =puppy_id