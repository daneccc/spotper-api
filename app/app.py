from config import SERVER, DATABASE, USER, PASSWORD
from flask import Flask, jsonify, request, render_template
import pyodbc

app = Flask(__name__)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER+';PWD='+ PASSWORD)
cursor = cnxn.cursor()
print("Conectado ao Banco de dados. kkkk")


@app.route('/')
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
@app.route('/playlist/<int:id>/delete', methods=['POST'])
def deletePlaylist(id):
    query = "DELETE FROM Playlist WHERE PLAYLIST_ID=?"
    cursor.execute(query, id)
    cnxn.commit()

    return {'message':'Playlist deletada'}

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