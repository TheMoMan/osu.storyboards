# coding=utf8
from __future__ import print_function, division
from builtins import *
from PIL import Image, ImageFont, ImageDraw, ImageFilter

def drawLyrics(lyrics, fontFile, folder):
    """Generates image files for each character in the lyrics, and creates a list of
    characters where the index is the file name. No need to regenerate files for every 
    update so replace this function with getCharacters() after running."""
    
    # Use Pillow to draw each character file
    global characters, g_count # Should get rid of this next time
    characters = []
    g_count = 0
    for i in range(len(lyrics)):
        if lyrics[i] not in [u"　", u"\ufeff", u"\u3000", "\n"] and lyrics[i] not in characters:
            dimX, dimY = 100, 100
            txt = Image.new("RGBA", (dimX, dimY))

            # Shadow
            fnt = ImageFont.truetype(fontFile, size=80, encoding="unic")

            d = ImageDraw.Draw(txt)

            # Find size and position relatively
            size = d.textsize(lyrics[i], font=fnt)
            #print(size)
            length = round(size[0]*.5)
            height = round(size[1]*.5)

            shadowOffset = 0
            shadowX = (dimX*.5) + shadowOffset - length
            shadowY = (dimX*.5) + shadowOffset - height
            bold = 2.5
            d.text((shadowX, shadowY), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
            d.text((shadowX+bold, shadowY+bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
            d.text((shadowX+bold, shadowY-bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
            d.text((shadowX-bold, shadowY+bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
            d.text((shadowX-bold, shadowY-bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")

            #txt = txt.resize((116, 116))
            #txt = txt.crop((8, 8, 108, 108))
            txt = txt.filter(ImageFilter.GaussianBlur(4))

            # Foreground
            fnt = ImageFont.truetype(fontFile, size=80, encoding="unic")

            d = ImageDraw.Draw(txt)

            # Find size and position relatively
            size = d.textsize(lyrics[i], font=fnt)
            #print(size)
            length = round(size[0]*.5)
            height = round(size[1]*.5)

            d.text((dimX*.5-length, dimY*.5-height), lyrics[i], font=fnt, fill=(255,255,255,255), align="center")

            txt.save(folder+"{}.png".format(g_count))
            g_count+=1
            characters.append(lyrics[i])

def getCharacters(lyrics):
    """Returns a list of characters used in the lyrics where the index is the file name."""
    
    characters = []
    for i in range(len(lyrics)):
        if lyrics[i] not in [u"　", u"\ufeff", u"\u3000", "\n"] and lyrics[i] not in characters:
            characters.append(lyrics[i])

    return characters
