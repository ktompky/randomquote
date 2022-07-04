import requests
import json
import random

def getquote():

    r = requests.get('https://type.fit/api/quotes')
    data = r.json()

    quote = random.choice(data)
    print(quote['text'])
    print(quote['author'])


getquote()



















