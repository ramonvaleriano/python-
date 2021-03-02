# Program: exemplo08a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 12:26

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(nome='Olá mundo!')

# Apenas para aprensentar o contexto de hooks
"""
@app.before_request

@app.before_first_request

@app.after_request

@app.teardown_request
"""