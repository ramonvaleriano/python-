# Program: exemplo03a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 10:08

from flask import Flask

app = Flask(__name__)

def index():
    return '<h1>Olá mundo</h1>'

app.add_url_rule('/', 'index', index)

app.run(debug=True)