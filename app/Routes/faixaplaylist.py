from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

@app.route('/faixaplaylist') 
def getFaixasPlaylists():
    query = "SELECT * FROM FaixasPlaylistAux"
    row = cursor.execute(query).fetchall()
    
    if (not row):
        return {'message':'Erro ao procurar por Faixa ligada a Playlist'}, 404

    faixas = []
    for faixa in row:
        faixas.append({   
                            'id_playlist': faixa[0],
                            'id_faixa':faixa[1],
                            'n_faixa_tocada': faixa[2],
                            'data_faixa_tocada': faixa[3],
                        }
                    )

    return jsonify(faixas)

@app.route('/faixaplaylist/<int:id_Playlist>/<int:id_faixa>') 
def getFaixaByPlaylist(id_Playlist, id_faixa):
    query = "SELECT * FROM FaixasPlaylistAux WHERE id_playlist=?"
    row = cursor.execute(query, id_Playlist).fetchall()

    if (row):
        for faixa in row:
            if(faixa.id_faixa == id_faixa):
                return  {   
                            'id_playlist': faixa[0],
                            'id_faixa':faixa[1],
                            'n_faixa_tocada': faixa[2],
                            'data_faixa_tocada': faixa[3],
                        }

    return {'message':'Erro ao procurar por Faixa ligada a Playlist'}, 404
                    
@app.route('/faixaplaylist/<int:id_Playlist>') 
def getFaixasByPlaylist(id_Playlist):
    query = "SELECT * FROM FaixasPlaylistAux WHERE id_playlist=?"
    row = cursor.execute(query, id_Playlist).fetchall()
    
    if (not row):
        return {'message':'Erro ao procurar por Faixa ligada a Playlist'}, 404
    faixas = []
    for faixa in row:
        faixas.append({   
                            'id_playlist': faixa[0],
                            'id_faixa':faixa[1],
                            'n_faixa_tocada': faixa[2],
                            'data_faixa_tocada': faixa[3],
                        }
                    )

    return jsonify(faixas)

@app.route('/faixaplaylist/<int:id_Playlist>', methods=['POST'])
def postFaixaPlaylist():
    data = request.get_json()
    faixa = {   
                'id_faixa': data['id_faixa'], 
                'id_playlist': data['id_playlist'],
                'faixa_vezes_tocada': 0,
                'data_faixa_tocada': None
            }
    query = "INSERT INTO FaixasPlaylistAux (id_playlist, id_faixa, faixa_vezes_tocada, data_faixa_tocada) VALUES (?, ?, ?, ?)"
    cursor.execute(query, faixa['id_faixa'], faixa['id_playlist'], faixa['faixa_vezes_tocada'], faixa['data_faixa_tocada'])
    cnxn.commit()

    return jsonify(faixa)

@app.route('/faixaplaylist/<int:id_playlist>/<int:id_faixa>', methods=['DELETE'])
def deleteFaixaPlaylist(id_playlist, id_faixa):
    query = "DELETE FROM FaixasPlaylistAux WHERE id_playlist=? AND id_faixa = ?"
    cursor.execute(query, id_playlist, id_faixa)
    cnxn.commit()

    return {'message':'Faixa deletada da Playlist'}

