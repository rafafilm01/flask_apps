# flask_apps
collection of flask_apps along with notes and descriptions 

##### OATH_example: #####

libs used :
- os 
- from flask import Flask, redirect, url_for, render_template
- from flask_dance.contrib.google import make_google_blueprint, google

description:
- home page that links to a welcome page that is only accessible once you authenticate yourself with google 
- welcome.html will only be available if the user is authenticated , otherwise a custom internal error page will be shown 
- environment variables need to be set up to avoid errors (os lib)
- flask_dance references - https://flask-dance.readthedocs.io/en/latest/
- CLIENT_ID and CLIENT_SECRET removed , can be added from https://console.cloud.google.com/
---

##### flask_app_intro ####

libs used: 
- from flask import Flask, render_template, request

description:

- example of template forms 
- example of a custom made 404 page not found 
- request lib used for getting the information from the form 
- examples of referencing base.html for code uniformity 
- examples of block content 
- examples of filters 
- examples of url_for() (links for templates)
- introduction to render_teamplates
- introduction to jinja (syntax and use)
---

#### flask_app_no2 ####

libs used: 
- from flask import Flask, render_template, request

description:
- example of template forms 
- example of a custom made 404 page not found 
- request library used for getting the information from the form 
- NOTE ! make sure to use the correct bootstrap version as script links will work differently , current bootstrap for the project 4.6
- username validation test under username_check.html . Makes sure username provided by the user meets the conditions 
---

#### flask_app_no3 ####

libs used:
- from flask import Flask, render_template
- from flask_wtf import FlaskForm
- from wtforms import StringField, SubmitField

description:
- flask form examples 
- GET and POST method in use 
- class inheritance (custom class inheriting from FlaskForm class )
- form logic applied in def index(), schema in py code , if statement in jinja on index.html
---

#### flask_app_no4 ####

libs used:
- from flask import Flask, render_template, session, redirect, url_for, flash
- from flask_wtf import FlaskForm
- from wtforms import (StringField, BooleanField, DateField, RadioField, SelectField, 
                     SearchField, TextAreaField, TelField, SubmitField)
                     
description:
- use and examples of form fields
- use of sessions for holding and passing data provided by user in the form
- use of flash for flash alerts / messages  
- redirect - url_for used as an alternative to routing web traffic in HTML code 
- NOTE flow of the program --> variables used in forms are described in classes along with potential answers  (which inherits types of form fields from flaskForm), then these parameters are  put together in a form created from the custom class we set up earlier and called on in app.route / def new_function . Session is being used for the input data to be stored and moved forward. Lastly in the HTML code we need establish form elements (so that they are showing and in which order ). form.object.label & form.object(for user selection / input)
                     
#### flask_app_no5 ####

libs used:
- import os 
- from flask import Flask
- from flask_sqlalchemy import SQLAlchemy
- from flask_migrate import Migrate

description:
-flask SQLalchemy in use alng with examples 
- creating a model (table) in SQLAlchemy 
- process for activating a DB in terminal
---
