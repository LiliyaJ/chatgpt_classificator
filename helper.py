import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

from flask import make_response 
import os

#for local debugging
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
clientAI = OpenAI()

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

def get_class(url):
    message = scrap_and_clean(url)

    promt = f"""Classify the following text as SEO, SEA or Web Analytics. No further options are available.
    Message: '{message}'.
    The output can only conatin one of these words.
    Do not include any further information into the output.
    """

    response = clientAI.chat.completions.create(
        model = "gpt-3.5-turbo",
        temperature=0.0,
        messages=[{"role": "user", "content": promt}]
    )
    return response.choices[0].message.content

url = 'https://www.more-fire.com/blog/strukturierte-daten-guide/'
print(get_class(url))