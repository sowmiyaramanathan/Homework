from flask import Flask, render_template

app = Flask(__name__)

@app.route('/selectchoice')
def choice():
    return render_template('choice.html')

@app.route('/addproducts')
def add():
    return render_template('add.html')

app.run()