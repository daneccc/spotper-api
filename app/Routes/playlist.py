from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

@app.route('/playlist') 
def getPlaylists():
    cursor.execute("""
    SELECT p.id,p.nome,p.descricao,p.data_criacao, COUNT(fp.id_faixa),convert(char(8),dateadd(second,SUM ( DATEPART(hh,(convert(datetime,f.duracao,1))) * 3600 +
    DATEPART(mi, (convert(datetime,f.duracao,1))) * 60 + DATEPART(ss,(convert(datetime,f.duracao,1)))),0),108)
    FROM FaixasPlaylistAux as fp
    INNER JOIN Playlist as p 
    ON fp.id_playlist = p.id
    INNER JOIN Faixas as f
    ON fp.id_faixa = f.id
    GROUP BY p.id,p.nome,p.descricao,p.data_criacao,fp.id_playlist
    """)
    playlists = []                      
    for row in cursor.fetchall():
        playlists.append({
            'id':  row[0],
            'nome': row[1],
            'descricao': row[2],
            'data_criacao': row[3],
            'num_musicas':row[4],
            'tempo_total':row[5]
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