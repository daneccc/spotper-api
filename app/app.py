import config

from flask import Flask
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

import routes

app.run(port=5000)