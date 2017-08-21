import pandas as pd 
from scipy.spatial.distance import cdist
from flask import Flask, render_template, request, url_for
from main import find_metro 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('insert.html')
    #return df_find_coord['station'].values[0]

@app.route('/metro/', methods=['POST'])
def metro():
    try: 
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])
        station = find_metro(lat,lon) 
    except:
        station = "Не верный формат вводимых данных"
    return render_template('metro.html', station = station)

if __name__ == "__main__":
    app.run(host='127.0.0.1')
