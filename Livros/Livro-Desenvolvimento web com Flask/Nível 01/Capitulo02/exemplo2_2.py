# Program: exemplo2_2.py
# Author: Ramon R. Valeriano
# Description: Exemplos do livro
# Developed: 02/03/2020 - 10:27

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá mundo!</h1>'

@app.route('/user/<name>/')
def user(name):
    return f'<h1>Olá {name}, seja bem vindo!</h1>'

app.run()