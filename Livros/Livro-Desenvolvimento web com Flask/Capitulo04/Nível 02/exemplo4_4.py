# Program: exemplo4_4.py
# Author: Ramon R. Valeriano
# Description: Desenvolvendo os códigos do Cápitulo 4, nível 02
# Developed: 12/03/2020 - 13:30

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'testandoaplicacao'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('Qual é seu nome?', validators=[DataRequired()])
    submit = SubmitField('Submeter')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

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