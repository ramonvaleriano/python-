# Prgrama: exemplo2a.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 09:59

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('controle.html')

@app.route('/user/<name>')
def user(name):
    return render_template('controle.html', name=name)

app.run(debug=True)