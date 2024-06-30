from helper import get_class
from flask import make_response
import functions_framework


@functions_framework.http
def main(request):

     # get the string variable passed by the user
    url = request.args.get('url')

    #get class
    result = get_class(url)

    #return result
    return result

