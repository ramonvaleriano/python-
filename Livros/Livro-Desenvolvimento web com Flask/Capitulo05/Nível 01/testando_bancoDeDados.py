# Program: testando_bancoDeDados.py
# Author: Ramon R. Valeriano
# Description: Testando o banco de dados.
# Developed: 19/03/2020 - 11:06

from exemplo01a import db, app

db.create_all()
app.run()

