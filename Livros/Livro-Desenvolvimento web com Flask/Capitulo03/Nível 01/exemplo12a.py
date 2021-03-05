# Program: exemplo12a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 05/03/2020 - 09:22

from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base2.html')

app.run(debug=True)