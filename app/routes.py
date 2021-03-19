from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

@app.route('/')  ## TODO: mudar depois
def home():
    return render_template('index.html')

# PLAYLIST

@app.route('/playlist')
def getPlaylists(self):
    cursor.execute("SELECT * from Playlist")
    playlists = []
    for row in cursor.fetchall():
        playlists.append({'nome': row[0], 
                        'descricao':row[1], 
                        'PLAYLIST_ID':row[2], 
                        'data_criacao':row[3], 
                        'tempo_duracao':row[4]})
    return jsonify(playlists)

@app.route('/playlist/<int:id>')    
def getPlaylist(self, id):
    query = "SELECT * from Playlist where PLAYLIST_ID=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'nome': row[0], 
                'descricao':row[1], 
                'PLAYLIST_ID':row[2], 
                'data_criacao':row[3], 
                'tempo_duracao':row[4]}
    return {'message': 'Playlist não encontrada'}, 404

@app.route('/playlist', methods=['POST'])
def createPlaylist(self, request):
    data = request.get_json()
    playlist = {'nome': data['nome'], 
                'descricao': data['descricao']}
    query = "INSERT INTO Playlist (nome, descricao) VALUES (?, ?)"
    cursor.execute(query, playlist['nome'], playlist['descricao'])
    cnxn.commit()

    return playlist, 201

@app.route('/playlist/<int:id>', methods=['DELETE'])
def deletePlaylist(self, id):
    query = "DELETE FROM Playlist WHERE PLAYLIST_ID=?"
    cursor.execute(query, id)
    cnxn.commit()

    return {'message':'Playlist deletada'}

# ALBUM

# GET /album
@app.route('/album')
def getAlbums():
    cursor.execute("SELECT * from Album")
    albums = []
    for row in cursor.fetchall():
        albums.append({'ALBUM_ID':row[0],
                        'nome': row[1], 
                        'descricao':row[2], 
                        'data_gravacao':row[3], 
                        'data_compra':row[4], 
                        'preco_compra':(float(row[5])), 
                        'tipo_compra':row[6], 
                        'cod_gravadora':row[7]})
    return jsonify(albums)

# GET /album/<int:id>
@app.route('/album/<int:id>')
def getAlbum(id):
    query = "SELECT * FROM Album WHERE ALBUM_ID=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'ALBUM_ID':row[0],
                    'nome': row[1], 
                    'descricao':row[2], 
                    'data_gravacao':row[3], 
                    'data_compra':row[4], 
                    'preco_compra':row[5], 
                    'tipo_compra':row[6], 
                    'cod_gravadora':row[7]}
    return {'message':'Álbum não encontrado'}, 404

# GRAVADORA

## TODO: GET /gravadora
@app.route('/gravadora')
def getGravadoras(id):
    cursor.execute("SELECT * from Gravadora")
    gravadoras = []
    for row in cursor.fetchall():
        gravadoras.append({'GRAVADORA_ID':row[0],
                        'endereco': row[1], 
                        'telefone':row[2], 
                        'site':row[3], 
                        'nome':row[4]
                        })
    return jsonify(gravadoras)

# GET /gravadora/<int:id>
@app.route('/gravadora/<int:id>')
def getGravadora(id):
    query = "SELECT * FROM Gravadora WHERE GRAVADORA_ID=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'GRAVADORA_ID':row[0],
                    'endereco': row[1], 
                    'telefone':row[2], 
                    'site':row[3], 
                    'nome':row[4]}
    return {'message':'Álbum não encontrado'}, 404

# FAIXA

# TODO: GET: /faixa
@app.route('/track')
def getTracks():
    return

# GET /faixa/<int:id>
@app.route('/track/<int:id>')
def getTrack(id):
    query = "SELECT * FROM Faixas WHERE FAIXA_ID=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'FAIXA_ID':row[0],
                    'album_id': row[1], 
                    'tipo_composicao':row[2], 
                    'numero_faixa':row[3], 
                    'nome':row[4],
                    'tempo_musical':row[5],
                    'descricao':row[6],
                    'tipo_gravacao':row[7],
                    'duracao':row[8]}

    return {'message':'Faixa não encontrada'}, 404

# INTERPRETE

# TODO: GET: /interprete
@app.route('/interprete')
def getInterpretes():
    return

# TODO: GET /composicao/<int:id>
@app.route('/interprete/<int:id>')
def getInterprete(id):
    return

# COMPOSICAO

# TODO: GET: /composicao
@app.route('/composicao')
def getComposicoes():
    return

# TODO: GET /composicao/<int:id>
@app.route('/composicao/<int:id>')
def getComposicao(id):
    return

# PERIODO MUSICAL

# TODO: GET: /periodo
@app.route('/periodo')
def getPeriodos():
    return

# TODO: GET /periodo/<int:id>
@app.route('/periodo/<int:id>')
def getPeriodo(id):
    return

# COMPOSITOR

# TODO: GET: /compositor
@app.route('/compositor')
def getCompositores():
    return

# TODO: GET /compositor/<int:id>
@app.route('/compositor/<int:id>')
def getCompositor(id):
    return


# FAIXAS-COMPOSITOR-AUX

# TODO: GET: /faixacompositor
@app.route('/faixacompositor')
def getFaixaCompositores():
    return

# TODO: GET /faixacompositor/<int:id>
@app.route('/faixacompositor/<int:id>')
def getFaixaCompositor(id):
    return


# FAIXAS-INTERPRETE-AUX

# TODO: GET: /faixainterprete
@app.route('/faixainterprete')
def getFaixasInterpretes():
    return

# TODO: GET /faixainterprete/<int:id>
@app.route('/faixainterprete/<int:id>')
def getFaixasInterprete(id_faixa, id_interprete):
    return


# FAIXA-PLAYLIST-AUX ****

# TODO: GET: /faixaplaylist
@app.route('/faixaplaylist')
def getFaixaPlaylists():
    return

# TODO: GET /faixaplaylist/<int:id>
@app.route('/faixaplaylist/<int:id>')
def getFaixaPlaylist(id_faixa, id_playlist):
    return


## PROVAVELMENTE SERÃO NECESSARIOS NA MANUTENÇÃO DAS PLAYLISTS:

# TODO: POST /faixaplaylist/<int:id>
@app.route('/faixaplaylist/<int:id>', methods=['POST'])
def postFaixaPlaylist(id_faixa, id_playlist):
    return

# TODO: DELETE /faixaplaylist/<int:id>
@app.route('/faixaplaylist/<int:id>', methods=['DELETE'])
def deleteFaixaPlaylist(id_faixa, id_playlist):
    return