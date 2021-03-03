# Program: exemplo02a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 03/03/2020 - 09:02

from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def index(name):
    name = title()
    return '<h1>Olá {{ name }}</h1>' # Não irá funcionar dessa forma.

app.run()