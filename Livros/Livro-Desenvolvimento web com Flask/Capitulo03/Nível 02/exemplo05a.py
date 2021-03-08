# Prgrama: exemplo05a.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 13:29

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erro_servidor(e):
    return render_template('500.html'), 500

app.run(debug=True)