from helper import get_class
from flask import make_response
import functions_framework
import json


@functions_framework.http
def main(request):

     # get the string variable passed by the user
    request_json = request.get_json()
    calls = request_json['calls'][0]
    replies = []

    for call in calls:
        result = get_class(call)
        #get class
        replies.append(result)
   

    #return result
    return json.dumps({
        # each reply is a STRING (JSON not currently supported)
        'replies': [json.dumps(reply) for reply in replies]
      })

