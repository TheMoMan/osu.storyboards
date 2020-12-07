from __future__ import print_function, division
from builtins import *
from osbpy import *
from drawLyrics import *
from random import randint, uniform

# Shorthands
bkg = "Background"
ctr = "Centre"
sc = "sb/scene/"

bgs = 480/1080

def scene(sceneName, x=320, y=240):
    return osbject(sc + sceneName + ".jpg", bkg, ctr, x, y)

# Kill default background (remove this later)
bg = osbject(sc+"v.jpg", bkg, ctr, 320, 240)
bg.fade(0, 0, 0, 0, 0)
bg.scale(0, 0, 0, bgs, bgs)

# Make a white background
backWhite = osbject("sb/white.jpg", bkg, ctr, 320, 240)
backWhite.fade(0, 522, 985, 0, 1)
backWhite.fade(0, 309132, 309132, 1, 0)


### Scenes

# Intro
a = scene("a", 320, 340)
a.fade(0, 522, 985, 0, 1)
a.scale(0, 522, 522, .8, .8)
a.moveX(0, 522, 12652, 350, 250)
a.fade(0, 11726, 12466, 1, 0)

a = scene("a")
a.scale(0, 12652, 12744, 1, bgs+.01)
a.scale(0, 12744, 16169, bgs+.01, bgs)
a.fade(0, 14688, 16169, 1, 0)

v = scene("v")
v.fade(0, 16169, 16910, 0 ,1)
v.moveX(0, 16169, 22095, 330, 310)
v.moveY(0, 16169, 22095, 235, 245)
v.scale(0, 19132, 19132, .5, .5)

s = scene("s")
s.scale(0, 22095, 22188, 1, bgs+.01)
s.scale(0, 22188, 22651, bgs+.01, bgs)
# s.fade(6, 22188, 22651, 1, 0)
s.fade(0, 22095, 22281, 0, 1)

p = scene("p")
p.scale(0, 22651, 22744, 1, bgs+.01)
p.scale(0, 22744, 23206, bgs+.01, bgs)
# p.fade(6, 22744, 23206, 1, 0)
p.fade(0, 22651, 22836, 0, 1)

k = scene("k")
k.scale(0, 23206, 23299, 1, bgs+.01)
k.scale(0, 23299, 23762, bgs+.01, bgs)
# k.fade(6, 23299, 23762, 1, 0)
k.fade(0, 23206, 23392, 0, 1)

c = scene("c")
c.scale(0, 23762, 23855, 1, bgs+.01)
c.scale(0, 23855, 24410, bgs+.01, bgs)
# c.fade(6, 24132, 24410, 1, 0)
# c.moveY(0, 24318, 24410, 240, -240)
c.fade(0, 23762, 23947, 0, 1)

w = osbject(sc+"w.png", bkg, ctr, 320, 240)
w.scale(0, 24318, 25058, bgs+.01, bgs)
w.moveY(0, 24318, 24410, 720, 240)
w.fade(6, 24318, 25058, 1, 0)


# Verse 1 + prechorus
h = scene("h")
h.scale(0, 25058, 25058, .48, .48)
h.fade(0, 25058, 25799, 0, 1)
h.moveX(0, 25058, 37651, 340, 300)

d = scene("d")
d.scale(0, 36910, 36910, .48, .48)
d.fade(0, 36910, 37651, 0, 1)
d.moveX(0, 36910, 49132, 340, 300)

x = scene("x1")
x.fade(0, 48762, 49132, 0, 1)
x.scale(0, 48762, 60984, 0.48, bgs)

z = scene("z")
z.fade(0, 60614, 60984, 0, 1)
z.scale(0, 60614, 65799, 0.46, bgs)
z.fade(0, 64873, 65799, 1, 0)


# Chorus 1
v = scene("v")
v.scale(0, 66540, 79132, .48, .48)
v.fade(0, 66540, 67281, 0, 1)
v.moveX(0, 66540, 79132, 340, 300)
v.moveY(0, 66540, 79132, 230, 240)

b = scene("b")
b.scale(0, 78392, 90984, .48, .48)
b.fade(0, 78392, 79132, 0, 1)
b.moveX(0, 78392, 90984, 340, 300)

c = scene("c")
c.scale(0, 90244, 90244, .48, .48)
c.fade(0, 90244, 90984, 0, 1)
c.moveX(0, 90244, 96169, 330, 310)

y = scene("y")
y.scale(0, 96169, 96262, 1.5, .48)
y.scale(0, 96262, 99503, .48, bgs)
y.fade(0, 96169, 96355, 0, 1)
y.fade(3, 98577, 99132, 1, 0)


# Post chorus 1
p = scene("p")
p.scale(0, 99132, 99132, .48, .48)
p.fade(0, 99132, 100614, 0, 1)
p.moveX(0, 99132, 108021, 300, 340)

c = scene("c")
c.scale(0, 108021, 108114, 1, bgs+.01)
c.scale(0, 108114, 108577, bgs+.01, bgs)
# c.fade(6, 108114, 108577, 1, 0)
c.fade(0, 108021, 108206, 0, 1)

b = scene("b")
b.scale(0, 108577, 108669, 1, bgs+.01)
b.scale(0, 108669, 109132, bgs+.01, bgs)
# b.fade(6, 108669, 109132, 1, 0)
b.fade(0, 108577, 108762, 0, 1)

v = scene("v")
v.scale(0, 109132, 109225, 1, bgs+.01)
v.scale(0, 109225, 109688, bgs+.01, bgs)
# v.fade(6, 109225, 109688, 1, 0)
v.fade(0, 109132, 109318, 0, 1)

a = scene("a")
a.scale(0, 109688, 109781, 1, bgs+.01)
a.scale(0, 109781, 110336, bgs+.01, bgs)
# a.fade(0, 110151, 110336, 1, 0)
# a.moveY(0, 110244, 110336, 240, -240)
a.fade(0, 109688, 109873, 0, 1)

w = osbject(sc+"w.png", bkg, ctr, 320, 240)
w.scale(0, 110244, 110984, bgs+.01, bgs)
w.moveY(0, 110244, 110336, 720, 240)
w.fade(6, 110244, 110984, 1, 0)


# Verse 2 + prechorus
u = scene("u")
u.scale(0, 110984, 123577, .48, bgs)
u.fade(0, 110984, 111725, 0, 1)

e = scene("e")
e.scale(0, 122836, 122836, .48, .48)
e.fade(0, 122836, 123577, 0, 1)
e.moveX(0, 122836, 135058, 340, 300)

x = scene("x")
x.scale(0, 134688, 146910, .48, bgs)
x.fade(0, 134688, 135058, 0, 1)

z = scene("z1")
z.fade(0, 146540, 146910, 0, 1)
z.scale(0, 146540, 151725, .46, bgs)
z.fade(0, 150799, 151725, 1, 0)


# Chorus 2
g = scene("g")
g.scale(0, 152466, 152466, .48, .48)
g.fade(0, 152466, 153206, 0, 1)
g.moveX(0, 152466, 165058, 340, 300)

f = scene("f")
f.scale(0, 164318, 164318, .48, .48)
f.fade(0, 164318, 165058, 0, 1)
f.moveX(0, 164318, 176910, 340, 300)

i = scene("i")
i.scale(0, 176169, 176169, .48, .48)
i.fade(0, 176169, 176910, 0, 1)
i.moveX(0, 176169, 182095, 330, 310)

a = scene("aa")
a.scale(0, 182095, 182188, 1.5, .48)
a.scale(0, 182188, 185058, .48, bgs)
a.fade(0, 182095, 182281, 0, 1)
a.fade(3, 184503, 185058, 1, 0)


# Bridge
k = scene("k")
k.scale(0, 185058, 185058, bgs, bgs)
k.fade(0, 185058, 185799, 0, 1)
k.moveX(0, 185058, 196910, 360, 320)
k.fade(0, 195429, 196910, 1, 0)

j = scene("j")
j.fade(0, 196910, 197651, 0, 1)
j.scale(0, 196910, 208762, .48, bgs)
j.fade(0, 208021, 208762, 1, 0)

s = scene("s")
s.scale(0, 208762, 208762, .47, .47)
s.fade(0, 208762, 209503, 0, 1)
s.moveX(0, 208762, 221355, 340, 300)

t = scene("t")
t.scale(0, 220614, 220614, .47, .47)
t.fade(0, 220614, 221355, 0, 1)
t.moveX(0, 220614, 232466, 340, 300)
t.fade(0, 231725, 232466, 1, 0)


# Prechorus 3
b = scene("ab")
b.scale(0, 232466, 232466, .48, .48)
b.fade(0, 232466, 233206, 0, 1)
b.moveX(0, 232466, 243577, 340, 300)

b = scene("ab1")
b.scale(0, 232466, 232466, .48, .48)
b.fade(0, 238392, 238762, 0, 1)
b.moveX(0, 232466, 243577, 340, 300)

c = scene("ac")
c.scale(0, 243392, 245244, bgs, bgs)
c.fade(0, 243392, 243577, 0, 1)
# c.fade(0, 245614, 245984, 1, 0)

# c0 = scene("ac0")
# c0.scale(0, 243392, 244132, bgs, bgs)
# c0.fade(0, 243392, 243577, 0, 1)

c1 = scene("ac1")
c1.scale(0, 243947, 244688, bgs, bgs)
c1.fade(0, 243947, 244132, 0, 1)

c2 = scene("ac2")
c2.scale(0, 244503, 245244, bgs, bgs)
c2.fade(0, 244503, 244688, 0, 1)

c3 = scene("ac3")
c3.scale(0, 245058, 245984, bgs, bgs)
c3.fade(0, 245058, 245244, 0, 1)
c3.fade(0, 245614, 245984, 1, 0)

# Chorus 3
# First two scenes flipped because layering since m isn't a full size image
m = scene("m")
m.scale(0, 259688, 271725, .6, .6)
m.moveY(0, 259688, 271725, 180, 300)
# m.fade(0, 259688, 260429, 0, 1)

l = scene("l")
l.scale(0, 247281, 247281, bgs, bgs)
l.fade(0, 247281, 248021, 0, 1)
l.moveY(0, 247281, 260429, 200, 280)
l.fade(0, 259688, 260429, 1, 0)

n = scene("n")
n.scale(0, 270984, 270984, .48, .48)
n.fade(0, 270984, 271725, 0, 1)
n.moveX(0, 270984, 283577, 340, 300)

o = scene("o", 320, 60)
# o.scale(0, 282836, 282836, .8, .8)
o.fade(0, 282836, 283577, 0, 1)
o.moveX(0, 282836, 288762, 340, 300)
# o.fade(0, 287836, 288392, 1, 0)

o = scene("o")
o.scale(0, 288762, 288855, 1.5, .48)
o.scale(0, 288855, 291725, .48, bgs)
o.fade(0, 288762, 288947, 0, 1)
o.fade(3, 291169, 291725, 1, 0)


# Outro
p = scene("p1")
p.scale(0, 294688, 299873, 0.5, bgs)
p.fade(0, 294688, 295429, 0, 1)

# Trial and error to match scales of the two images
qm = .073
q = scene("q")
q.scale(0, 299132, 306540, 0.5+qm, .46)
q.fade(0, 299132, 299873, 0, 1)
q.fade(0, 305799, 306540, 1, 0)

r = scene("r")
r.scale(0, 306540, 309503, 0.45, bgs)
r.fade(0, 306540, 307095, 0, 1)
r.fade(0, 309132, 309503, 1, 0)


### Fighto

# Parameters
chL = 0      # Left co-ord
chR = 640    # Right co-ord
chD = 440    # Dip distance

# Heights of each fighto
c0 = 372
c1 = 364
c2 = 380
c3 = 388
c4 = 380
c5 = 385
c6 = 380
c7 = 387

# Prechorus 1
c = osbject("sb/ch0.png", bkg, ctr, chL, 560)
c.scale(0, 50799, 50799, bgs, bgs)
c.moveY(0, 50799, 50984, 610, c0)
c.moveY(0, 50984, 51169, c0, chD)
c.moveY(0, 51169, 51355, chD, c0)
c.moveY(0, 51355, 51540, c0, 610)

c = osbject("sb/ch1.png", bkg, ctr, chR, 560)
c.scale(0, 50799, 50799, bgs, bgs)
c.moveY(0, 50799, 50984, 610, c1)
c.moveY(0, 50984, 51169, c1, chD)
c.moveY(0, 51169, 51355, chD, c1)
c.moveY(0, 51355, 51540, c1, 610)

c = osbject("sb/ch2.png", bkg, ctr, chL, 560)
c.scale(0, 53762, 53762, bgs, bgs)
c.moveY(0, 53762, 53947, 610, c2)
c.moveY(0, 53947, 54132, c2, chD)
c.moveY(0, 54132, 54318, chD, c2)
c.moveY(0, 54318, 54503, c2, 610)

c = osbject("sb/ch3.png", bkg, ctr, chR, 560)
c.scale(0, 53762, 53762, bgs, bgs)
c.moveY(0, 53762, 53947, 610, c3)
c.moveY(0, 53947, 54132, c3, chD)
c.moveY(0, 54132, 54318, chD, c3)
c.moveY(0, 54318, 54503, c3, 610)

c = osbject("sb/ch4.png", bkg, ctr, chL, 560)
c.scale(0, 56725, 56725, bgs, bgs)
c.moveY(0, 56725, 56910, 610, c4)
c.moveY(0, 56910, 57095, c4, chD)
c.moveY(0, 57095, 57281, chD, c4)
c.moveY(0, 57281, 57466, c4, 610)

c = osbject("sb/ch5.png", bkg, ctr, chR, 560)
c.scale(0, 56725, 56725, bgs, bgs)
c.moveY(0, 56725, 56910, 610, c5)
c.moveY(0, 56910, 57095, c5, chD)
c.moveY(0, 57095, 57281, chD, c5)
c.moveY(0, 57281, 57466, c5, 610)

c = osbject("sb/ch6.png", bkg, ctr, chL, 560)
c.scale(0, 59688, 59688, bgs, bgs)
c.moveY(0, 59688, 59873, 610, c6)
c.moveY(0, 59873, 60058, c6, chD)
c.moveY(0, 60058, 60244, chD, c6)
c.moveY(0, 60244, 60429, c6, 610)

c = osbject("sb/ch7.png", bkg, ctr, chR, 560)
c.scale(0, 59688, 59688, bgs, bgs)
c.moveY(0, 59688, 59873, 610, c7)
c.moveY(0, 59873, 60058, c7, chD)
c.moveY(0, 60058, 60244, chD, c7)
c.moveY(0, 60244, 60429, c7, 610)


# Prechorus 2
c = osbject("sb/ch6.png", bkg, ctr, chL, 560)
c.scale(0, 136725, 136725, bgs, bgs)
c.moveY(0, 136725, 136910, 610, c6)
c.moveY(0, 136910, 137095, c6, chD)
c.moveY(0, 137095, 137281, chD, c6)
c.moveY(0, 137281, 137466, c6, 610)

c = osbject("sb/ch7.png", bkg, ctr, chR, 560)
c.scale(0, 136725, 136725, bgs, bgs)
c.moveY(0, 136725, 136910, 610, c7)
c.moveY(0, 136910, 137095, c7, chD)
c.moveY(0, 137095, 137281, chD, c7)
c.moveY(0, 137281, 137466, c7, 610)

c = osbject("sb/ch4.png", bkg, ctr, chL, 560)
c.scale(0, 139688, 139688, bgs, bgs)
c.moveY(0, 139688, 139873, 610, c4)
c.moveY(0, 139873, 140058, c4, chD)
c.moveY(0, 140058, 140244, chD, c4)
c.moveY(0, 140244, 140429, c4, 610)

c = osbject("sb/ch5.png", bkg, ctr, chR, 560)
c.scale(0, 139688, 139688, bgs, bgs)
c.moveY(0, 139688, 139873, 610, c5)
c.moveY(0, 139873, 140058, c5, chD)
c.moveY(0, 140058, 140244, chD, c5)
c.moveY(0, 140244, 140429, c5, 610)

c = osbject("sb/ch2.png", bkg, ctr, chL, 560)
c.scale(0, 142651, 142651, bgs, bgs)
c.moveY(0, 142651, 142836, 610, c2)
c.moveY(0, 142836, 143021, c2, chD)
c.moveY(0, 143021, 143206, chD, c2)
c.moveY(0, 143206, 143392, c2, 610)

c = osbject("sb/ch3.png", bkg, ctr, chR, 560)
c.scale(0, 142651, 142651, bgs, bgs)
c.moveY(0, 142651, 142836, 610, c3)
c.moveY(0, 142836, 143021, c3, chD)
c.moveY(0, 143021, 143206, chD, c3)
c.moveY(0, 143206, 143392, c3, 610)

c = osbject("sb/ch0.png", bkg, ctr, chL, 560)
c.scale(0, 145614, 145614, bgs, bgs)
c.moveY(0, 145614, 145799, 610, c0)
c.moveY(0, 145799, 145984, c0, chD)
c.moveY(0, 145984, 146169, chD, c0)
c.moveY(0, 146169, 146355, c0, 610)

c = osbject("sb/ch1.png", bkg, ctr, chR, 560)
c.scale(0, 145614, 145614, bgs, bgs)
c.moveY(0, 145614, 145799, 610, c1)
c.moveY(0, 145799, 145984, c1, chD)
c.moveY(0, 145984, 146169, chD, c1)
c.moveY(0, 146169, 146355, c1, 610)


### Lyrics

# Read lyrics file, gets list of lines
with open("lyrics.txt", "r", encoding="utf8") as f:
    lyrics = f.readlines()

# Read times file, gets list of times as [start, end, position]
with open("times.txt", "r") as f:
    times = []
    for i in f:
        times.append([int(x) for x in i.split()])

characters = getCharacters()

# Lyrics parameters
x0 = 20           # Origin x pos for type 0
y0 = 368          # Origin y pos for type 0
x1 = 120          # Origin x pos for type 1
y1 = 400          # Origin y pos for type 1
spacing = 27      # Spacing between each character
cSz = .35         # Size
cVel = .005       # Horizontal velocity of the line
# cdY = 5           # Vertical movement for fade in/out
# cdR = 0.2         # Rotational movement for fade in/out
fadeTime = 500    # Fade time
fadeDelay = 50    # Delay between each character
adj = 200         # Start/end time adjustment

# Iterate through each character in the lyrics and position/animate accordingly
for i in range(len(lyrics)):
    lineLen = len(lyrics[i])
    offset = 0

    for j in range(len(lyrics[i])):
        # Get character and related stuff
        char = lyrics[i][j]

        # Ignore characters which aren't actually characters
        try:
            charIndex = characters.index(char)
        except ValueError:
            continue

        charFile = "sb/lyrics/{}.png".format(charIndex)

        # Space depending on position in line
        cX = spacing * j
        cD = fadeDelay * j

        # Get y position for character
        if times[i][2] == 0:
            cX += x0
            cY = y0
        else:
            cX += x1
            cY = y1

        # Get time for character
        cStart = times[i][0] + cD - adj
        cEnd = times[i][1] + cD - adj
        time = (cEnd + fadeTime) - cStart # Total active time

        # Get translation based on active time and velocity
        cMve = time * cVel

        # Place in SB
        c = osbject(charFile, "Foreground", ctr, cX, cY)
        c.scale(0, cStart, cEnd, cSz, cSz)
        c.fade(0, cStart, cStart+fadeTime, 0, 1)
        c.fade(0, cEnd, cEnd+fadeTime, 1, 0)
        c.moveX(0, cStart, cEnd+fadeTime, cX, cX+cMve)
        # c.moveY(0, cStart, cStart+fadeTime, cY-cdY, cY)
        # c.moveY(0, cEnd, cEnd+fadeTime, cY, cY-cdY)
        # c.rotate(0, cStart, cStart+fadeTime, -cdR, 0)
        # c.rotate(0, cEnd, cEnd+fadeTime, 0, cdR)


### Outro petals

endOfSB = 309503

# Petals parameters
minP = 3          # Minimum number of petals per spawn
maxP = 5          # Maximum number of petals per spawn
delayP = 550      # Time between each spawn cycle
minSzP = 20       # Minimum petal size (*E-2)
maxSzP = 50       # Maximum petal size (*E-2)
minVelP = 100     # Minimum petal velocity (*E-3)
maxVelP = 200     # Maximum petal velocity (*E-3)
maxrVelP = 100    # Maximum petal rotational velocity (*E-5)
maxScP = 10       # Maximum petal x scaling (*E-1)
minScP = -10      # Minimum petal x scaling (*E-1)
yMve = 10         # Vertical displacement

# Iterate through each spawn cycle and animate petals
for i in range(288762, 309132, delayP):
    petals = randint(2, 4)
    for j in range(petals):
        pY = randint(0, 470) # Generate random y position
        pSz = float(randint(minSzP, maxSzP) * .01) # Generate random size
        pVel = float(randint(minVelP, maxVelP) * .001) # Generate random velocity
        pR = float(randint(0, 314) * .01) # Generate random start rotation
        pVelR = float(randint(-maxrVelP, maxrVelP) * .00001) # Generate random end rotation
        pSc = float(randint(0, maxScP) * .1) # Generate random x vector scaling
        pSc2 = float(randint(minScP, maxScP) * .1) # Generate another random x vector scaling

        timeToCross = round(900/pVel) # Time for petal to cross horizontal length of SB

        # If petal can't cross in time, fade it out early but keep velocity consistent
        if i + timeToCross > endOfSB:
            pEnd = endOfSB
            isCut = True

        # Otherwise let it cross and despawn when it reaches the end
        else:
            pEnd = i + timeToCross
            isCut = False

        # Calculate active time and displacements
        pTime = pEnd - i
        pdX = -pTime * pVel
        pdR = pTime * pVelR
        pdY = (pTime / timeToCross) * 10

        # Place in SB
        p = osbject("sb/petal.png", bkg, ctr, 780, pY)
        # p.para(0, i, i, "A")
        p.fade(0, i, i, 0.8, 0.8)
        p.vecscale(0, i, pEnd, pSz-pSc, pSz, pSz+pSc2, pSz)
        p.rotate(0, i, pEnd, pR, pR+pdR)
        p.moveX(0, i, pEnd, 780, 780+pdX)
        p.moveY(0, i, pEnd, pY, pY+pdY)
        p.colour(0, i, i, 244, 223, 223, 244, 223, 223)

        if isCut:
            p.fade(0, 309132, 309503, 1, 0)


## Credits

# Parameters
startX = -400
dly = 50
x0 = 0
y0 = 64
x1 = 42
y1 = 88
mve = 20

c = osbject("sb/honeyworks.png", bkg, "CentreLeft", x0, y0)
c.scale(0, 13114, 13114, 0.4, 0.4)
c.moveX(0, 13114, 13207, startX, x0)
c.moveX(0, 13207, 14595, x0, x0+mve)
c.moveX(0, 14595, 14688, x0+mve, 780)

c = osbject("sb/guitar.png", bkg, "CentreLeft", x0, y0)
c.scale(0, 14595, 14595, 0.4, 0.4)
c.moveX(0, 14595, 14688, startX, x0)
c.moveX(0, 14688, 16077, x0, x0+mve)
c.moveX(0, 16077, 16169, x0+mve, 780)

c = osbject("sb/bass.png", bkg, "CentreLeft", x1, y1)
c.scale(0, 14595, 14595, 0.4, 0.4)
c.moveX(0, 14595+dly, 14688+dly, startX, x1)
c.moveX(0, 14688+dly, 16077+dly, x1, x1+mve)
c.moveX(0, 16077+dly, 16169+dly, x1+mve, 780)

c = osbject("sb/piano.png", bkg, "CentreLeft", x0, y0)
c.scale(0, 16077, 16077, 0.4, 0.4)
c.moveX(0, 16077, 16169, startX, x0)
c.moveX(0, 16169, 17558, x0, x0+mve)
c.moveX(0, 17558, 17651, x0+mve, 780)

c = osbject("sb/drums.png", bkg, "CentreLeft", x1, y1)
c.scale(0, 16077, 16077, 0.4, 0.4)
c.moveX(0, 16077+dly, 16169+dly, startX, x1)
c.moveX(0, 16169+dly, 17558+dly, x1, x1+mve)
c.moveX(0, 17558+dly, 17651+dly, x1+mve, 780)

c = osbject("sb/stringsArr.png", bkg, "CentreLeft", x0, y0)
c.scale(0, 17558, 17558, 0.4, 0.4)
c.moveX(0, 17558, 17651, startX, x0)
c.moveX(0, 17651, 19040, x0, x0+mve)
c.moveX(0, 19040, 19132, x0+mve, 780)

c = osbject("sb/strings.png", bkg, "CentreLeft", x1, y1)
c.scale(0, 17558, 17558, 0.4, 0.4)
c.moveX(0, 17558+dly, 17651+dly, startX, x1)
c.moveX(0, 17651+dly, 19040+dly, x1, x1+mve)
c.moveX(0, 19040+dly, 19132+dly, x1+mve, 780)

c = osbject("sb/illust.png", bkg, "CentreLeft", x0, y0)
c.scale(0, 19040, 19040, 0.4, 0.4)
c.moveX(0, 19040, 19132, startX, x0)
c.moveX(0, 19132, 20521, x0, x0+mve)
c.moveX(0, 20521, 20614, x0+mve, 780)

c = osbject("sb/movie.png", bkg, "CentreLeft", x0, y0)
c.scale(0, 20521, 20521, 0.4, 0.4)
c.moveX(0, 20521, 20614, startX, x0)
c.moveX(0, 20614, 22003, x0, x0+mve)
c.moveX(0, 22003, 22095, x0+mve, 780)

# Write SB to map folder
with open ("loc.txt", "r") as f:
    loc = f.readline().rstrip()

osbject.end(loc + "\\HoneyWorks meets TrySail - Senpai. (-Mo-).osb")
