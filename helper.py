import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

from flask import make_response 
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


from openai import OpenAI
client = OpenAI()

def scrap_and_clean(url):
    '''  
    FUNCTION:
    Scrapes the text and remove tags    
    
    INPUT:
    url - a url from which the text should be taken and scraped
    
    OUTPUT:
    the content of the webpage cleaned from tags in string format
    
    '''

    #increase mac redirects (default are 30)
    requests.session().max_redirects = 100

    #get text from a url
    r = requests.get(url, allow_redirects=False).text

    #parse html content
    soup = bs(r, 'html.parser')

    for data in soup(['script', 'style']):
        #remove tags
        data.decompose()

    #return string with the text
    return ' '.join(soup.stripped_strings)

