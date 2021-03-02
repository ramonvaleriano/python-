# Program: exemplo04a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 15:50

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Seu Browser é {user_agent}</p>'

app.run()