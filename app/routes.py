from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app


@app.route('/')  # TODO: mudar depois
def home():
    return render_template('index.html')

##### PLAYLIST #####

@app.route('/playlist') # TODO retornar quantidade de musicas na playlist
def getPlaylists():
    cursor.execute("SELECT * from Playlist")
    playlists = []                      
    for row in cursor.fetchall():
        playlists.append({
            'id':  row[0],
            'nome': row[1],
            'descricao': row[2],
            'data_criacao': row[3]
        })
    return jsonify(playlists)


@app.route('/playlist/<int:id>')  # TODO duracao de todas as musicas da playlist 
def getPlaylist(id):
    query = "SELECT * from Playlist where id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':  row[0],
                'nome': row[1],
                'descricao': row[2],
                'data_criacao': row[3]}
    return {'message': 'Playlist não encontrade'}, 404


@app.route('/playlist', methods=['POST']) # OK
def createPlaylist():
    data = request.get_json()
    playlist = {'nome': data['nome'], 
                'descricao': data['descricao']}
    query = "INSERT INTO Playlist (nome, descricao, data_criacao) VALUES (?, ?, SYSDATETIME())"
    cursor.execute(query, playlist['nome'], playlist['descricao'])
    cnxn.commit()
    return playlist, 201


@app.route('/playlist/<int:id>', methods=['DELETE']) # OK
def deletePlaylist(id):
    query = "DELETE FROM Playlist WHERE id=?"
    cursor.execute(query, id)
    cnxn.commit()

    return {'message':'Playlist deletade'}


######## ALBUM ########

# GET /album
@app.route('/album') # OK
def getAlbums():
    cursor.execute("SELECT * from Album")
    albums = []
    for row in cursor.fetchall():
        albums.append({'cod':row[0],
                        'nome': row[1],
                        'data_gravacao':row[2], 
                        'data_compra':row[3], 
                        'preco_compra':(float(row[4])), 
                        'tipo_compra':row[5], 
                        'cod_gravadora':row[6]})
    return jsonify(albums)


@app.route('/album/<int:id>') # OK
def getAlbum(id):
    query = "SELECT * FROM Album WHERE cod=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'cod':row[0],
                    'nome': row[1], 
                    'data_gravacao':row[2], 
                    'data_compra':row[3], 
                    'preco_compra':(float(row[4])), 
                    'tipo_compra':row[5], 
                    'cod_gravadora':row[6]}
    return {'message':'Álbum não encontrade'}, 404


###### GRAVADORA #######

@app.route('/gravadora') # ok
def getGravadoras():
    cursor.execute("SELECT * from Gravadora")
    gravadoras = []
    for row in cursor.fetchall():
        gravadoras.append({'id':row[0],
                        'nome': row[1], 
                        'endereco':row[2], 
                        'telefone':row[3], 
                        'site':row[4]})
    return jsonify(gravadoras)


@app.route('/gravadora/<int:id>') # OK
def getGravadora(id):
    query = "SELECT * FROM Gravadora WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                    'nome': row[1], 
                    'endereco':row[2], 
                    'telefone':row[3], 
                    'site':row[4]}
    return {'message':'Gravadora não encontrade'}, 404


########## FAIXA #############

@app.route('/faixa') # OK
def getTracks():
    cursor.execute("SELECT * from Faixas")
    faixas = []
    for row in cursor.fetchall():
        faixas.append({'id':row[0],
                    'id_faixa_album': row[1], 
                    'nome':row[2], 
                    'duracao':(str(row[3])), 
                    'descricao':row[4],
                    'tipo_gravacao':row[5],
                    'album':row[6],
                    'tipo_composicao':row[7]})
    return jsonify(faixas)


@app.route('/faixa/<int:id>') # OK
def getTrack(id):
    query = "SELECT * FROM Faixas WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                'id_faixa_album': row[1], 
                'nome':row[2], 
                'duracao':row[3], 
                'descricao':row[4],
                'tipo_gravacao':row[5],
                'album':row[6],
                'tipo_duracao':row[7]}
    return {'message':'Faixa não encontrade'}, 404

######### INTERPRETE ##########

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


####### COMPOSICAO ########

@app.route('/composicao') # OK
def getComposicoes(): 
    cursor.execute("SELECT * from Composicao")
    composicoes = []
    for row in cursor.fetchall():
        composicoes.append({'id':row[0],
                            'nome': row[1], 
                            'descricao':row[2]})
    return jsonify(composicoes)

@app.route('/composicao/<int:id>') # OK
def getComposicao(id): 
    query = "SELECT * FROM Composicao WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                        'nome': row[1], 
                        'descricao':row[2]}
    return {'message':'Composição não encontrade'}, 404


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


######### COMPOSITOR ########

@app.route('/compositor') # OK
def getCompositores(): 
    cursor.execute("SELECT * from Compositor")
    compositores = []
    for row in cursor.fetchall():
        compositores.append({'id':row[0],
                            'nome': row[1], 
                            'cidade_natal':row[2],
                            'pais_natal': row[3],
                            'data_nasc': row[4],
                            'data_morte': row[5],
                            'periodo_musical': row[6]})
    return jsonify(compositores)


@app.route('/compositor/<int:id>') # OK
def getCompositor(id):
    query = "SELECT * FROM Compositor WHERE id=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id':row[0],
                'nome': row[1], 
                'cidade_natal':row[2],
                'pais_natal': row[3],
                'data_nasc': row[4],
                'data_morte': row[5],
                'periodo_musical': row[6]}
    return {'message':'Composição não encontrade'}, 404


# FAIXAS-COMPOSITOR-AUX

@app.route('/faixacompositor') # OK
def getFaixaCompositores():
    cursor.execute("SELECT * from FaixasCompositorAux")
    faixacompositores = []
    for row in cursor.fetchall():
        faixacompositores.append({'id_compositor':row[0],
                                'id_faixa': row[1]})
    return jsonify(faixacompositores)


@app.route('/faixacompositor/<int:id>') # OBSERVACAO QUAL O ID ESCOLHER
def getFaixaCompositor(id):
    query = "SELECT * FROM FaixasCompositorAux WHERE id_faixa=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id_compositor':row[0],
                'id_faixa': row[1]}
    return {'message':'Faixa - compositor não encontrade'}, 404


# FAIXAS-INTERPRETE-AUX

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


# FAIXA-PLAYLIST-AUX ****

# TODO: GET: /faixaplaylist
@app.route('/faixaplaylist')
def getFaixaPlaylists():
    return

# TODO: GET /faixaplaylist/<int:id>
@app.route('/faixaplaylist/<int:id>') # NAO TA FUNCIONANDO - OBS VER A QUESTAO DO ID COMPOSTO AQUI TB
def getFaixaPlaylist(id):
    query = "SELECT * FROM FaixasPlaylistAux WHERE id_faixa=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'id_faixa':row[0],
                'id_playlist': row[1],
                'n_faixa_tocada': row[2],
                'data_faixa_tocada': row[3],
                'tempo_total_playlist': row[4]}
    return {'message':'Faixa - playlist não encontrade'}, 404


## PROVAVELMENTE SERÃO NECESSARIOS NA MANUTENÇÃO DAS PLAYLISTS:

# TODO: POST /faixaplaylist/<int:id>
@app.route('/faixaplaylist/<int:id>', methods=['POST'])
def postFaixaPlaylist(id_faixa, id_playlist):
    return

# TODO: DELETE /faixaplaylist/<int:id>
@app.route('/faixaplaylist/<int:id>', methods=['DELETE'])
def deleteFaixaPlaylist(id_faixa, id_playlist):
    return