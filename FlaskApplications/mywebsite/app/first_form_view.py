from flask import Flask, render_template, request, flash
from first_form import FirstForm
app = Flask(__name__)
app.secret_key = 'my secret key'

@app.route('/firstform', methods = ['GET', 'POST'])
def first_form():
    form = FirstForm()
    if request.method == 'POST':
        if form.validate()==True:
            flash('All fields are required.')
            return render_template('first_form.html',form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
            return render_template('first_form.html', form = form)
if __name__ == '__main__':
    app.run(debug = True)
