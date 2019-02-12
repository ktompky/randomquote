import requests
import json

user_choice = input("Do you want to get a quote? 'y' or 'n' ")


def getquote():

    r = requests.get('http://quotesondesign.com/api/3.0/api-3.0.json')
    data = r.json()

    author = data.get('author')
    quote = data.get('quote')

    print(quote, "\n  \t\t\t- by", author)


while user_choice == 'y':
    getquote()
    user_choice = input("Would you like another quote? 'y' or 'n' ")
if user_choice == 'n':
    print("Okayyyyyy.")




















