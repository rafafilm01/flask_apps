#forms  for the user to login to the website and register 
import email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
#validators will be passed to StringField and PasswordField to make sure correct type of data is provided (e.g. makes sure the email field is correctly completed )
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User


#login form 
class LoginForm(FlaskForm):
    email =StringField('Email', validators=[DataRequired(), Email()])
    password =StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


#build registration form
class RegistrationForm(FlaskForm):
    email =StringField('Email', validators=[DataRequired(), Email()])
    username=StringField('Username', validators=[DataRequired()])
    #validation check to make sure password and repeated password match 
    password =StringField('Password', validators=[DataRequired(), EqualTo('password_confirm', message="Please make sure both password match ! ")])
    password_confirm= StringField('Confirm Password', validators=[DataRequired()])
    submit= SubmitField('Register ! ')
    
#check the DB to see if the email hasn't been already activated 
    def check_email(self, field):
        #check to see if the email provided by the user in the form is not already in use 
        if User.query.filter_by (email=field.data).first():
        #if the check is true t- raise a validation error and notify the user that email is already in use 
            raise ValidationError('The email you have added has already been registered ! ')
        
#check the DB to see if the username hasn't been already activated 
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first(): 
            raise ValidationError('That username is already taken ! ')