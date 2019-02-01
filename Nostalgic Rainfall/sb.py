# coding=utf8
from __future__ import print_function, division
from builtins import *
from osbpy import *
from drawLyrics import *
from random import randint

### Let's start with the background scenes
sc = "sb/scene/"
bgs = 480/1080

size = 0.46

bkg = "Background"
ctr = "Centre"

# Shortcuts
def transition(scene1, scene2, startTime, endTime):
    """
    Simple fade transition for two scenes
    Duration of transition is between startTime and endTime
    """
    st, fn = startTime, endTime
    outa = scene1.fade(0, fn, fn, 1, 0)
    outb = scene2.fade(0, st, fn, 0, 1)
    return outa, outb

def createScene(sceneLetter, sceneTime, sceneLength, scenes, excpt):
    """
    Creates a list of osbjects for each scene in a section
    """
    sceneToAppend = []
    for i in range(sceneLength):
        scene = osbject(sc+"{}{}.jpg".format(sceneLetter,i), bkg, ctr, 320, 240)

        if i not in excpt:
            # Don't scale for scenes that'll have a scale later
            scene.scale(0, sceneTime, sceneTime, size, size)

        sceneToAppend.append(scene)

    scenes.append(sceneToAppend)

def ruRuRaRa(time):
    """
    Creates objects and animations for Ru Ru Ra Ra part
    """
    # Start and end times for each object
    start1 = time
    start2 = time + 182
    start3 = start2 + 364
    start4 = start3 + 364
    end = 500

    # Other constants
    scle = 0.5
    xMovement = 10
    rtate = 0.17
    rtateEnd = 0.2
    fadeDelay = 100

    y1 = 240
    y2 = 180
    yMovement = 50

    a = osbject("sb/ru.png", bkg, ctr, 320, 240)
    b = osbject("sb/ru.png", bkg, ctr, 320, 240)
    c = osbject("sb/ra.png", bkg, ctr, 320, 240)
    d = osbject("sb/ra.png", bkg, ctr, 320, 240)

    a.scale(0, start1, start1, scle, scle)
    b.scale(0, start2, start2, scle, scle)
    c.scale(0, start3, start3, scle, scle)
    d.scale(0, start4, start4, scle, scle)

    a.colour(0, start1, start1, 255, 179, 186, 255, 179, 186)
    b.colour(0, start2, start2, 255, 255, 186, 255, 255, 186)
    c.colour(0, start3, start3, 186, 255, 201, 186, 255, 201)
    d.colour(0, start4, start4, 186, 255, 255, 186, 255, 255)

    a.moveX(0, start1, start1 + end, 80, 80 - xMovement)
    b.moveX(0, start2, start2 + end, 240, 240 + xMovement)
    c.moveX(0, start3, start3 + end, 400, 400 - xMovement)
    d.moveX(0, start4, start4 + end, 560, 560 + xMovement)

    a.moveY(1, start1, start1 + end, y1, y1 - yMovement)
    b.moveY(1, start2, start2 + end, y2, y2 - yMovement)
    c.moveY(1, start3, start3 + end, y1, y1 - yMovement)
    d.moveY(1, start4, start4 + end, y2, y2 - yMovement)

    a.fade(0, start1 + fadeDelay, start1 + end, 1, 0)
    b.fade(0, start2 + fadeDelay, start2 + end, 1, 0)
    c.fade(0, start3 + fadeDelay, start3 + end, 1, 0)
    d.fade(0, start4 + fadeDelay, start4 + end, 1, 0)

    a.rotate(0, start1, start1, -rtate, -rtateEnd)
    b.rotate(0, start2, start2, rtate, rtateEnd)
    c.rotate(0, start3, start3, -rtate, -rtateEnd)
    d.rotate(0, start4, start4,-rtate, rtateEnd)

def ripple(time, posX, posY, scale, duration):
    """
    Ripple effect.
    """
    # Constants
    #duration = 900
    time2 = int(time + 100 * (duration/900))
    scaleX = 0.8 * scale
    scaleY = 0.2 * scale
    scale2 = 2/3
    dScale = 0.1 * scale
    dY = 50 * scale

    r = osbject("sb/ring.png", bkg, ctr, posX, posY)
    r.fade(0, time, time + duration, 0.8, 0)
    r.vecscale(19, time, time + duration, 0, 0, scaleX, scaleY)
    #r.para(0, time, time, "A")

    s = osbject("sb/ring.png", bkg, ctr, posX, posY)
    s.fade(0, time2, time2 + duration, 0.8, 0)
    s.vecscale(19, time2, time2 + duration, 0, 0, scaleX * scale2, scaleY * scale2)
    #s.para(0, time2, time2, "A")

    d = osbject("sb/drop.png", bkg, ctr, posX, posY)
    d.scale(0, time, time, dScale, dScale)
    d.moveY(1, time, time + duration, posY, posY - dY)
    d.fade(0, time, time + duration, 0.8, 0)
    #d.para(0, time, time, "A")

scenes = []

bgr = 0.475
lft = 306
rght = 334
dwn = 247
up = 233

# Kill the default background
bg = osbject("bg.jpg", bkg, ctr, 320, 240)
bg.fade(0, 0, 0, 0, 0)
bg.scale(0, 0, 0, bgs, bgs)

# Create backwhite, this makes background white when no sprites present (instead of black)
backwhite = osbject("sb/white.png", bkg, ctr, 320, 240)

# Scene a, Intro
excpt = [1]
createScene("a", 343, 7, scenes, excpt)
a0, a1, a2, a3, a4, a5, a6 = scenes[0]

# First scene should be done manually
a0.fade(0, 343, 1070, 0, 1)
a0.moveX(0, 343, 7434, lft, rght)

transition(a0, a1, 6343, 7434)
a1.scale(0, 6343, 12888, bgr, bgs)

transition(a1, a2, 11979, 12888)
a2.moveX(0, 11979, 17797, rght, lft)

transition(a2, a3, 16707, 17797)
a3.moveX(0, 16707, 20888, rght-6, lft+6)

transition(a3, a4, 19979, 20888)
a4.moveX(0, 19979, 23797, rght, lft)

transition(a4, a5, 23252, 23797)
a5.moveY(0, 23252, 25434, up, dwn)

transition(a5, a6, 25434, 25394)
a6.moveY(0, 25434, 32525, up, dwn)
#32525

# Scene b, Verse 1

excpt = [0, 3, 4]
createScene("b", 32525, 5, scenes, excpt)
b0, b1, b2, b3, b4 = scenes[1]

transition(a6, b0, 32525, 32525)
b0.scale(0, 32525, 38707, bgr, bgs)

transition(b0, b1, 38161, 38707)
b1.moveX(0, 38161, 44343, lft, rght)

transition(b1, b2, 43797, 44343)
b2.moveX(0, 43797, 49797, rght, lft)

transition(b2, b3, 49434, 49797)
b3.scale(0, 49434, 52707, bgr, bgs)

# Motion blur
b4a = osbject(sc+"b4a.jpg", bkg, ctr, 920, 240)
transition(b3, b4a, 52707, 52707)

b4a.scale(0, 52707, 52707, bgr, bgr)
b4a.moveX(0, 52707, 52797, 920, rght)

b4.scale(0, 52797, 52797, bgr, bgr)
b4.moveX(0, 52797, 55252, rght, lft)

backwhite.fade(0, 52707, 52797, 1, 1)
backwhite.fade(0, 52797, 52797, 0, 0)

# Scene c, Chorus 1
excpt = [0, 3, 4, 7, 8]
createScene("c", 52707, 10, scenes, excpt)
c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = scenes[2]

transition(b4, c0, 54888, 54888)
## Needs blur
c0.scale(0, 55706, 55797, 1.5, bgr)
c0.scale(0, 55797, 64161, bgr, bgs)
c0a = osbject(sc+"c0a.jpg", bkg, ctr, 320, 240)
c0a.scale(0, 55706, 55797, 1.5, 1.5)
c0a.fade(2, 54888, 55797, 1, 0)

c0.move(0, 54888, 55797, 340, 230, 320, 240)
c0a.move(0, 54888, 55797, 340, 230, 320, 240)

transition(c0, c1, 63616, 64161)
c1.moveX(0, 63616, 65616, rght-8, lft+8)

transition(c1, c2, 65252, 65616)
c2.moveX(0, 65252, 67979, rght-6, lft+6)

transition(c2, c3, 67434, 67797)
c3.scale(0, 67434, 67525, 1.2, bgr)
c3.scale(0, 67525, 73434, bgr, bgs)

transition(c3, c4, 73070, 73434)
c4.scale(0, 73070, 73161, 1, 0.455)
c4.scale(0, 73161, 76707, 0.455, bgs)

transition(c4, c5, 76343, 76707)
c5.moveY(0, 76343, 80525, dwn-2, up+2)

transition(c5, c6, 80525, 80525)
c6.moveX(0, 80525, 83979, rght-6, lft+6)

transition(c6, c7, 83434, 83979)
c7.scale(0, 83434, 86888, 0.455, bgs)

transition(c7, c8, 86343, 86888)
c8.scale(0, 86343, 89797, 0.455, bgs)

transition(c8, c9, 89252, 89797)
c9.moveX(0, 89252, 90707, rght-11.5, lft+11.5)


# Scene d, Verse 2
excpt = []
createScene("d", 90707, 6, scenes, excpt)
d0, d1, d2, d3, d4, d5 = scenes[3]

backwhite.fade(0, 90707, 91434, 1, 1)
backwhite.fade(0, 91434, 91434, 0, 0)

transition(c9, d0, 90843, 90843)
## This needs animated transition

#d0.moveY(0, 90707, 90888, 0, up)
d0b = osbject(sc+"d0b.png", bkg, ctr, 320, 240)
d0bo = 195
d0b.moveY(0, 90707, 90843, 0+d0bo-300, up+d0bo)
d0b.scale(0, 90707, 90707, size, size)
d0.moveY(0, 90843, 91979, up, dwn)
d0ao = 55
d0a = osbject(sc+"d0a.jpg", bkg, ctr, 320, 240)
d0a.moveY(0, 90707, 90843, 0-d0ao-300, up-d0ao)
d0a.scale(0, 90707, 90707, size, size)

transition(d0, d1, 91434, 91979)
d1.moveX(0, 91434, 97070, rght, lft)

transition(d1, d2, 96525, 97070)
d2.moveX(0, 96525, 102888, rght, lft)

transition(d2, d3, 102343, 102888)
d3.moveX(0, 102343, 108343, rght, lft)

transition(d3, d4, 107797, 108343)
d4.moveX(0, 107797, 111070, rght, lft)

transition(d4, d5, 110525, 111070)
d5.moveX(0, 110525, 113252, rght, lft)

# Scene e, Chorus 2
# Ordering matters here to make parallax for blackboard work
# e2 needs to be below everything
e2 = osbject(sc+"e2.jpg", bkg, ctr, 320, 240)
e2a = osbject(sc+"e2a.png", bkg, ctr, 315, 260)
excpt = [0, 1, 2]
createScene("e", 113252, 4, scenes, excpt)
e0, e1 = scenes[4][0], scenes[4][1]
e3 = scenes[4][3]

e2.scale(0, 125616, 125707, 1.2, bgr)
e2.scale(0, 125707, 131616, bgr, bgs+.01)
#e2a.fade(1, 125616, 125979, 0, 1)
e2a.scale(0, 125616, 125707, 1.2, bgr+.02)
e2a.scale(0, 125707, 131616, bgr+.02, bgs+.02)
#e2a.fade(2, 131252, 131616, 1, 0)

# Motion for blackboard parallax
bbStep = 360
currentX = 320
currentY = 240
prevX = 99
prevY = 99
plusX = 0
plusY = 0
for i in range(6000/bbStep):
    while plusX == prevX and plusY == prevY:
        # Anti roll the same numbers
        plusX = randint(-1, 1)
        plusY = randint(-1, 1)

    prevX = plusX
    prevY = plusY

    e2.move(0, 125616+i*bbStep, 125616+(i+1)*bbStep, currentX, currentY, 320+plusX, 240+plusY)
    currentX = 320+plusX
    currentY = 240+plusY

transition(d5, e0, 113252, 113252)

##Blur again
e0.scale(0, 114070, 114161, 1.1, bgr)
e0.scale(0, 114161, 119979, bgr, bgs)
e0a = osbject(sc+"e0a.jpg", bkg, ctr, 320, 240)
e0a.scale(0, 114070, 114161, 1.1, 1.1)
e0a.fade(2, 113252, 114161, 1, 0)

e0.move(0, 113252, 114161, 340, 230, 320, 240)
e0a.move(0, 113252, 114161, 340, 235, 320, 240)

transition(e0, e1, 119434, 119979)
e1.scale(0, 119434, 119434, 0.47, 0.47)
e1.moveX(0, 119434, 125979, rght+10, lft-10)
e1.fade(0, 125616, 125979, 1, 0)

#transition(e1, e2, 125616, 125979)

transition(e2, e3, 131252, 131616)
e3.moveX(0, 131252, 135979, lft, rght)

# Scene f, 7/4 section

# Same thing as the blackboard to stop it raining indoors
f3 = osbject(sc+"f3.jpg", bkg, ctr, 320, 240)

# Make it rain in the window
for i in range(145070, 155252, 33):
    rainX = randint(-10, 558)
    rainS = randint(5, 15) * .01
    r = osbject("sb/rain.png", bkg, ctr, rainX, 240)
    r.moveY(0, i, i+250, -50, 492)
    r.vecscale(0, i, i, 0.08, rainS, 0.08, rainS)
    r.colour(0, i, i, 220, 220, 220, 220, 220, 220)
    r.para(0, i, i, "A")

    if i >= 154706:
        r.fade(0, 154706, 155252, 0.5, 0)
    else:
        r.fade(0, i, i, 0.5, 0.5)

f3a = osbject(sc+"f3a.png", bkg, ctr, 320, 240)

excpt = [2, 3, 4, 5]
createScene("f", 135979, 7, scenes, excpt)
f0, f1, f2, = scenes[5][0], scenes[5][1], scenes[5][2]
f4, f5, f6 = scenes[5][4], scenes[5][5], scenes[5][6]

transition(e3, f0, 135979, 135979)
f0.moveX(0, 135979, 139434, rght, lft)

transition(f0, f1, 138888, 139434)
f1.moveX(0, 138888, 141979, rght, lft)

transition(f1, f2, 141434, 141979)
f2.scale(0, 141434, 145070, bgr, bgs)

#transition(f2, f3, 145070, 145070)
#f3m = 270
#f3.scale(0, 145070, 145070, 0.5, 0.5)
#f3.move(0, 145070, 150161, 373, f3m, 373, f3m-10)

transition(f2, f3, 145070, 145070)
f3.moveY(0, 145070, 155252, 305, 175)
f3.scale(0, 145070, 145070, size, size)

f3a.scale(0, 145070, 145070, size, size)
#f3a.fade(0, 154706, 155252, 1, 0)
f3a.moveY(0, 145070, 155252, 305, 175)

transition(f3, f4, 154706, 155252)
f4.scale(0, 154706, 157615, 0.47, 0.465)

transition(f4, f5, 156343, 157615)
f5.scale(0, 156343, 160706, bgr, 0.465)

transition(f5, f6, 159797, 160706)
f6.moveY(0, 159797, 166525, dwn, up)

# Scene g, Solo
excpt = [0, 3]
createScene("g", 166525, 4, scenes, excpt)
g0, g1, g2, g3 = scenes[6]

transition(f6, g0, 166525, 166525)
g0.scale(0, 166525, 172161, bgr, bgs)

transition(g0, g1, 171615, 172161)
g1.moveX(0, 171615, 175979, rght, lft)

transition(g1, g2, 175252, 175979)
g2.moveX(0, 175252, 180343, rght, lft)

transition(g2, g3, 179797, 180343)
## Blur here
g3.scale(0, 179797, 183797, bgr, bgs)
g3a = osbject(sc+"g3a.jpg", bkg, ctr, 320, 240)
g3a.scale(0, 179797, 183797, bgr, bgs)
g3a.fade(2, 182706, 183252, 0, 1)

# Scene h, pre-Chorus
excpt = [2]
createScene("h", 183797, 3, scenes, excpt)
h0, h1, h2 = scenes[7]

transition(g3, h0, 183797, 183797)
h0.moveX(0, 183797, 189979, rght, lft)

transition(h0, h1, 189434, 189979)
h1.moveX(0, 189434, 193070, rght-6, lft+6)

transition(h1, h2, 192525, 193070)
h2.scale(0, 192525, 192615, 1.2, 0.47)
h2.scale(0, 192615, 195706, 0.47, bgs)

# Scene i, Chorus 3 + Outro
excpt = [0, 1, 2, 4]
createScene("i", 195706, 9, scenes, excpt)
i0, i1, i2, i3, i4, i5, i6, i7, i8 = scenes[8]

transition(h2, i0, 195706, 195706)
## Blur again
i0.scale(0, 196434, 196525, 0.9, 0.46)
i0.scale(0, 196525, 201979, 0.46, bgs)
i0a = osbject(sc+"i0a.jpg", bkg, ctr, 320, 240)
i0a.scale(0, 195706, 196525, 0.9, 0.9)
i0a.fade(2, 195706, 196525, 1, 0)

i0y = -95
i0.move(0, 195706, 196434, 330, 250+i0y, 320, 240+i0y)
i0a.move(0, 195706, 196434, 330, 250+i0y, 320, 240+i0y)
i0.move(0, 196434, 196525, 330, 250+i0y, 320, 240)
i0a.move(0, 196434, 196525, 330, 250+i0y, 320, 240)

transition(i0, i1, 201434, 201979)
i1.scale(0, 201434, 204706, 0.46, 0.45)

transition(i1, i2, 203252, 204706)
i2.scale(0, 203252, 207525, 0.465, bgs)

transition(i2, i3, 207434, 207525)
i3.moveX(0, 207434, 207525, 640, rght)
i3.moveX(0, 207525, 213797, rght, lft)

transition(i3, i4, 213434, 213797)
i4.scale(0, 213434, 213525, 0.6, bgr)
i4.scale(0, 213525, 219434, bgr, bgs)

transition(i4, i5, 218888, 219434)
i5.moveX(0, 218888, 227979, rght, lft)

transition(i5, i6, 222525, 223070)
##Blur thing
i6.moveX(0, 218888, 227979, rght, lft)
i6a = osbject(sc+"i6a.jpg", bkg, ctr, 320, 240)
i6a.moveX(0, 218888, 227979, rght, lft)
i6a.fade(0, 226525, 226888, 0, 1)
i6a.scale(0, 226525, 226525, size, size)

transition(i6, i7, 227979, 227979)
i7.moveY(0, 227979, 232343, up, dwn)

transition(i7, i8, 231615, 232343)
i8.moveX(0, 231615, 236525, rght, lft)

# Final scene is also manual
i8.fade(0, 236161, 236525, 1, 0)

# Rain for chorus 2
# Actually let's just add rain where it looks good

def rain(start, end, fadeStart, fadeEnd):
    for i in range(start, end, 20):
        rainX = randint(-105, 745)
        rainS = randint(5, 15) * .01
        r = osbject("sb/rain.png", bkg, ctr, rainX, 240)
        r.moveY(0, i, i+250, -50, 492)
        r.vecscale(0, i, i, 0.08, rainS, 0.08, rainS)
        r.colour(0, i, i, 220, 220, 220, 220, 220, 220)
        r.para(0, i, i, "A")

        if i >= fadeStart:
            r.fade(0, fadeStart, fadeEnd, 0.5, 0)
        else:
            r.fade(0, i, i, 0.5, 0.5)

rain(343, 25252, 25343-250, 25434)
rain(113070, 125979, 125616, 125979)
rain(136161, 141979, 141434, 141979)

# Transition thing for intro. Down here so it's ontop of the rain
a5a = osbject(sc+"a5a.jpg", bkg, ctr, 320, 480)
a5a.moveY(0, 25252, 25434, -1680, 2160)

# Whiteouts
white = osbject("sb/white.png", bkg, ctr, 320, 240)

white.fade(0, 31252, 32343, 0, 1)
white.fade(1, 32616, 33070, 1, 0)
white.fade(0, 54525, 54888, 0, 1)
white.fade(1, 54979, 55161, 1, 0)
white.fade(0, 79979, 80434, 0, 1)
white.fade(1, 80525, 81070, 1, 0)
white.fade(0, 112707, 112888, 0, 1)
white.fade(1, 113252, 113434, 1, 0)
white.fade(0, 135070, 135979, 0, 1)
white.fade(0, 136161, 136525, 1, 0)
white.fade(0, 144161, 144706, 0, 1)
white.fade(0, 145070, 146343, 1, 0)
white.fade(0, 165070, 165797, 0, 1)
white.fade(0, 166706, 167070, 1, 0)
white.fade(0, 183252, 183797, 0, 1)
white.fade(0, 183979, 184343, 1, 0)
white.fade(0, 195434, 195615, 0, 1)
white.fade(1, 195706, 195888, 1, 0)
white.fade(0, 226525, 227434, 0, 1)
white.fade(0, 227979, 229070, 1, 0)

# lyrics

lyricsFile = "lyrics.txt"
font = "msgothic.ttc"
folder = "E:/Extra Games/osu!/Songs/Nostalgic Rainfall/sb/lyrics/"

with open(lyricsFile, "r", encoding="utf8") as f:
    lyrics = f.readlines()
lyricsFull = u"".join(lyrics)

with open("times.txt", "r") as f:
    times = []
    for i in f:
        times.append([int(x) for x in i.split()])

for i in range(len(lyrics)):
    lyrics[i] = lyrics[i].replace(u"\n", "")

#drawLyrics(lyricsFull, font, folder)
characters = getCharacters(lyricsFull)
charX = 20
charY = 410
spacing = 28
charSz = 0.35
fadeTime = 200

for i in range(len(lyrics)):
    lineLen = len(lyrics[i]) # Length of each line
    charOffset = 0
    periodCount = 0
    fadeOffset = 0

    for j in range(len(lyrics[i])):
        # Find character file
        char = lyrics[i][j]
        if char != u"\u3000":
            # If the character is not a space

            if periodCount == 1:
                # If previous character was period
                charOffset += -6
                periodCount -= 1

            if char == u".":
                # Offset exception for .
                charOffset += 16
                periodCount += 1

            else:
                # Character offset
                charOffset += spacing

            cX = charX + charOffset

            charIndex = characters.index(char)
            charFile = "sb/lyrics/{}.png".format(charIndex)

            # Find time
            charStart = times[i][0]
            charEnd = times[i][1]
            cTrueStart = charStart-fadeTime+fadeOffset
            cTrueEnd = charEnd+fadeTime+fadeOffset

            # Total active time, for movement calculations
            cTotalTime = cTrueEnd - cTrueStart
            cMovement = cTotalTime * 0.005

            # Place on the SB
            c = osbject(charFile, "Foreground", ctr, charX + charOffset, charY)
            c.scale(0, charStart, charEnd, charSz, charSz)
            #c.para(0, cTrueStart, cTrueEnd, "A")
            #c.colour(0, cTrueStart, cTrueEnd, 0, 0, 0, 0, 0, 0)
            c.fade(0, cTrueStart, charStart+fadeOffset, 0, 1)
            c.fade(0, charEnd+fadeOffset, cTrueEnd, 1, 0)
            c.moveX(0, cTrueStart, cTrueEnd, cX, cX + cMovement)

        else:
            charOffset += spacing/2

        fadeOffset += 30

# Ru Ru Ra Ra ~~
ruRuRaRa(73252)
ruRuRaRa(131434)
ruRuRaRa(213252)
ruRuRaRa(216161)
ruRuRaRa(219070)

ripple(706, 540, 380, 0.75, 900)
ripple(2161, 100, 140, 0.75, 900)
ripple(5252-100, 320, 240, 1.2, 900)

ripple(194706-100, 80, 240, 0.75, 450)
ripple(194888-100, 240, 240, 0.75, 450)
ripple(195070-100, 400, 240, 0.75, 450)
ripple(195252-100, 560, 240, 0.75, 450)

# Credit yamaco
# Bodge job because cba to make a proper function

# yamaco = osbject("sb/yamaco.png", bkg, ctr, 260, 320)
# yamaco.scale(0, 233797, 233797, 0.3, 0.3)
# yamaco.moveX(0, 233797, 236525, 220, 230)
# yamaco.fade(0, 233797, 234524, 0, 1)
# yamaco.fade(0, 236161, 236525, 1, 0)

yamaco = u"Illustrations:　ヤマコ"
yamaList = u"Ilustraion:ヤマコ"
#           I L L   U   S   T R A   T   I O N   S   : _  Y  M  C
creditsX = [0,3,2.5,3.5,4.5,4,4,4.2,4.2,3,4,4.5,4.5,4,9,9,9,9]
cX = 0

for i in range(len(yamaco)):
    yChar = yamaco[i]

    if yChar != u"　":
        yInd = yamaList.index(yChar)

        cX += creditsX[i]*5.25*(5/6)
        cT = 30 * i

        cY = 0
        if yChar == ":":
            cY = 4.5

        c = osbject("sb/c/{}.png".format(yInd), bkg, ctr, 120+cX, 320+cY)
        c.scale(0, 233797, 233797, 0.5, 0.5)
        c.moveX(0, 233797, 236525, 100+cX, 110+cX)
        c.fade(0, 233797+cT, 233797+cT+200, 0, 1)
        c.fade(0, 236161, 236525, 1, 0)


export_path = u".../osu!/Songs/Nostalgic Rainfall/CHiCO with HoneyWorks - Nostalgic Rainfall (-Mo-).osb"
osbject.end(export_path)
