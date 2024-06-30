from helper import get_class
from flask import make_response
import functions_framework
from flask import escape

@functions_framework.http
def main(request):

     # get the string variable passed by the user
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'url' in request_json:
        url = request_json['url']
    elif request_args and 'url' in request_args:
        url = request_args['url']
    else:
        return 'Error: No url provided', 400

    #get class
    result = get_class(url)

    #return result
    return result

