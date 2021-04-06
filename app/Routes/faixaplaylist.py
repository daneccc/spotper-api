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
                            'id_faixa':faixa[0],
                            'id_playlist': faixa[1],
                            'n_faixa_tocada': faixa[2],
                            'data_faixa_tocada': faixa[3],
                            'tempo_total_execucao': faixa[4]
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
                            'id_faixa': faixa[0],
                            'id_playlist':faixa[1],
                            'n_faixa_tocada': faixa[2],
                            'data_faixa_tocada': faixa[3],
                            
                        }

    return {'message':'Erro ao procurar por Faixa ligada a Playlist'}, 404
                    
@app.route('/faixaplaylist/<int:id_Playlist>') 
def getFaixasByPlaylist(id_Playlist):

    query =  """SELECT FaixasPlaylistAux.id_playlist,FaixasPlaylistAux.id_faixa,FaixasPlaylistAux.n_faixa_tocada,FaixasPlaylistAux.data_faixa_tocada,Faixas.nome,Composicao.nome,Compositor.nome,Interprete.nome,Album.nome,Faixas.duracao FROM FaixasPlaylistAux,Faixas,FaixasCompositorAux,Composicao,Compositor,FaixasInterpreteAux,Interprete,Album 
                WHERE FaixasPlaylistAux.id_faixa = Faixas.id 
                AND FaixasCompositorAux.id_faixa = Faixas.id
                AND Composicao.id = Faixas.tipo_composicao
                AND Compositor.id = FaixasCompositorAux.id_compositor
                AND FaixasInterpreteAux.id_faixa = Faixas.id
                AND FaixasInterpreteAux.id_interprete = Interprete.id
                AND Faixas.album = Album.cod
                AND id_playlist=?
                GROUP BY FaixasPlaylistAux.id_playlist,FaixasPlaylistAux.id_faixa,FaixasPlaylistAux.n_faixa_tocada,FaixasPlaylistAux.data_faixa_tocada,Faixas.nome,Composicao.nome,Compositor.nome,Interprete.nome,Album.nome,Composicao.nome,Faixas.duracao
                ORDER BY FaixasPlaylistAux.id_faixa"""
    row = cursor.execute(query, id_Playlist).fetchall()
    
    if (not row):
        return {'message':'Erro ao procurar por Faixa ligada a Playlist'}, 404
    faixas = []
    for faixa in row:
        faixas.append({   
                            'id_faixa':faixa[0],
                            'id_playlist': faixa[1],
                            'n_faixa_tocada': faixa[2],
                            'data_faixa_tocada': faixa[3],
                            'nome_musica':faixa[4],
                            'nome_composicao':faixa[5],
                            'nome_compositor':faixa[6],
                            'nome_interprete':faixa[7],
                            'nome_album':faixa[8],
                            'duracao_musica':(str(faixa[9]))
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

