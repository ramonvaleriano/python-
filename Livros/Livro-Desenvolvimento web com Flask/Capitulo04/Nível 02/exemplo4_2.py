# Program: exemplo4_2.py
# Author: Ramon R. Valeriano
# Description: Desenvolvendo os códigos do Cápitulo 4, nível 02
# Developed: 12/03/2020 - 12:22

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Nivel02Capitulo04'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NomeForm(FlaskForm):
    name = StringField('Qual é o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Subimeter')

@app.route('/')
def index():
    form = NomeForm()
    return render_template('indexInicial1.html', current_time=datetime.utcnow(), form=form)

app.run(debug=True)
