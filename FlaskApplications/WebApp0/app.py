from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import request
from database import Database

app = Flask(__name__)


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/show', methods=['GET','POST'])
def show_entries():
    entries=Database.find_records()
    return render_template('show_entries.html',entries=entries)


@app.route('/edit',methods=['GET','POST'])
def edit_entry():
    if request.method == "POST":
        original_name=request.form.get('original_name')
        name = request.form.get('name')
        school = request.form.get('school')
        code = request.form.get('code')
        email = request.form.get('email')
        phone = request.form.get('phone')
        city = request.form.get('city')
        text = request.form.get('text')
        args = {'name': original_name}
        doc = {
            'n  ame': name,
            'school': school,
            'code': code,
            'email': email,
            'phone': phone,
            'city': city,
            'text': text
            }
        Database.edit_record(args,doc)
        return redirect(url_for('show_entries'))
    return render_template('edit_entry.html')


@app.route('/add',methods = ['GET','POST'])
def add_entry():
    if request.method=="POST":
        name = request.form.get('name')
        school = request.form.get('school')
        code = request.form.get('code')
        email = request.form.get('email')
        phone = request.form.get('phone')
        city = request.form.get('city')
        text = request.form.get('text')
        doc = {
            'name': name,
            'school': school,
            'code': code,
            'email': email,
            'phone': phone,
            'city': city,
            'text': text
            }
        Database.insert_record(doc)
        return redirect(url_for('show_entries'))
    return render_template('add_entry.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_all():
    Database.delete_all()
    return redirect(url_for('show_entries'))


@app.route('/deleteone', methods=['GET', 'POST'])
def delete_one():
    if request.method == "POST":
        name = request.form.get('name')
        doc = {'name': name}
        Database.delete_one(doc)
        return render_template('home.html')
    return render_template('delete_one.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        email = request.form.get('email')
        state = request.form.get('state')
        phone_number = request.form.get('phone_number')
        return redirect(url_for('home',user=user,state=state,email=email,phone_number=phone_number))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
