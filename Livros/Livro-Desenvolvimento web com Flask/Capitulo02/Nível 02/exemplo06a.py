# Program: exemplo06a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 16:25

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Requisição ruim!</h1>', 400

app.run()