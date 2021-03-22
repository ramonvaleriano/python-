# Program: testes_bancodedados.py
# Author: Ramon R. Valeriano
# Description: Fazendo os testes necessários por aqui.
# Debeloped: 21/03/2020 - 12:53

import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRETY_KEY'] = 'testequalquer'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

admin_role = Role(name='Admin')
mod_role = Role(name='Moderador')
user_role = Role(name='User')

user_john = User(username='John', role=admin_role)
user_susan = User(username='Susan', role=user_role)
user_david = User(username='Davida', role=user_role)

db.session.add_all([admin_role, mod_role, user_role, user_john, user_david, user_david])
db.session.commit()

print(f'Id da Função Administrativo: {admin_role.id}')
print(f'O nome da Função: {admin_role.name}')
print(f'O id da função do Usuário Jhon: {user_john.role_id}')
print(f'O id da função da Usuária Susan: {user_susan.role_id}')

admin_role.name = 'Administrador'
db.session.add(admin_role)
db.session.commit()

print('\n\n')
print(f'Id da Função Administrativo: {admin_role.id}')
print(f'O nome da Função: {admin_role.name}')
print(f'O id da função do Usuário Jhon: {user_john.role_id}')
print(f'O id da função da Usuária Susan: {user_susan.role_id}')

print(Role.query.all())

db.session.delete(mod_role)
db.session.commit()

print('\n\n')
print(f'Id da Função Administrativo: {admin_role.id}')
print(f'O nome da Função: {admin_role.name}')
print(f'O id da função do Usuário Jhon: {user_john.role_id}')
print(f'O id da função da Usuária Susan: {user_susan.role_id}')

print('\n')
print(Role.query.all())
print(User.query.all())

print('\n')
print(User.query.filter_by(role=user_role).all())

user_david.username = 'David'
db.session.add(user_david)
db.session.commit()

print('\n')
print(User.query.filter_by(role=user_role).all())
print('\n')
print(str(User.query.filter_by(role=user_role)))

print('\n')
print(user_role.users.order_by(User.username).all())
print(f'Quantidade de Usuários: {user_role.users.count()}')