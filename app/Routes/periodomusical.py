
from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

########## PERIODO MUSICAL #########

@app.route('/periodo') # OK
def getPeriodos():
    cursor.execute("SELECT * from PeriodoMusical")
    periodos = []
    for row in cursor.fetchall():
        periodos.append({'id':row[0], 
                        'descricao':row[1],
                        'tempo_atividade': row[2]})
    return jsonify(periodos)


@app.route('/periodo/<int:id>') # OK
def getPeriodo(id):
    query = "SELECT * FROM PeriodoMusical WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0], 
                'descricao':row[1],
                'tempo_atividade': row[2]}
    return {'message':'Periodo Musical não encontrade'}, 404