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
    query = """SELECT a.nome, COUNT(f.album) as 'Músicas no album',
               convert(char(8),dateadd(second,SUM ( DATEPART(hh,(convert(datetime,f.duracao,1))) * 3600 +
               DATEPART(mi, (convert(datetime,f.duracao,1))) * 60 + DATEPART(ss,(convert(datetime,f.duracao,1)))),0),108)
               FROM Album as a
               INNER JOIN Faixas as f
               ON a.cod = f.album 
               GROUP BY a.cod,a.nome
               HAVING a.cod = ?
            """
    row = cursor.execute(query, id).fetchone()
    if row:
        return {
                    'nome' : row[0],
                    'num_musicas' : row[1],
                    'tempo_total' : row[2]
                }

    return {'message':'Álbum não encontrade'}, 404