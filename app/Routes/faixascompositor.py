from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

@app.route('/faixacompositor') 
def getFaixaCompositores():
    cursor.execute("SELECT * from FaixasCompositorAux")
    faixacompositores = []
    for row in cursor.fetchall():
        faixacompositores.append({'id_compositor':row[0],
                                'id_faixa': row[1]})
    return jsonify(faixacompositores)

@app.route('/faixacompositor/<int:id>') 
def getFaixaCompositor(id):
    query = "SELECT * FROM FaixasCompositorAux WHERE id_faixa=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id_compositor':row[0],
                'id_faixa': row[1]}
    return {'message':'Faixa - compositor não encontrade'}, 404