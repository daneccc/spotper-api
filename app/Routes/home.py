from flask import Flask, jsonify, request, render_template
from db import cnxn, cursor
from __main__ import app

@app.route('/') 
def home():
    return render_template('index.html')

