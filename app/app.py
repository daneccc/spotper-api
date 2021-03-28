import config

from flask import Flask
app = Flask(__name__)

import routes

app.run(port=5000)