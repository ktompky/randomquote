import requests
import json
import random
from PIL import Image, ImageFont, ImageDraw



def getquote():
    r = requests.get('https://type.fit/api/quotes')
    data = r.json()
    quote = random.choice(data)
    return quote['text'] + " \n" + quote['author']

def getFortune():
    random_id = random.randint(1, 3)
    if random_id == 1:
        r = "You're going to have a great day!"
    elif random_id == 2:
        r = "You're going to have a bad day. Sorry bro."
    else:
        r = "The day is what you want it to be."
    return(r)


def finalImage():
    userAnswer = userInput()
    if userAnswer == "quote":
        final_quote = getquote()
        print("Check the result.jpg for your quotes!")
    elif userAnswer == "fortune":
        print('Check the result.jpg for your for fortune.')
        final_quote= getFortune()
    else:
        print('Well what do you want?')

    # open image
    my_image = Image.open('wide_image.jpg')
    title_font = ImageFont.truetype('Raleway/static/Raleway-Bold.ttf', 75)
    # draw image object
    image_editable = ImageDraw.Draw(my_image)
    # add text to image
    image_editable.text((215,515), final_quote, (0, 0, 0), font=title_font)
    # save image
    my_image.save("result.jpg")

def userInput():
    userAnswer = input("Would you like a quote or a fortune? ")
    return userAnswer

print(finalImage())













