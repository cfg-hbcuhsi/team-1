from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
import csv
app = Flask(__name__)
app.secret_key="zbc"

def loaderNetCost(college):
    try:
        data = csv.DictReader(open("net_price.csv"))
        for row in data:
            if college == row['Institution Name']:
                return list(row.items())[7:16]
    except:
        pass


def loaderAdCost(college):
    try:
        data = csv.DictReader(open("sticker_price.csv"))
        for row in data:
            if college == row['Institution Name']:
                return list(row.items())[7:13]
    except Exception as e:
        print(e)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        session['college'] = request.form['college']
        session['income'] = request.form['income']
        return redirect('/home')
    return render_template('index.html')

@app.route('/home', methods=['POST','GET'])
def home():
    college = session.get('college')
    AdCost = loaderAdCost(college)
    NetCost = loaderAdCost(college)
    return render_template('home.html', NetCost=NetCost, AdCost=AdCost, college=college, income=session.get('income'))

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/jobpage')
def jobpage():
    return render_template('jobpage.html')

@app.route('/freefood')
def freefood():
    return render_template('freefood.html')

@app.route('/reciepe')
def reciepe():
    return render_template('reciepe.html')


if __name__ == "__main__":

    data = loaderNetCost("CUNY City College")
    for i in data:
        print(i)