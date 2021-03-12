# Program: exemplo1a.py
# Author: Ramon R. Valeriano
# Description: Desenvolvendo os códigos do Cápitulo 4, nível 02
# Developed: 12/03/2020 - 13:57

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testequalquer'

bootstrap = Bootstrap(app)

app.run()