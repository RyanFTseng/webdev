from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
    return ("Hello World!")

@app.route('/welcome')
def welcome():
    return('welcome to flask')

@app.route('/hello/<name>')
def show_user_profile(name):
    return 'hello %s'%(name)

@app.route('/<firstName>/<lastName>')
def user(firstName, lastName):
    return '<h1>Hello,%s%s!<h1>'%(firstName,lastName)

@app.route('/myage/<age>')
def showage(age):
    return 'age %s'%(age)




if __name__=="__main__":
    app.run(host='0.0.0.0')
