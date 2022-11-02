from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add/<int:numOne>/<int:numTwo>')
def add(numOne, numTwo):
    return f'Addition is {numOne + numTwo}'

app.run()