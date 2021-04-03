from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

@app.route('/faixa') # OK
def getTracks():
    cursor.execute("SELECT * from Faixas")
    faixas = []
    for row in cursor.fetchall():
        faixas.append({'id':row[0],
                    'id_faixa_album': row[1], 
                    'nome':row[2], 
                    'duracao':(str(row[3])), 
                    'descricao':row[4],
                    'tipo_gravacao':row[5],
                    'album':row[6],
                    'tipo_composicao':row[7]})
    return jsonify(faixas)

@app.route('/faixa/<int:id>') # OK
def getTrack(id):
    query = "SELECT * FROM Faixas WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                'id_faixa_album': row[1], 
                'nome':row[2], 
                'duracao':row[3], 
                'descricao':row[4],
                'tipo_gravacao':row[5],
                'album':row[6],
                'tipo_duracao':row[7]}
    return {'message':'Faixa não encontrade'}, 404