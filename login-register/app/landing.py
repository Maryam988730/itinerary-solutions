from flask import Blueprint, render_template

landing = Blueprint('landing', __name__)

@landing.route('/') 
@landing.route('/home')
 # Home page route
def home():
    return render_template('home.html')
