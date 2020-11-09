from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template,flash,request,redirect,url_for,session
from flask import request
from database import Database
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)
app.secret_key='secret'

@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def home():
    flash("hello user")
    return render_template('base.html', current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)