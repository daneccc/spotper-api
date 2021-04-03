from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app


@app.route('/gravadora') # ok
def getGravadoras():
    cursor.execute("SELECT * from Gravadora")
    gravadoras = []
    for row in cursor.fetchall():
        gravadoras.append({'id':row[0],
                        'nome': row[1], 
                        'endereco':row[2], 
                        'telefone':row[3], 
                        'site':row[4]})
    return jsonify(gravadoras)

@app.route('/gravadora/<int:id>') # OK
def getGravadora(id):
    query = "SELECT * FROM Gravadora WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                    'nome': row[1], 
                    'endereco':row[2], 
                    'telefone':row[3], 
                    'site':row[4]}
    return {'message':'Gravadora não encontrade'}, 404