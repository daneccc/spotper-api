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
    data = []
    query = """SELECT Faixas.id,Faixas.id_faixa_album,Faixas.nome,Faixas.descricao,Faixas.tipo_gravacao,Faixas.album,Faixas.tipo_composicao,Faixas.duracao,Compositor.nome,Interprete.nome,Composicao.nome
    From Faixas, FaixasCompositorAux,Compositor, FaixasInterpreteAux,
    Interprete,Composicao
    WHERE Faixas.id = FaixasCompositorAux.id_faixa 
    AND FaixasCompositorAux.id_compositor = Compositor.id
    AND  FaixasInterpreteAux.id_faixa = Faixas.id 
    AND FaixasInterpreteAux.id_interprete = Interprete.id 
    AND Faixas.tipo_composicao = Composicao.id
    AND album=?
    GROUP BY Faixas.id,Faixas.id_faixa_album,Faixas.nome,Faixas.descricao,Faixas.tipo_gravacao,Faixas.album,Faixas.tipo_composicao,Faixas.duracao,Compositor.nome,Interprete.nome,Composicao.nome
    ORDER BY Faixas.id_faixa_album """
    
    rows = cursor.execute(query, id).fetchall()
    for row in rows:
        data.append({'id':row[0],
                'id_faixa_album': row[1], 
                'nome':row[2], 
                'descricao':row[3],
                'tipo_gravacao':row[4],
                'album':row[5],
                'tipo_composicao':row[6],
                'duracao':(str(row[7])),
                'nome_compositor':row[8],
                'nome_interprete':row[9],
                'nome_composicao':row[10]}
                )
    return jsonify(data)