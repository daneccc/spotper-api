from flask import Flask, jsonify, request, render_template  # pacotemetodo flask - classe Flask


app = Flask(__name__)

playlists = [
    {
        'name':'Playlist01',
        'songs': [
            {
                'name':'Rap do Gabriel Monteiro',
                'artist':'Pedro',
                'time':9
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


# POST /playlist data: {name:}
@app.route('/playlist', methods=['POST'])
def createPlaylist():
    requestData = request.get_json()
    newPlaylist = {
        'name': requestData['name'],
        'songs':[]
    }
    playlists.append(newPlaylist)
    return jsonify(newPlaylist)


# GET /playlist/<string:name>
@app.route('/playlist/<string:name>')
def getPlaylist(name):
    for playlist in playlists:
        if playlist['name'] == name:
            return jsonify(playlist)
    return jsonify({'message':'playlist not found'})


# GET /playlist
@app.route('/playlist')
def getPlaylists():
    return jsonify({'playlists': playlists})


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


app.run(port=5000)
