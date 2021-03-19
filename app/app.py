from config import SERVER, DATABASE, USER, PASSWORD
from flask import Flask, jsonify, request, render_template
import pyodbc
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'user'


cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER+';PWD='+ PASSWORD)
cursor = cnxn.cursor()
print("Conectado ao Banco de dados. kkkk")

jwt = JWT(app, authenticate, identity)  # /auth

@app.route('/')  ## mudar depois
def home():
    return render_template('index.html')


# POST /playlist data: {name:}
@app.route('/playlist', methods=['POST'])
def createPlaylist():
    data = request.get_json()
    playlist = {'nome': data['nome'], 
                'descricao': data['descricao']}

    query = "INSERT INTO Playlist (nome, descricao) VALUES (?, ?)"
    cursor.execute(query, playlist['nome'], playlist['descricao'])
    cnxn.commit()

    return playlist, 201
    

# GET /playlist/<int:id>
@app.route('/playlist/<int:id>')
@jwt_required()
def getPlaylist(id):
    query = "SELECT * from Playlist where PLAYLIST_ID=?"
    row = cursor.execute(query, id).fetchone()
    if row:
        return {'nome': row[0], 
                'descricao':row[1], 
                'PLAYLIST_ID':row[2], 
                'data_criacao':row[3], 
                'tempo_duracao':row[4]}
    return {'message': 'Playlist não encontrada'}, 404


# GET /playlist
@app.route('/playlist')
def getPlaylists():
    cursor.execute("SELECT * from Playlist")
    playlists = []
    for row in cursor.fetchall():
        playlists.append({'nome': row[0], 
                        'descricao':row[1], 
                        'PLAYLIST_ID':row[2], 
                        'data_criacao':row[3], 
                        'tempo_duracao':row[4]})
    return jsonify(playlists)


# DELETE /playlist/<int:id>/delete
@app.route('/playlist/<int:id>', methods=['DELETE'])
def deletePlaylist(id):
    query = "DELETE FROM Playlist WHERE PLAYLIST_ID=?"
    cursor.execute(query, id)
    cnxn.commit()

    return {'message':'Playlist deletada'}


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
                        'preco_compra':row[5], 
                        'tipo_compra':row[6], 
                        'cod_gravadora':row[7]})
    return jsonify(albums)


# ta dando o erro  no getAlbum, getAlbums, getTrack 
# TypeError: Object of type Decimal is not JSON serializable
# TypeError: Object of type time is not JSON serializable
# por causa do preco_compra 


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


# GET /track/<int:id>
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
    return {'message':'Álbum não encontrado'}, 404

# POST play track





"""
# POST /playlist/<string:name>/songs {name:, time:}
@app.route('/playlist/<string:name>/songs', methods=['POST'])
def createSongsInPlaylist(name):
    requestData = request.get_json()
    for playlist in playlists:
        if playlist['name'] == name:
            newSongs = {
                'name': requestData['name'],
                'artist': requestData['artist'],
                'time': requestData['time']
            }
            playlist['songs'].append(newSongs)
            return jsonify(newSongs)
    return jsonify({'message': 'playlist not found'})


# GET /playlist/<string:name>/songs
@app.route('/playlist/<string:name>/songs')
def getSongsInPlaylist(name):
    for playlist in playlists:
        if playlist['name'] == name:
            return jsonify({'songs': playlist['songs']})
    return jsonify({'message':'songs not found'})

"""


app.run(port=5000)