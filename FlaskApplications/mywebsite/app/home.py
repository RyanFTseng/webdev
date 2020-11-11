from flask import render_template
from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user={'name':'Antonio'}
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/about/<name>/<age>')
def about(name,age):
    user = {'name':name, 'age': age}
    return render_template('about.html',user=user)

@app.route('/car/<model>/<age>/<color>/<year>')
def duck(model, age, color,year):
    user={ 'model':model, 'age':age, 'color':color, 'year':year}
    return render_template('hometemplate.html',user=user)

if __name__ == '__main__':
    app.run(debug=True)
