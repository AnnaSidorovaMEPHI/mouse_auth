import os
import flask
import time
import json
import shutil
import random
import subprocess
import numpy as np
from hashlib import sha256
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from utils import load_json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
@cross_origin()
def get_features():
    cur_feature = np.array([]) 

    # parse request
    row_data = request.form.to_dict(flat=False)
    print(row_data.keys())    
    # print(row_data["dists_of_mouse"][0])


    # preparation of coordinates
    row_data["dists_of_mouse"] = json.loads(row_data["dists_of_mouse"][0])
    x_dists = []
    y_dists = []
    for timestamp in row_data["dists_of_mouse"].keys():
        x_dists.append(row_data["dists_of_mouse"][timestamp]["distanceX"])
        y_dists.append(row_data["dists_of_mouse"][timestamp]["distanceY"])
    if x_dists:
        print("x_coordinates_mean =",np.array(x_dists).mean())
    if y_dists:        
        print("y_coordinates_mean =",np.array(y_dists).mean())


    # preparation of speeds
    row_data["speeds_of_mouse"] = json.loads(row_data["speeds_of_mouse"][0])
    x_speeds = []
    y_speeds = []
    for timestamp in row_data["speeds_of_mouse"].keys():
        speed_x = row_data["speeds_of_mouse"][timestamp]["speedX"]
        speed_y = row_data["speeds_of_mouse"][timestamp]["speedY"]
        if speed_x:
            x_speeds.append(speed_x)
        if speed_y:
            y_speeds.append(speed_y)
    if x_speeds:
        print("x_speeds_mean=",np.array(x_speeds, dtype=float).mean())
    if y_speeds:        
        print("y_speeds_mean=",np.array(y_speeds, dtype=float).mean())   


    # preparation of accelerations
    row_data["accelerations_of_mouse"] = json.loads(row_data["accelerations_of_mouse"][0])
    x_accelerations = []
    y_accelerations = []
    for timestamp in row_data["accelerations_of_mouse"].keys():
        acceleration_x = row_data["accelerations_of_mouse"][timestamp]["accelerationX"]
        acceleration_y = row_data["accelerations_of_mouse"][timestamp]["accelerationY"]
        if acceleration_x:
            x_accelerations.append(acceleration_x)
        if acceleration_y:
            y_accelerations.append(acceleration_y)
    if x_accelerations:
        print("x_accelerations_mean =",np.array(x_accelerations).mean())
    if y_accelerations:        
        print("y_accelerations_mean =",np.array(y_accelerations).mean())   


    # preparation of angular characteristics
    # print(row_data["angular_characteristics"])
    row_data["angular_characteristics"] = json.loads(row_data["angular_characteristics"][0])
    cosines = []
    for timestamp in row_data["angular_characteristics"].keys():
        cos = row_data["angular_characteristics"][timestamp]["cosAngle"]
        if cos:
            cosines.append(cos)
    if cosines:
        print("cosines_mean =",np.array(cosines).mean())


    if row_data:
        return "True"    
    else:
        return "False"


if __name__ == "__main__":
    context = ('../frontend/server.crt', '../frontend/server.key')
    app.run('0.0.0.0', 5000, debug=True, ssl_context=context)