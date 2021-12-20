import os
import flask
import time
import json
import shutil
import random
import subprocess
from hashlib import sha256
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from utils import load_json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def get_data():
    # parse request
    row_data = request.form
    print(request.form)
    if row_data:
        features = json.dumps(row_data,indent=4)
        print(features)
        return "True"    
    else:
        return "False"


if __name__ == "__main__":
    context = ('../frontend/server.crt', '../frontend/server.key')
    app.run('0.0.0.0', 5000, debug=True, ssl_context=context)