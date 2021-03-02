# Program: exemplo02a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 14:58

from flask import Flask

app = Flask(__name__)

def index():
    return '<h1>Olá mundo por uma outra vez!</h1>'


app.add_url_rule('/','index', index)

app.run()