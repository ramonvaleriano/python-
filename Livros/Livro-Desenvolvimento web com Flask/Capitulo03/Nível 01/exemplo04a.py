# Program: exemplo04a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 03/03/2020 - 09:15

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def get_user(name):
    mame = name.title()
    return render_template('userInicial.html', name=name)

app.run()