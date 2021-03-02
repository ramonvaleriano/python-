# Program: exemplo12a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 12:49

from flask import Flask, abort

app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return f'<h1>Olá {user}</h1>'

app.run()