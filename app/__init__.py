from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/ar')
def ar():
    return render_template('AR.html')