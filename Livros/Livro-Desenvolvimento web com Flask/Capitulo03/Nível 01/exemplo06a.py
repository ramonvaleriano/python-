# Program: exemplo06a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 03/03/2020 - 10:18

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('derivadoDaBase.html')

app.run()