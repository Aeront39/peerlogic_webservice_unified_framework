# -*- coding: utf-8 -*-
"""
Takes JSON input and breaks down into seperate calls to other peerlogic
web services.
"""
import json
import requests

input_json = """{ "reviews" : [
      {
      "id" : 1,
      "text" : "This is incredible! I can't find a single thing wrong with your project! This is simply great, you are amazing, great job! Only thing I can say is I might have made the font size larger."
  },
      {
          "id" : 2,
          "text" : "I think your project is the worst thing I've seen in my entire life it's so terrible it makes me sick I hate it and everything about it. The home screen doesn't even have a button to navigate to the app."
      },
	    {
          "id" : 3,
          "text" : "It was good."
      }
  ],
 "services" : [
	 "problem",
	 "volume",
	 "suggestions"
 ]
  }"""

supported_services = {"volume" : "http://152.7.99.200:5000/volume",
                      "problem" : "http://152.7.99.200:5000/problem",
                      "suggestions" : "http://152.7.99.200:5000/suggestions",}

in_dict = json.loads(input_json)

# make a dict to use for passing to services
json_dict_for_services = in_dict.copy()
json_dict_for_services.pop("services")

# if the reviews dict has more than 10 elements, split it up and do 10 at a time


# prepare output JSON
output = {}

# break up reviews into 

# send a request to each service mentioned, if supported
for service in in_dict["services"]:
    
    if service in supported_services.keys():
        
        service_url = supported_services[service]
        
        # make POST request, get reply
        response = requests.post(service_url, json=json_dict_for_services)
        
        # add reply to output json
        output[service] = response.json()

# have concluded for all services, send reply
