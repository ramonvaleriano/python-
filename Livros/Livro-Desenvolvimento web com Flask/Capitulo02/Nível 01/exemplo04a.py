# Program: exemplo04a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 10:13

from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    return f'<h1>Olá {name}, seja bem vindo!</h1>'

app.run(debug=True)
