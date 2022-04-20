# flask_apps
collection of flask_apps

##### OATH_example: #####

libs used :
os 
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

description:
home page that links to a welcome page that is only accessible once you authenticate yourself with google 
welcome.html will only be available if the user is authenticated , otherwise a custom internal error page will be shown 
environment variables need to be set up to avoid errors (os lib)
flask_dance references - https://flask-dance.readthedocs.io/en/latest/
CLIENT_ID and CLINET_SECRET removed , can be added from https://console.cloud.google.com/

##### flask_app_intro ####

libs used: 
from flask import Flask, render_template, request

description:

example of template forms 
example of a custom made 404 page not found 
request lib used for getting the information from the form 
examples of referencing base.html for code uniformity 
examples of block content 
examples of filters 
examples of url_for() (links for templates)
introduction to render_teamplates 
introduction to jinja (syntax and use)


#### flask_app_no2 ####

libs used: 
from flask import Flask, render_template, request

description:
example of template forms 
example of a custom made 404 page not found 
request library used for getting the information from the form 
NOTE ! make sure to use the correct bootstrap version as script links will work differently , current bootstrap for the project 4.6
username validation test under username_check.html . Make sure username provided by the user meets our conditions 
