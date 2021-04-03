from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app


@app.route('/interprete')
def getInterpretes():
    cursor.execute("SELECT * from Interprete")
    interpretes = []
    for row in cursor.fetchall():
        interpretes.append({'id':row[0],
                            'nome': row[1], 
                            'tipo':row[2]})
    return jsonify(interpretes)


@app.route('/interprete/<int:id>')
def getInterprete(id):
    query = "SELECT * FROM Interprete WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                'nome': row[1], 
                'tipo':row[2]}
    return {'message':'Composição não encontrade'}, 404
