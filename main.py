from helper import get_class
from flask import make_response
import functions_framework
import json


@functions_framework.http
def main(request):

     # get the string variable passed by the user
    request_json = request.get_json()
    url = request_json['calls'][0][0]
    
    #get class
    result = get_class(url)

    #return result
    return json.dumps({
        # each reply is a STRING (JSON not currently supported)
        'replies': result})

