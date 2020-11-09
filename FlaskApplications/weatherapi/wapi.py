from flask import Flask
from Database import Database
from flask import render_template,request,redirect,url_for
from datetime import datetime
import urllib3, json

app = Flask(__name__)

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def home():
    Database.delete_all()
    state='CA'
    city='Fremont'
    http=urllib3.PoolManager()
    r=http.request('GET',
                   'http://api.wunderground.com/api/f3c442098e60ca9c/conditions/q/'+state+'/'+city+'.json')
    f=json.loads(r.data.decode('utf-8'))
    a=f['current_observation']['observation_location']
    b=f['current_observation']['weather']
    c=f['current_observation']['temperature_string']
    d=f['current_observation']['relative_humidity']
    e=f['current_observation']['wind_string']
    g = f['current_observation']['wind_mph']
    h = f['current_observation']['icon_url']
    print(f)
    print(a)
    weather=[city,state,b,h,c,d,e,g]
    print(weather)
    doc = {
        'location':a,
        'weather':b,
        'tempstring':c,
        'humidity':d,
        'wind':g,
        'icon':h
    }
    Database.insert_record(doc)
    return render_template('home.html')


@app.route('/show', methods=['GET','POST'])
def show_entries():
    entries=Database.find_records()
    return render_template('showentries.html',entries=entries)

if __name__ == '__main__':
    app.run(debug=True)
