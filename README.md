# flask_apps
collection of flask_apps

##### OATH_example: #####

libs used : os, 
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

description:
home page that links to a welcome page that is only accessible once you authenticate yourself with google 
welcome.html will only be available if the user is authenticated , otherwise a custom internal error page will be shown 
environment variables need to be set up to avoid errors (os lib)
flask_dance references - https://flask-dance.readthedocs.io/en/latest/
CLIENT_ID and CLINET_SECRET removed , can be added from https://console.cloud.google.com/
