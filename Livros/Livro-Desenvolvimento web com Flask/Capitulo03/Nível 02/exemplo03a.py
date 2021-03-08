# Prgrama: exemplo3a.py
# Author: Ramon R. Valeriano
# Description: Desensolvolvendo os Scripts do Nível 2 do Capitulo 3 do Livro.
# Developed: 08/03/2020 - 10:54

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('derivadobase.html')

app.run(debug=True)