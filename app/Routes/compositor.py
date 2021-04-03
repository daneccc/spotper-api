from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

######### COMPOSITOR ########

@app.route('/compositor') # OK
def getCompositores(): 
    cursor.execute("SELECT * from Compositor")
    compositores = []
    for row in cursor.fetchall():
        compositores.append({'id':row[0],
                            'nome': row[1], 
                            'cidade_natal':row[2],
                            'pais_natal': row[3],
                            'data_nasc': row[4],
                            'data_morte': row[5],
                            'periodo_musical': row[6]})
    return jsonify(compositores)


@app.route('/compositor/<int:id>') # OK
def getCompositor(id):
    query = "SELECT * FROM Compositor WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                'nome': row[1], 
                'cidade_natal':row[2],
                'pais_natal': row[3],
                'data_nasc': row[4],
                'data_morte': row[5],
                'periodo_musical': row[6]}
    return {'message':'Composição não encontrade'}, 404