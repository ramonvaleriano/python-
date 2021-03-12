# Program: exemplo4_5.py
# Author: Ramon R. Valeriano
# Description: Desenvolvendo os códigos do Cápitulo 4, nível 02
# Developed: 12/03/2020 - 14:15

from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'quasela'

bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Submeter')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect('index')
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    render_template('user.html', name=name)


@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erro_servidor(e):
    return render_template('500.html'), 500