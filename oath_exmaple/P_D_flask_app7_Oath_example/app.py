
#TASK home page that links to a welcome page that is only accessible once you authenticate yourself with google 
#welcome.html will only be available if the user is authenticated , otherwise a custom internal error page will be shown 
#environment variables need to be set up to avoid errors 
# flask_dance references - https://flask-dance.readthedocs.io/en/latest/
# CLIENT_ID and CLINET_SECRET removed , can be added from https://console.cloud.google.com/

#### #needed to run locally without any errors #####
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

############################

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google


#setting up the app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

#setting up the blueprint
#NOTE normally you would save the client ID / client secret as env. variables 
blueprint = make_google_blueprint(client_id='CLIENT_ID_RETRACTED',  #obtained from https://console.cloud.google.com/
                                  client_secret='CLIENT_SECRET_RETRACTED',  #obtained from https://console.cloud.google.com/
                                  offline=True, #change to False if the app is not running locally 
                                  scope=['profile', 'email'] #what info we are pulling rom google on the person who signed in 
                                  )

#register the blueprint , '/login' html will go straight into google to carry out the authentication activity 
app.register_blueprint(blueprint, url_prefix= '/login')

#setting up the templates
#home web page view 
@app.route('/')
def index():
    return render_template('home.html')

#setting up the welcome page with a nested logged in functionality for users who have already signed in 
@app.route('/welcome')
def welcome():
    #RETURN ERROR - INTERNAL SERVER ERROR IF USER NOT LOGGED IN ! WELCOME PAGE WILL NOT WORK CORRECTLY IF A USER TRIES TO JUMP OVER LOGIN PAGE AND GO STRAIGHT TO WELCOME PAGE 
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    email = resp.json()['email']
    
    return render_template('welcome.html', email = email )
    

#setting up a logged in page 
@app.route('/login/google')
def login():
    #check to see if the user is logged in , if not flask dance will redirect the user to google.login in order to sign in 
    
    #### NOTE functionality provided by flask_dance ##########
        if not google.authorized: #pulled from flask_dance.contrib.google library 
            return render_template(url_for('google.login'))
    ######################
    
    
    #if the user is already signed in , retrieve his info 
        resp = google.get("/oauth2/v1/userinfo")
        
        #confirm the response is valid 
        assert resp.ok, resp.text
        
        #grab the email of the person signed in 
        email = resp.json()['email']
        
        return render_template('welcome.html', email = email )
    
    
if __name__  == '__main__':
    app.run()