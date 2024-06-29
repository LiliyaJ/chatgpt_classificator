import pandas as pd

from flask import make_response 
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


from openai import OpenAI
client = OpenAI()