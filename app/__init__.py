from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/jobpage')
def jobpage():
    return render_template('jobpage.html')

@app.route('/freefood')
def freefood():
    return render_template('freefood.html')
