from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

####### COMPOSICAO ########

@app.route('/composicao') # OK
def getComposicoes(): 
    cursor.execute("SELECT * from Composicao")
    composicoes = []
    for row in cursor.fetchall():
        composicoes.append({'id':row[0],
                            'nome': row[1], 
                            'descricao':row[2]})
    return jsonify(composicoes)

@app.route('/composicao/<int:id>') # OK
def getComposicao(id): 
    query = "SELECT * FROM Composicao WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                        'nome': row[1], 
                        'descricao':row[2]}
    return {'message':'Composição não encontrade'}, 404