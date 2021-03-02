# Program: exemplo05a.py
# Author: Ramon R. Valeriano
# Description: Programa do Capítulo 2, para melhorar a fixação
# Developed: 02/03/2020 - 16:05

from flask import current_app
from helloword import app

current_app.name

app_ctx = app.app_context()
app_ctx.push()
current_app.name
app_ctx.pop()

app.run()