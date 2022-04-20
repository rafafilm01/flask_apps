# example of template forms 
# example of a custom made 404 page not found 
#request lib used for getting the information from the form 
from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
    

if __name__ =='__main__':
    app.run(debug=True)


