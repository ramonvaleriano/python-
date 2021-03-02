# Program: exemplo09a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 16:37

from flask import Flask, abort

app = Flask(__name__)

@app.route('/user/<id>')
def get_user():
    user = load_user(id)
    if not user:
        abort(404)
    return f'<h1>Olá {user}</h1>'

app.run()