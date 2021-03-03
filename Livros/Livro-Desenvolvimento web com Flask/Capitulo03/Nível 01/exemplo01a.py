# Program: exemplo01a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 03/03/2020 - 08:59

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá mundo!</h1>'

app.run()