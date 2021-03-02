# Program: exemplo05a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 11:55

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Your Browser is {user_agent}</p>'

app.run(debug=True)