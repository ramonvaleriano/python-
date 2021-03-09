# Program: exemplo01a.py
# Author: Ramon R. Valeriano
# Description: Fazendos os programas do Capítulo 04, do nível 01
# Developed: 09/03/2020 - 10:29

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', )