# Program: exemplo03a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 15:03

from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def get_user(name):
    name = name.title()
    return f'<h1>Bem vindo ao mundo Flask {name}</h1>'

app.run(debug=True)