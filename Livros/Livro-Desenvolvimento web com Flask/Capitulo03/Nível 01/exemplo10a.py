# Program: exemplo10a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 3, para melhorar a fixação
# Developed: 04/03/2020 - 15:55

from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def erro_servidor_interno(e):
    return render_template('500.html'), 500


