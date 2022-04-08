from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


data = {"data":"Hello, World"}
#endpoint # 1
@app.route('/endpoint1', methods = ['GET', 'POST'])
def endpoint1():
    if(request.method == 'GET'):    
        return data 


#endpoint # 2
@app.route('/endpoint2', methods = ['GET', 'POST'])
def endpoint2():
    if(request.method == 'GET'):
       r =  requests.get("https://api.zippopotam.us/us/90211")
       return r.json()



  