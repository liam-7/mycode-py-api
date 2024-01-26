#!/usr/bin/python3

# python3 -m pip install requests
import requests

# python3 -m pip install Django
from django.http import JsonResponse    # replaces "import json"

# API to lookup - Django will proxy the request for us
API = "http://api.open-notify.org/astros.json"
    
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
APINASA = "https://api.nasa.gov/planetary/apod?api_key="

# Your NASA API key goes here
# in production this should be set as an environmental variable
APIKEY = "DEMO_KEY"

def astro(request):    
    res = requests.get(API)
    return JsonResponse(res.json())  # abstraction to return json

def nasa(request):
    res = requests.get(f"{APINASA}{APIKEY}")
    return JsonResponse(res.json()) # abstraction to return json

