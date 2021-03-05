# Program: exemplo14a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 05/03/2020 - 20:05

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('hellonew1.html', current_time=datetime.utcnow())

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