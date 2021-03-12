# Program: exemplo4_1.py
# Author: Ramon R. Valeriano
# Description: Desenvolvendo os códigos do Cápitulo 4, nível 02
# Developed: 12/03/2020 - 12:14

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nivel2capitulo4'

