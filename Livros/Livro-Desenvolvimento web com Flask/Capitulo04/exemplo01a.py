# Program: exemplo01a.py
# Author: Ramon R. Valeriano
# Description: Fazendos os programas do Capítulo 04, do nível 01
# Developed: 09/03/2020 - 10:29

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('userInicial.html', name=name)

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erro_servidor(e):
    return render_template('500.html'), 500

app.run(debug=True)