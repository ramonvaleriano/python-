# Program: exemplo09a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 04/03/2020 - 15:49

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base1.html')

app.run()