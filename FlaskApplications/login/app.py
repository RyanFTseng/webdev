from flask import Flask
from flask import render_template,flash,request,redirect,url_for,session
from flask import request
from login_database import Database


app = Flask(__name__)
app.secret_key='secret'

@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username'),
        d=Database.find_one(username)
        if d is None:
            password = request.form.get('password'),
            email = request.form.get('email')
            Database.signup(username, password, email)
        else:
            return 'Username already exists'
        return redirect(url_for('home'))
    return render_template('signup.html')


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        existing_username = Database.find_one({'username': username})
        if existing_username:
            print(existing_username['password'], request.form['password'])
            if existing_username['password'] == request.form['password']:
                print('hello')
                session['name'] = request.form['name']
                return redirect('')
        return 'Invalid username/password'
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username'),
        d=Database.find_one({'username':username})
        if d:
            session['logged_in']= True
            return render_template('show_profile.html')
        else:
            flash('wrong password')
    return render_template('login.html')


@app.route('/show')
def show():
    entries = Database.find_records()
    return render_template('show_all.html', entries=entries)


@app.route('/clear')
def clear():
    Database.clear()
    return redirect(url_for('home'))


@app.route('/show_profile')
def show_profile():
    return render_template('show_profile.html')


if __name__ == '__main__':
    app.run(debug=True)