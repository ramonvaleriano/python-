# Program: exemplo07a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 16:29

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>Este documento esta sendo carregado em um cookie.</h1>')
    response.set_cookie('answer', '42')
    return response

app.run()