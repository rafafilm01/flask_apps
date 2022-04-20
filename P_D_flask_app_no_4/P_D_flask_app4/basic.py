#use and examples of form fields
#use of sessions for holding and passing data provided by user in the form
# use of flash for flash alerts / messages  
# redirect - url_for used as an alternative to routing web traffic in HTML code 


from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField, RadioField, SelectField, 
                     SearchField, TextAreaField, TelField, SubmitField)

#NOTE flow of the program --> variables used in forms are described in classes along with potential answers  (which inherits types of form fields from flaskForm), then these parameters are  put together in a form created from the custom class we set up earlier and called on in app.route / def new_function . Session is being used for the input data to be stored and moved forward. Lastly in the HTML code we need establish form elements (so that they are showing and in which order ). form.object.label & form.object(for user selection / input)

#simple validator , making sure data is provided before the form is submitted, various validators are available 
from wtforms.validators import DataRequired

app= Flask(__name__)

app.config['SECRET_KEY'] ='myKey'

class InfoForm(FlaskForm):
    #by adding the validatros we will force the user to provide the data before the form can be submitted NOTE dataRequired needs to be called () in order to work 
    breed =StringField('What breed are you? ', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered ? ')
    #with radio buttons only 1 can be selected at a time , we use tuple pairs to describe button and provide description for the user 
    mood = RadioField('Please choose your mood: ', 
                      choices=[('mood_one', 'Happy'),
                               ('mood_two', 'excited'),
                               ('mood_three','sad'),
                               ('mood_four','curious'),                      
                      ])
    food_choice = SelectField('Pick you favourite food: ', 
                              choices=[('option_1', 'chicken'),
                                       ('option_2','beef'),
                                       ('option_3','fish'),
                                       ] )
    feedback= TextAreaField()
    submit =SubmitField('Smash that submit button ! ')
    
    
#based on the class a simple form is created, for loop is run and once the if condition is met a flash message is generated . Once flash is hit it gets passed to HTML code - get_flashed_messages and a flash message is brought up on the screen . Code for flash alerts can be obtained from bootstrap - components - alerts 
class Click_me_form(FlaskForm):
    breed =StringField('what breed are you?: ')
    submit =SubmitField('Click me !')
    
@app.route('/', methods=['GET', 'POST'])
def index():
    
    #create an instace of the form 
    form = InfoForm()
    if form.validate_on_submit():
        
    #session used to pass data from the template (filled byt the user)  to the form automatically  , session will hold the data temporarily (on the server). Session attributes are created like dictionary items
    
        session['breed']= form.breed.data
        session['neutered']=form.neutered.data
        session['mood']=form.mood.data
        session['food']= form.food_choice.data
        session['feedback']=form.feedback.data
        
        #use the redirect and URL_FOR , usefull  to have the form redirected automatically  to a different page (like a thankYou page ) instead of doing the redirection from the HTML side 
        return redirect(url_for('thank_you'))
    
    return render_template(u'index.html', form=form)        

#create a thank you page for when the form is submitted
@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')


@app.route('/click_me_form', methods=['GET','POST'])
def click_me():
    form=Click_me_form()
    
    if form.validate_on_submit():
        session['breed']=form.breed.data
        flash(f"You just changed your breed to : {session['breed']} ! " )
        
        return redirect(url_for('click_me'))
    return render_template('click_me.html', form=form)
    
if __name__=='__main__':
    app.run(debug=True)
