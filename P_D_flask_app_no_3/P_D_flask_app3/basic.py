#flask form examples 
#GET and POST method in use 
#class inheritance (custom class inheriting from FlaskForm class )
#form logic applied in def index(), schema in py code , if statement in jinja on index.html

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app =Flask(__name__)

#configure the secret key , at a later date the secret key should not be hard coded into the app, environment varialbes will be used instead 
app.config['SECRET_KEY']= 'mysecretkey'

#create an instace (wtform class )  of the wtform  and a view that can access the form and check if it is a valid submission 

#creating a new class and inheriting from wtform
#in real life classes would go to their own dedicated files.py but for now they will stay in this script
class InfoForm(FlaskForm):
    
    breed =StringField('what breed are u ? ')
    submit = SubmitField('Submit button')
    
#set up a view 
@app.route('/', methods=['GET','POST'])
def index():
    
    breed = False 
    
    form = InfoForm()
    
    if form.validate_on_submit():
        
        breed =form.breed.data
        form.breed.data= ''
    return render_template ('index.html', form=form, breed=breed)


if __name__ =='__main__':
    app.run(debug=True)