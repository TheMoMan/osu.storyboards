# coding=utf8
from __future__ import print_function, division
from builtins import *
from PIL import Image, ImageFont, ImageDraw, ImageFilter

with open("./loc.txt", "r") as f:
    folder = f.readline() + "/sb/lyrics/"

with open("./lyrics.txt", "r", encoding="utf8") as f:
    lyrics = f.readlines();
lyrics = u"".join(lyrics)
# print(lyrics)

font = "C:/Windows/Fonts/Yu Mincho/yumindb.ttf"

# Use Pillow to draw each character file
characters = []
g_count = 0

badCharacters = [u"　", u"\ufeff", u"\u3000", u"\n"];
# for i in range(len(badCharacters)):
#     badCharacters[i] = badCharacters[i].encode("utf8")

for i in range(len(lyrics)):
    if lyrics[i] not in badCharacters and lyrics[i] not in characters:
        dimX, dimY = 300, 300
        txt = Image.new("RGBA", (dimX, dimY))

        # Shadow
        fnt = ImageFont.truetype(font, size=240, encoding="unic")

        d = ImageDraw.Draw(txt)

        # Find size and position relatively
        size = d.textsize(lyrics[i], font=fnt)
        #print(size)
        length = round(size[0]*.5)
        height = round(size[1]*.5)

        shadowOffset = 0
        shadowX = (dimX*.5) + shadowOffset - length
        shadowY = (dimX*.5) + shadowOffset - height
        bold = 7.5
        d.text((shadowX, shadowY), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
        d.text((shadowX+bold, shadowY+bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
        d.text((shadowX+bold, shadowY-bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
        d.text((shadowX-bold, shadowY+bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")
        d.text((shadowX-bold, shadowY-bold), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")

        #txt = txt.resize((116, 116))
        #txt = txt.crop((8, 8, 108, 108))
        txt = txt.filter(ImageFilter.GaussianBlur(12))

        # Foreground
        fnt = ImageFont.truetype(font, size=240, encoding="unic")

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

print("done")