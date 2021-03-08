# Prgrama: exemplo3_1.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 09:24

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá, mundo. Olha nós de novo aqui!</h1>'

app.run()