#examples of referencing base.html for code uniformity 
#examples of block content 
#examples of filters 
#examples of url_for() (links for templates)
from flask import Flask, render_template

app= Flask(__name__)


#base.html is used as the main source of HTML code, it is never referenced directly but links to the base.html are given in every other html page . Differences in other websites are walled off using %block statements % 

#use of filters (in html code ) - varaible | function . Example name |caopitalize  . USed for python functions  that can be passed and work on the variables inside the HTML code 
@app.route('/')
def index():
    return render_template('home.html')

#URL_FOR() used in base.html - used for linking to internal sites of our webpage. Use {{url_for(name_of_the_view_function)}} to route to the desired page 
#in a similar syntax, linking to static images can be done with url_for('static' , filename=filename.png)
@app.route('/pup/<name>')
def puppies(name):
    return render_template('pup.html', name=name)

if __name__ =='__main__':
    app.run(debug=True)