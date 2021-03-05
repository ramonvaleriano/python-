# Program: exemplo13a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 05/03/2020 - 19:33

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('hellonew.html')

@app.route('/user/<name>')
def usuario(name):
    return render_template('user3.html', name=name)

@app.errorhandler(404)
def paginaNaoEncontrada(e):
    return render_template('404.html')

@app.errorhandler(500)
def erroNoServidor(e):
    return render_template('500.html')

app.run(debug=True)