# coding=utf8
from __future__ import print_function, division
from builtins import *
from osbpy import *
#from math import pi
from random import randint, uniform
from PIL import Image, ImageFont, ImageDraw, ImageFilter

characters = []
g_count = 0
def drawLyrics(lyrics):
    # Use Pillow to draw each character file
    global characters, g_count
    for i in range(len(lyrics)):
        if lyrics[i] not in [u"　", u"\ufeff", u"\u3000", "\n"] and lyrics[i] not in characters:
            dimX, dimY = 100, 100
            txt = Image.new("RGBA", (dimX, dimY))

            # Shadow
            fnt = ImageFont.truetype("EPGYOBLD.TTF", size=86, encoding="unic")

            d = ImageDraw.Draw(txt)

            # Find size and position relatively
            size = d.textsize(lyrics[i], font=fnt)
            #print(size)
            length = round(size[0]*.5)
            height = round(size[1]*.5)

            shadowOffset = 2
            shadowX = (dimX*.5) + shadowOffset - length
            shadowY = (dimX*.5) + shadowOffset - height
            d.text((shadowX, shadowY), lyrics[i], font=fnt, fill=(0,0,0,255), align="center")

            txt = txt.filter(ImageFilter.GaussianBlur(4))

            # Foreground
            fnt = ImageFont.truetype("EPGYOBLD.TTF", size=80, encoding="unic")

            d = ImageDraw.Draw(txt)

            # Find size and position relatively
            size = d.textsize(lyrics[i], font=fnt)
            #print(size)
            length = round(size[0]*.5)
            height = round(size[1]*.5)

            d.text((dimX*.5-length, dimY*.5-height), lyrics[i], font=fnt, fill=(255,255,255,255), align="center")

            txt.save("songFolder\senya - Zetsubou no Fuchi\sb\{}.png".format(g_count))
            g_count+=1
            characters.append(lyrics[i])

with open("lyrics.txt", "r", encoding="utf8") as f:
    lyrics = f.readlines()

with open("lyrics_times.txt", "r") as f:
    lyricsTimes = []
    for i in f:
        lyricsTimes.append([int(x) for x in i.split()])

for i in range(len(lyrics)):
    lyrics[i] = lyrics[i].replace(u"\ufeff", "")
    lyrics[i] = lyrics[i].replace(u"\n", "")
    drawLyrics(lyrics[i])

#print("characters:",characters)
#print("lyrics:",lyrics)
#print(lyricsTimes)

### Background

bgs = 480/1080

bg = osbject("bg.jpg", "Background", "Centre", 320, 240)
bg.scale(0,0,186211,bgs,bgs)

### Lyrics

for i in range(len(lyrics)):
    lineLen = len(lyrics[i]) # Length of each line in characters
    charDelay = 60 # Delay between each character

    lineSpacing = 50

    # Find midpoint, place relative to midpoint
    lineStartX = 480 - (lineLen/2 * lineSpacing)
    basePos = [lineStartX, 220]
    sz = 0.6
    if lineLen > 8 and u"." not in lyrics[i]:
        basePos[0] -= 15 * (lineLen-7)

    #print("line", i)
    #print(len(lyrics[i]))

    # Reset offset after each line
    charOffset = basePos[0]
    periodCount = 0

    for j in range(len(lyrics[i])):
        # Find character file
        char = lyrics[i][j]
        charIn = characters.index(char)
        #print(char.encode("utf8"))
        charFile = "sb/{}.png".format(charIn)

        # Find time
        charStart = lyricsTimes[i][0] + charDelay*j
        charEnd = lyricsTimes[i][1] + charDelay*j - 200

        # Drop speed
        charSpeed = 0.03 # units per ms
        charTime = charEnd - charStart # To calc speed
        charDrop = .5 * charTime * charSpeed
        charDrop = round(charDrop)

        # Place on SB
        if lyrics[i][j] == u".":
            # Spacing exception for .
            if periodCount == 0:
                lineSpacing = 35
                periodCount += 1
            else:
                lineSpacing = 20
        else:
            lineSpacing = 48

        charOffset += lineSpacing
        #print(charOffset)

        # Randomise height
        randomHeight = randint(0, 10)

        charPos = (charOffset, basePos[1])
        c = osbject(charFile, "Foreground", "Centre", charPos[0], charPos[1])
        c.scale(0, charStart, charEnd, sz, sz)
        c.moveY(1, charStart-1000, charStart, charPos[1]+500, charPos[1]-charDrop+randomHeight)
        c.moveY(0, charStart, charEnd-800, charPos[1]-charDrop+randomHeight, charPos[1]+charDrop+randomHeight)
        c.moveY(2, charEnd-700, charEnd, charPos[1]+charDrop+randomHeight, charPos[1]-500)

    # Bubbles
    slowBubbles = randint(2, 3)
    fastBubbles = randint(lineLen*5, lineLen*7) # Depends on number of characters

    lineStartT = lyricsTimes[i][0]
    lineEndT = lyricsTimes[i][1]
    lineTime = lineStartT - lineEndT # To calc speed

    for j in range(slowBubbles):
        bPosX = randint(basePos[0]-50, charOffset+50)
        bPosY = randint(100, 300)

        bSpeed = round(uniform(0.02, 0.06), 3)
        bDrop = round(.5 * bSpeed * lineTime, 0)
        bSize = round(uniform(0.1, 0.3), 2)

        b = osbject("sb/bubble.png", "Background", "Centre", bPosX, 740)
        b.scale(0, lineStartT, lineStartT, bSize, bSize)
        b.moveY(1, lineStartT-700, lineStartT+300, 740, bPosY)
        b.moveY(0, lineStartT+300, lineEndT-800, bPosY, bPosY-bDrop)
        b.moveY(2, lineEndT-800, lineEndT, bPosY-bDrop, -260)
        b.fade(0, lineStartT, lineStartT, 0.75, 0.75)
        b.para(0, lineStartT, lineStartT, "A")

    #fastCount = 0
    for j in range(fastBubbles):
        bPosX = randint(basePos[0], charOffset+50)
        bSize = round(uniform(0.01, 0.04), 2)
        bRiseY = randint(100, 200)
        bRiseT = randint(200, 800)

        b = osbject("sb/bubble.png", "Background", "Centre", bPosX, 740)
        b.scale(0, lineEndT, lineEndT, bSize, bSize)
        b.moveY(2, lineEndT-1800, lineEndT-bRiseT+200, 740, -260+bRiseY)
        b.fade(0, lineStartT, lineStartT, 0.75, 0.75)
        b.para(0, lineEndT, lineEndT, "A")

        b = osbject("sb/bubble.png", "Background", "Centre", bPosX, 740)
        b.scale(0, lineStartT, lineStartT, bSize, bSize)
        b.moveY(2, lineStartT-1500, lineStartT-bRiseT+500, 740, -260+bRiseY)
        b.fade(0, lineStartT, lineStartT, 0.75, 0.75)
        b.para(0, lineStartT, lineStartT, "A")

export_path = u"songFolder\senya - Zetsubou no Fuchi (-Mo-).osb"
osbject.end(export_path)
