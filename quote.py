import requests
import json


r = requests.get('http://quotesondesign.com/api/3.0/api-3.0.json')
data = r.json()


author = data.get('author')
quote = data.get('quote')

print(quote, "\n  \t\t\t- by", author)

















