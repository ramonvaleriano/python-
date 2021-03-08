# Prgrama: exemplo3_2.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 09:27

from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    name = name.title()
    return f'<h1>Olá, {name}</h1>'

app.run(debug=True)