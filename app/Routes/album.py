from flask import Flask, jsonify
from db import  cursor
from __main__ import app

@app.route('/album') 
def getAlbums():
    cursor.execute("SELECT * from Album")
    albums = []
    for row in cursor.fetchall():
        print(row)
        albums.append   (
                            {
                                'cod':row[0],
                                'nome': row[1],
                                'data_gravacao':row[2], 
                                'data_compra':row[3], 
                                'preco_compra':(float(row[4])), 
                                'tipo_compra':row[5], 
                                'cod_gravadora':row[6],
                
                            }
                        )
    return jsonify(albums)

@app.route('/album/<int:id>')
def getAlbum(id):
    query = "SELECT * FROM Album WHERE cod=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {
                    'cod':row[0],
                    'nome': row[1],
                    'data_gravacao':row[2], 
                    'data_compra':row[3], 
                    'preco_compra':(float(row[4])), 
                    'tipo_compra':row[5], 
                    'cod_gravadora':row[6]
                }

    return {'message':'Álbum não encontrade'}, 404