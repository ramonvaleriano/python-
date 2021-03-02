# Program: exemplo2_1.py
# Author: Ramon R. Valeriano
# Description: Exemplos do livro
# Developed: 02/03/2020 - 10:20

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá Mundo, seja bem vindo!</h1>'

app.run(debug=True)