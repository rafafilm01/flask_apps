
from flask import Flask

#create an app 
app =Flask(__name__)

#used for routing to specific pages of the webiste, '/' is the root of the page, should always be pointing to the page's index 
@app.route('/')
def index():
    return '<h1> This is the home page !</h1>'

@app.route('/standard_route')
def standard():
    return '<h1> this is an example of a standard route  </h1>'

#dynamic route allows for URLs to change depending on the info provided in the code (which can change), used for profike pages for specific users , or page numbers user provides when searching for info www.wite.com/user/unique_user_name
@app.route('/user/<username>')
def user_name(username):
    return f'<h1>Welcome back {username}</h1>'

#puppy latin exercise  - name of the dog provided in the URL needs to change, if it does not end with 'y' , 'y' needs to be added to the end of it . If it already ends with 'y' , 'y' needs to be removed and replaced with 'iful'
@app.route('/puppy_latin/<name>')
def latin_name(name):
    if name[-1]=='y':
        last_character =name[-1]
        new_name =name.replace('y','iful')
        
        return f'<h1>Hi {name}! Your latin name is {new_name}, last character is {last_character}</h1>'
    else:
        return f'Hi {name}! Your latin name is {name}y . That was easy ! '
    
#ALTERNATIVE LOGIC SOLUTION, complete return statement used (returned only once as opposed to the other example) pupname =name[:-1] - pupname is the same as name EXCLUDING the last character + the new variable 
@app.route('/puppy_latin_2/<name>')
def latin_name2(name):
    pupname =''
    if name[-1]=='y':
        pupname =name[:-1] +'iful'
    else:
        pupname =name +'y'
    return f'<h1> Hi {name}! Your latin name is {pupname} !  '
#here we run the actual app, the code makes sure that if we run the basic.py script the application is initialized 


if __name__ =='__main__':
    #running app in debug mode will allow for better error identification, that way we get more specific  flask errors if a link is broken 
    app.run(debug=True)