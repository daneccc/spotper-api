import config
from flask import Flask
app = Flask(__name__)

from Routes import album, composicao, compositor, faixaplaylist, faixas, faixascompositor, faixasinterprete, gravadora, interprete, periodomusical, playlist

app.run(port=5000)