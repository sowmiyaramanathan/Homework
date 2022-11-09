from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/add/<int:numOne>/<int:numTwo>')
def add(numOne, numTwo):
    return str(numOne + numTwo)

@app.route('/sub/<int:numOne>/<int:numTwo>')
def sub(numOne, numTwo):
    return str(numOne - numTwo)

@app.route('/mul/<int:numOne>/<int:numTwo>')
def mul(numOne, numTwo):
    return str(numOne * numTwo)

@app.route('/div/<int:numOne>/<int:numTwo>')
def div(numOne, numTwo):
    return str(numOne / numTwo)


@app.route('/calc')
def calc():
    return render_template('calc.html')

@app.route('/sqr/<int:numOne>')
def sqr(numOne):
    return str(numOne * numOne)

@app.route('/cub/<int:numOne>')
def cub(numOne):
    return str(numOne * numOne * numOne)

@app.route('/person')
def person():
    return render_template('persons.html')

@app.route('/personDetails')
def personDetails():
    personDetails = [
        {
            "Salutation" : "Ms",
            "Name" : "Geetha", 
            "Occupation" : "Software Developer",
            "Phonenumber" : 123456789
        },
        {
            "Salutation" : "Mr",
            "Name" : "Karan", 
            "Occupation" : "Team Lead",
            "Phonenumber" : 123456789
        },
        {
            "Salutation" : "Mrs",
            "Name" : "Kayal", 
            "Occupation" : "Manager",
            "Phonenumber" : 123456789
        }
    ]
    return personDetails

app.run()