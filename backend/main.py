import os
import flask
import time
import json
import shutil
import random
import requests
import subprocess
import numpy as np
from hashlib import sha256
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify
from flask_cors import CORS, cross_origin
from utils import load_json

app = Flask(__name__)
CORS(app)

CRITICAL_REQUESTS_COUNTER = {'count': 0}

# requests analisys

def update_request_statistic():
    CRITICAL_REQUESTS_COUNTER['count'] += 1
    return CRITICAL_REQUESTS_COUNTER['count']

def del_request_statistic():
    output = CRITICAL_REQUESTS_COUNTER['count']
    CRITICAL_REQUESTS_COUNTER['count'] = 0
    return output

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def get_features_from_screen():
    if request.method == "GET":
        if request.args and (request.args["data"]=="transaction" or request.args["data"]=="document"):
            update_request_statistic()
        return "True"
    elif request.method == "POST":
        feature_vector = np.array([])

        # parse request
        row_data = request.form.to_dict(flat=False)
        print(row_data.keys())    


        # preparation of coordinates
        row_data["dists_of_mouse"] = json.loads(row_data["dists_of_mouse"][0])
        x_dists = []
        y_dists = []
        for timestamp in row_data["dists_of_mouse"].keys():
            x_dists.append(row_data["dists_of_mouse"][timestamp]["distanceX"])
            y_dists.append(row_data["dists_of_mouse"][timestamp]["distanceY"])
        if x_dists:
            x_dists_mean = np.array(x_dists).mean()
        else:
            x_dists_mean = 0 
        print("x_coordinates_mean =", x_dists_mean)
        feature_vector = np.append(feature_vector, x_dists_mean)
        if y_dists:
            y_dists_mean = np.array(y_dists).mean()
        else:
            y_dists_mean = 0
        print("y_coordinates_mean =", y_dists_mean)
        feature_vector = np.append(feature_vector, y_dists_mean)


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
            x_speeds_mean = np.array(x_speeds, dtype=float).mean()
        else:
            x_speeds_mean = 0
        print("x_speeds_mean=", x_speeds_mean)
        feature_vector = np.append(feature_vector, x_speeds_mean)
        if y_speeds:
            y_speeds_mean = np.array(y_speeds, dtype=float).mean()    
        else:
            y_speeds_mean = 0
        print("y_speeds_mean=", y_speeds_mean)   
        feature_vector = np.append(feature_vector, y_speeds_mean)


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
            x_accelerations_mean = np.array(x_accelerations).mean()
        else:
            x_accelerations_mean = 0
        print("x_accelerations_mean =", x_accelerations_mean)
        feature_vector = np.append(feature_vector, x_accelerations_mean)
        if y_accelerations:        
            y_accelerations_mean = np.array(y_accelerations).mean()
        else:
            y_accelerations_mean = 0
        print("y_accelerations_mean =", y_accelerations_mean) 
        feature_vector = np.append(feature_vector, y_accelerations_mean)  


        # preparation of angular characteristics
        row_data["angular_characteristics"] = json.loads(row_data["angular_characteristics"][0])
        cosines = []
        for timestamp in row_data["angular_characteristics"].keys():
            cos = row_data["angular_characteristics"][timestamp]["cosAngle"]
            if cos:
                cosines.append(cos)
        if cosines:
            cos_mean = np.array(cosines).mean()
        else:
            cos_mean = 1
        print("cosines_mean =", cos_mean)
        feature_vector = np.append(feature_vector, cos_mean)  

        # preparation of curvature_distances
        row_data["curvature_distances"] = json.loads(row_data["curvature_distances"][0])
        cur_distances = []
        for timestamp in row_data["curvature_distances"].keys():
            cur_dis = row_data["curvature_distances"][timestamp]["curDis"]
            if cur_dis:
                cur_distances.append(cur_dis)
        if cur_distances:
            cur_distances_mean = np.array(cur_distances).mean()
            print("curvature_distances_mean =", cur_distances_mean)
            feature_vector = np.append(feature_vector, cur_distances_mean)

        # print(row_data["on_critical_area"])
        row_data["on_critical_area"] = json.loads(row_data["on_critical_area"][0]).values()
        on_area = list(row_data["on_critical_area"]).count(True)
        all_points = len(list(row_data["on_critical_area"]))
        if all_points:
            print("critical_area_frequency =", on_area/all_points)
            feature_vector = np.append(feature_vector, on_area/all_points)


        # requests analisys
        crit_reqs = del_request_statistic()
        print("critical_requests_counter =", crit_reqs)
        feature_vector = np.append(feature_vector, crit_reqs)

        print(feature_vector)


        if row_data:
            return "True"    
        else:
            return "False"




if __name__ == "__main__":
    context = ('../frontend/server.crt', '../frontend/server.key')
    app.run('0.0.0.0', 5000, debug=True, ssl_context=context)