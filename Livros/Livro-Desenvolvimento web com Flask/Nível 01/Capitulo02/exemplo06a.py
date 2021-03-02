# Program: exemplo06a.py
# Author: Ramon R. Valeriano
# Description: Primeiro exemplo de uma aplicação web
# Developed: 02/03/2020 - 12:07

from exemplo2_1 import app

from flask import current_app

current_app.name

app_ctx = app.app_context()
app_ctx.push()

app_ctx.pop()