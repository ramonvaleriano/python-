# Program: helloword.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 15:03

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá mundo, agora, acredito ques seja o ultimo.</h1>'

app.run()