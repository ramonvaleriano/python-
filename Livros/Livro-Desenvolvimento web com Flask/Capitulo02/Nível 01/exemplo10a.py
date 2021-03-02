# Program: exemplo10a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 12:42

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Esse documetno gera um cookie</h1>')
    response.set_cookie('answer', '42')
    return response

app.run()