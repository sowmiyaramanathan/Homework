from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add/<int:numOne>/<int:numTwo>')
def add(numOne, numTwo):
    return f'Addition is {numOne + numTwo}'

@app.route('/sub/<int:numOne>/<int:numTwo>')
def sub(numOne, numTwo):
    return f'Difference is {numOne - numTwo}'

@app.route('/mul/<int:numOne>/<int:numTwo>')
def mul(numOne, numTwo):
    return f'Product is {numOne * numTwo}'

@app.route('/div/<int:numOne>/<int:numTwo>')
def div(numOne, numTwo):
    return f'Division is {numOne / numTwo}'


@app.route('/calc')
def calc():
    return render_template('calc.html')

@app.route('/sqr/<int:numOne>')
def sqr(numOne):
    return f'Square of {numOne} is {numOne * numOne}'

@app.route('/cub/<int:numOne>')
def cub(numOne):
    return f'Cube of {numOne} is {numOne * numOne * numOne}'

app.run()