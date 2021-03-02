# Program: hellodinamico.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 15:17

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá mundo, pela 872803752895 vez!</h1>'

@app.route('/user/<name>')
def get_user(name):
    name = name.title()
    return f'<h1>Olá {name}, bem vindo novamente, ao mundo de Flask</h1>'

app.run(debug=True)