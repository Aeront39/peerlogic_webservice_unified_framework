from flask import Flask, render_template, request
import flask
import json
import requests
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# define custom error code
class UnsupportedModelException(HTTPException):
    code = 404
    description = "Error: the model you requested is not supported. Please check the spelling and model and try again."

@app.route('/call_models',methods=['POST'])
def call_models():

    # list of supported web services
    supported_services = {"intelligent_assignment_volume" : "http://152.7.99.200:5000/volume",
                          "intelligent_assignment_problems" : "http://152.7.99.200:5000/problem",
                          "intelligent_assignment_suggestions" : "http://152.7.99.200:5000/suggestions",
                          }
    
    # get JSON input as a dict
    in_dict = flask.request.json
    
    # prepare output JSON
    output = {}
    
    # each top level entry is a service to call
    for service in in_dict["services"]:
        
        # check if service is supported
        if service not in supported_services.keys():
            
            raise UnsupportedModelException()
            
        # if so, get info for this service
        json_dict_for_service = in_dict["input"]
   
        service_url = supported_services[service]
        
        # make POST request, get reply
        response = requests.post(service_url, json=json_dict_for_service)
        
        # add reply to output json
        output[service] = response.json()

    # have concluded for all services, send reply
    return flask.Response(json.dumps(output))

if __name__=='__main__':
    app.run(debug=True, port=3013)