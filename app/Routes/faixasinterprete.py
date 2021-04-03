from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

# TODO: GET: /faixainterprete
@app.route('/faixainterprete')
def getFaixasInterpretes():
    cursor.execute("SELECT * from FaixasInterpreteAux")
    compositores = []
    for row in cursor.fetchall():
        compositores.append({'id_faixa':row[0],
                            'id_interprete': row[1]})
    return jsonify(compositores)

# TODO: GET /faixainterprete/<int:id>
@app.route('/faixainterprete/<int:id>')   # OBS COMO PASSAR O ID COMPOSTO
def getFaixasInterprete(id):
    query = "SELECT * FROM FaixasInterpreteAux WHERE id_faixa=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id_faixa':row[0],
                'id_interprete': row[1]}
    return {'message':'Faixa - compositor não encontrade'}, 404