# Program: exemplo07a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 03/03/2020 - 10:38

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/user/<name>')
def get_user(name):
    return render_template('user2.html', name=name)

app.run()