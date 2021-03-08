# Prgrama: exemplo3_3.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 09:39

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

app.run(debug=True)