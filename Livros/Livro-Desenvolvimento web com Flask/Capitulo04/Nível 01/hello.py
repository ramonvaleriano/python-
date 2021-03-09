# Program: hello.py
# Author: Ramon R. Valeriano
# Description: Refazendo a função principal a ser usada no livro
# Developed: 09/03/2021 - 15:49

from flask import Flask, session, flash, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'olamundo'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Qual o seu nome?', validators=[DataRequired()])
    submit = SubmitField('Confirmar')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Verique se realmente é esse o seu nome')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    render_template('404.html'), 404

@app.errorhandler(500)
def erro_servidor(e):
    render_template('500.html'), 500

app.run(debug=True)






