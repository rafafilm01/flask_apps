#flask app with SQL 
#flask-migrate for migrating BDs once they are updated with new columns 
#NOTE issues with flask db init command  in CMD . Unable to set the environment variable name using CMD and powershell , ended up re-naming the script to app.py 
import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#choose a directory where SQL data will be stored , using absolute path
#code is grabbing the directory of where the basic.py script is 
#NOTE using the os module instead of hard coding the absolute file path will make sure the code always works and it also makes it system independent (WIN/MAC )
basedir =os.path.abspath(os.path.dirname(__file__))
print(basedir) #SANITY CHECK

app =Flask(__name__)


#set up the database location (using the current directory)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#enable  this in order not to track every single change in the DB, normally keep as disabled 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

#creating a database
db=SQLAlchemy(app)

#connect application with the db, needed when current DB is getting changed (e.g adding columns)
Migrate(app,db)

#!! NOTE !!
#set the FLASK_APP environment variable in terminal using:
#MACos/Linux --> export FLASK_APP=basic.py
#Win --> set FLASK_APP=basic.py

#once completed in CMD run --> flask db init
#!! NOTE !!


#setting up a table in the database (model)

class Puppy(db.Model):
    #manual overwrite for the table name if no table name is provided SQLalchemy will create a table based on the name of the class 
    # __tablename__= 'puppies2'
    
    #creating columns for the table
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed =db.Column(db.Text)
    
    #initialize the table , ID does not need to be added as it will be populated automatically since it is a unique primary key 
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed 
        
    #gives u a string representation of the object (table), useful for viewing data or troubleshooting 
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old."
    
#!!NOTE !!
#commands to be typed in the terminal when migrating db : 
# set FLASK_APP=basic.py  --> to set the environment variable to a different name of .py script. Issues with getting it work , a workaround was to rename the script as app.py(default value for FLASK_APP)
# flask db init --> used to initialise  the database
# flask db migrate -m 'comment' --> when changes are made to DB  (git style)
# flask db upgrade --> save changes (git style)
#!!NOTE !!