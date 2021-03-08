# Prgrama: exemplo4a.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 10:39

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('derivadobase.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

app.run(debug=True)