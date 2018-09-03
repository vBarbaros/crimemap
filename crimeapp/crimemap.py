from crimeapp import app

from flask import Flask
from flask import render_template
from flask import request

import datetime
import dateparser
import json
import string

import dbconfig
if dbconfig.use_mockDB:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper
    
DB = DBHelper()
categories = ['mugging', 'break-in']


@app.route("/")
def home(error_message=None):
    try:
        crimes = DB.get_all_crimes()
        crimes = json.dumps(crimes)
    except Exception as e:
        print e
        data = None
    return render_template(
        'home.html', 
        crimes=crimes,
        categories=categories,
        error_message=error_message
        )
   
@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    if category not in category:
        return home()
    date = format_date(request.form.get("date"))
    if not date:
        return home('Invalid date. Please use yyyy-mm-dd format.')
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
        return home()
    description = request.form.get("description")
    description = sanitize_string(request.form.get("description"))
    DB.add_crime(category, date, latitude, longitude, description)
    return home()

def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None

def sanitize_string(userinput):
    whitelist = string.letters + string.digits + " !?$.,;:-'()&"
    return filter(lambda x: x in whitelist, userinput)