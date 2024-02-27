import pyrebase
from flask import Flask, render_template, request

from model import predict_beneficiaries

app = Flask(__name__)



config = {"apiKey": "AIzaSyBzw2vT9PRwtti51TF2O1qqXq1m9dUR1i4",
  "authDomain": "solutionchallenge-4affd.firebaseapp.com",
  "databaseURL": "https://solutionchallenge-4affd-default-rtdb.firebaseio.com",
  "projectId": "solutionchallenge-4affd",
  "databaseURL":"https://solutionchallenge-4affd-default-rtdb.firebaseio.com",
  "storageBucket": "solutionchallenge-4affd.appspot.com",
  "messagingSenderId": "752159457680",
  "appId": "1:752159457680:web:ff263fd5543bfb6c3bf315"}

firebase = pyrebase.initialize_app(config)
database = firebase.database()


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    contact = request.form['contact']
    event_name = request.form['event-name']
    address = request.form['address']
    date = request.form['date']
    event_type = request.form['event-type']
    rice = request.form['rice']
    daal = request.form['daal']
    sweet = request.form['sweet']
    chapati = request.form['chapati']


    #predicting no of beneficieries
    beneficieries=predict_beneficiaries(int(rice), int(chapati), int(daal), int(sweet))


    data = {'name': name, 'contact': contact, 'event_name': event_name,
            'address': address,
            'date': date,
            'event_type': event_type,
            'rice': rice,
            'daal': daal,
            'sweet': sweet,
            'chapati': chapati,
            'beneficieries': int(beneficieries)

            }



    database.child(event_name).set(data)
    print(data)
    print("no of :", beneficieries)


    print("done")
    return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)

