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
                    'descricao':row[3],
                    'tipo_gravacao':row[4],
                    'album':row[5],
                    'tipo_composicao':row[6],
                    'duracao':(str(row[7]))})
    return jsonify(faixas)

@app.route('/faixa/<int:id>') # OK
def getTrack(id):
    query = "SELECT * FROM Faixas WHERE album=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        print(row)
        return {'id':row[0],
                'id_faixa_album': row[1], 
                'nome':row[2], 
                'descricao':row[3],
                'tipo_gravacao':row[4],
                'album':row[5],
                'tipo_composicao':row[6],
                'duracao':(str(row[7]))}
    return {'message':'Faixa não encontrade'}, 404