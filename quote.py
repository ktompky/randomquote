import requests
import json
import random
from PIL import Image, ImageFont, ImageDraw



def getquote():

    r = requests.get('https://type.fit/api/quotes')
    data = r.json()

    quote = random.choice(data)
    print(quote['text'])
    print(quote['author'])
    return quote['text'] + " \n" + quote['author']


final_quote = getquote()

# open image
my_image = Image.open('wide_image.jpg')
title_font = ImageFont.truetype('Raleway/static/Raleway-Bold.ttf', 100)
# draw image object
image_editable = ImageDraw.Draw(my_image)

# add text to image
image_editable.text((215,515), final_quote, (0, 0, 0), font=title_font)

# save image
my_image.save("result.jpg")


















