#introduction to render_teamplates 
#introduction to jinja (syntax and use)
from flask import Flask, render_template

app = Flask(__name__)


#routing is pointed to a basic2.html located in the template folder , This is how we normally populate HTML code instead of having fragments of it scattered in py code.  Example of pointing to a startic file in the basic2.html
#check out unsplash for more free images
#using jinja templates we can directly install python variables into our HTML code . The syntax for jinja is {{some_variable}}
@app.route('/')
def index():
    #variable is established in python and then using jinja passed to HTML in the .html file. The variable needs to be defined in .py. Basci python logic nca be used (operations on lists , dictionaries, for loops etc) 
    my_variable ='Visitor'
    return render_template('basic2.html', my_variable=my_variable)

#jinja can use control flow statements (e.g for loops , if statements ), for this we use the following syntax {% %}. Example of syntax:
#PYTHON LOGIC IS ADDED TO .HTML FILES , ONLY VARIABLES ARE DEFINED IN .PY
# <ul>
#     {% for item in my_list%}
#     <li>{{item}}</li>
#     {% endfor %}
# </ul>

#variable description in .py but the logic is placed in jinja format placed in HTML files , example of for loops and if / else in basic2.html
#real life example - logic to chek if the user is still logged in 
@app.route('/jinja')
def jinja_example():
    my_list = [1,2,3,4,5]
    puppies =['rufus', 'brian', 'snoopy']
    #T/F flag to see if the user is logged in () real life scenario) 
    user_logged_in =False
    return render_template('jinja_example.html', my_list=my_list, puppies=puppies, user_logged_in=user_logged_in)
if __name__ =='__main__':
    app.run(debug=True)   