#use of flash and abort from flask lib 


from myproject import app, db
from myproject import User
from myproject.forms import LoginForm, RegistrationForm
from flask import render_template, redirect, request, url_for,flash, abort
from flask_login import login_user, login_required, logout_user

#creating views for specific pages 
@app.route('/')
def home():
    return render_template('home.html')

#in order for the user to see the WELCOME page he needs to login first , that is why there are 2 decorators 
# if a user tries to access this page without signing in, he will be redirected and asked to sign in 
@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

#log out page also requires successful sign in before it can be accessed 
@app.route('/logout')
@login_required # <--login requirement 
def logout():
    #logout_user accessed from flask library
    logout_user()
    #flash popup message on the screen 
    flash('You have logged out ! Nice...')
    return redirect(url_for('home'))

#login page 
@app.route('/login', methods=['POST', 'GET'])
def login():
    
    form =LoginForm()
    if form.validate_on_submit():
        #create a login from using the custom template 
        form =LoginForm()
        
        #a check before each registration. Functionality locked due to security concerns 
        user = User.query.filter_by(email=form.email.data).first()
        
        if user.check_password(form.password.data) and user is not None:
         
            #LOG IN THE USER , once a check is carried out and the user has registered he will see the flash message confming successfull sign in activity      
            login_user(user)
            flash ('you have signed in')
            
            #when a user is trying  to access the webpage the REQUIRES login. Used when user is trying to navigate to a page before going into the login page first 
            next=request.args.get('next')          
            
            #if next exist or is a welcome page 
            if next == None or not next[0] == '/' :
                next =url_for('welcome_user')
                
            return redirect(next)
         
        return render_template('login.html', form=form) 
    
#create a registration view 
@app.route('/registration', methods=['POST','GET'])
def register():
    #initialise a form forms.RegistrationForm
    form = RegistrationForm()
    
    #validate the form and include its elements
    if form.validate_on_submit():
        user = User( email = form.email.data,
                    username = form.username.data,
                    password =form.password.data                    
                    )
        
        #add the user to the model
        db.session.add(user)
        db.session.commit()
        #confirmation message for the user 
        flash('Thanks for registration !')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)