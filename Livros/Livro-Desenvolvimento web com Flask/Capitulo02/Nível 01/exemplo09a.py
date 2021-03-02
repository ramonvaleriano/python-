# Program: exemplo09a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 12:38

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Resposta ruim!</h1>', 400

app.run(debug=True)