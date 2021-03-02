# Program: exemplo08a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 16:33

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.linkedin.com/in/ramon-r-valeriano-/')

app.run()