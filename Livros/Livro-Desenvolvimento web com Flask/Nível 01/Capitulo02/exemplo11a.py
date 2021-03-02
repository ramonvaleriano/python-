# Program: exemplo11a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 12:45

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('https://www.linkedin.com/in/ramon-r-valeriano-/')

app.run(debug=True)