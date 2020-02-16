from __future__ import print_function, division
from builtins import *
from osbpy import *
from math import pi
from random import randint, uniform, choice

### Background stuff ###

# Thank you message
# Also the same as lyrics (moved here for layering)

tylens = [18, 11]

with open("ty.csv", "r") as f:
    tys = []
    for i in f:
        tys.append([x for x in i.split()])

tyxr, tyyr = 320, 280
tylen = 0
tyline = 0
tystartsx = [-20, 0, 20]
tystartsy = [-20, 20]

tysx = -1
tysy = -1
tyx_last = -1
tyy_last = -1

for i in range(len(tys)):
    if tylen == tylens[tyline]:
        tyyr += 50
        tylen = 1
    else:
        tylen += 1

    tyc = tys[i][0]
    tyx = tyxr+float(tys[i][1])
    tyy = tyyr+float(tys[i][2])

    # Make it so the same start positions don't happen
    while tysx == tyx_last:
        tysx = choice(tystartsx)
    tyx_last = tysx
    tysy = choice(tystartsy)

    t = osbject("sb/t/{}.png".format(tyc), "Background", "TopLeft", tyx, tyy)
    t.move(0,234366,235140,tyx+tysx,tyy+tysy,tyx,tyy)
    t.fade(1,236979,237076,1,0)
    t.scale(0,234366,234366,0.5,0.5)

# Just some simple fades and toggling for the main BG
bgs = 480/1080 # 1080p into SB size

bg = osbject("yamabg.jpg", "Background", "Centre", 320,240)
bg.scale(0,6753,221979,bgs,bgs)
bg.fade(0,221979,221979,1,0)

# Basic fade and toggle for the sunset
sunset = osbject("sb/sunset.jpg", "Background", "Centre", 320, 240)
sunset.scale(0,0,0,0.47,0.47)
sunset.fade(0,0,1334,0,1)
sunset.moveY(0,0,6753,240,230)

sunset = osbject("sb/sunset.jpg", "Background", "Centre", 320, 240)
sunset.scale(0,234366,234366,0.47,0.47)
sunset.fade(0,228172,228172,1,0)
sunset.moveY(0,221979,235140,250,230)

sunsetb = osbject("sb/sunsetb.jpg", "Background", "Centre", 320, 240)
sunsetb.scale(0,234366,234366,0.47,0.47)
sunsetb.fade(0,228172,228172,0,1)
sunsetb.fade(0,234366,235140,1,0)
sunsetb.moveY(0,221979,235140,250,230)

### Background stuff ###

# Logos
cath = osbject("sb/catharsis.png", "Background", "Centre", 160, 200)
cath.scale(0,6753,6753,0.5,0.5)
#cath.para(0,0,0,"A")

cath.fade(0,0,1334,0,1)
cath.fade(0,6753,6753,1,0)
cath.fade(0,221979,221979,0,1)
cath.fade(0,236979,237076,1,0)

frac = osbject("sb/fractal.png", "Background", "Centre", 480, 200)
frac.scale(0,6753,6753,0.5,0.5)
#frac.para(0,0,0,"A")

frac.fade(0,0,1334,0,1)
frac.fade(0,6753,6753,1,0)
frac.fade(0,221979,221979,0,1)
frac.fade(0,236979,237076,1,0)

# Date
# Functions to generate each number with their relative positions
#nadx, nady = 0, 0 # Nudge shadows
def zero(px, py):
    #zeros = osbject("sb/n/glow/0030.png", "Background", "TopLeft", px-11.5+nadx, py+6+nady)
    zero = osbject("sb/n/0030.png", "Background", "TopLeft", px-9-7, py+8.5-7)
    return zero#, zeros
def one(px, py):
    #ones = osbject("sb/n/glow/0031.png", "Background", "TopLeft", px-8+nadx, py+6+nady)
    one = osbject("sb/n/0031.png", "Background", "TopLeft", px-5.5-7, py+8-7)
    return one#, ones
def two(px, py):
    #twos = osbject("sb/n/glow/0032.png", "Background", "TopLeft", px-12+nadx, py+6+nady)
    two = osbject("sb/n/0032.png", "Background", "TopLeft", px-9-7, py+8.5-7)
    return two#, twos
def three(px, py):
    #threes = osbject("sb/n/glow/0033.png", "Background", "TopLeft", px-11+nadx, py+6+nady)
    three = osbject("sb/n/0033.png", "Background", "TopLeft", px-9-7, py+8.5-7)
    return three#, threes
def four(px, py):
    #fours = osbject("sb/n/glow/0034.png", "Background", "TopLeft", px-12.5+nadx, py+6+nady)
    four = osbject("sb/n/0034.png", "Background", "TopLeft", px-10-7, py+8-7)
    return four#, fours
def five(px, py):
    #fives = osbject("sb/n/glow/0035.png", "Background", "TopLeft", px-10.5+nadx, py+6.5+nady)
    five = osbject("sb/n/0035.png", "Background", "TopLeft", px-8.5-7, py+9-7)
    return five#, fives
def six(px, py):
    #sixs = osbject("sb/n/glow/0036.png", "Background", "TopLeft", px-11+nadx, py+6+nady)
    six = osbject("sb/n/0036.png", "Background", "TopLeft", px-8.5-7, py+8-7)
    return six#, sixs
def seven(px, py):
    #sevens = osbject("sb/n/glow/0037.png", "Background", "TopLeft", px-11+nadx, py+6.5+nady)
    seven = osbject("sb/n/0037.png", "Background", "TopLeft", px-9-7, py+9-7)
    return seven#, sevens
def eight(px, py):
    #eights = osbject("sb/n/glow/0038.png", "Background", "TopLeft", px-10.5+nadx, py+6+nady)
    eight = osbject("sb/n/0038.png", "Background", "TopLeft", px-8-7, py+8.5-7)
    return eight#, eights
def nine(px, py):
    #nines = osbject("sb/n/glow/0039.png", "Background", "TopLeft", px-11+nadx, py+6+nady)
    nine = osbject("sb/n/0039.png", "Background", "TopLeft", px-9-7, py+8.5-7)
    return nine#, nines

# Place four numbers in the centre with some spacing between them
# This one is for the intro, the easy one
spc = 30 # Spacing
dx = 320 # Relative to line
dy = 180
scle = 0.35

# Slot 1
s1x = dx - (spc * 1.5)
s1 = one(s1x,dy)

s1.fade(0,0,1334,0,1)
s1.scale(0,6753,6753,scle,scle)
#s1.para(0,6753,6753,"A")

# Slot 2
s2x = dx - (spc * 0.5)
s2 = nine(s2x,dy)

s2.fade(0,0,1334,0,1)
s2.scale(0,6753,6753,scle,scle)
#s2.para(0,6753,6753,"A")

# Slot 3
s3x = dx + (spc * 0.5)
s3 = four(s3x,dy)

s3.fade(0,0,1334,0,1)
s3.scale(0,6753,6753,scle,scle)
#s3.para(0,6753,6753,"A")

# Slot 4
s4x = dx + (spc * 1.5)
s4 = five(s4x,dy)

s4.fade(0,0,1334,0,1)
s4.scale(0,6753,6753,scle,scle)
#s4.para(0,6753,6753,"A")

# Start at 1945 from 221979
# Then start scrolling through the numbers at 229721 until 232818
# Ending at 2016
# Scrolling speed should decelerate
def slot_1(number, ts, te):
    s1x = dx - (spc * 1.5)
    s1 = number(s1x,dy)
    s1.scale(0,ts,te,scle,scle)

def slot_2(number, ts, te):
    s2x = dx - (spc * 0.5)
    s2 = number(s2x,dy)
    s2.scale(0,ts,te,scle,scle)

def slot_3(number, ts, te):
    s3x = dx + (spc * 0.5)
    s3 = number(s3x,dy)
    s3.scale(0,ts,te,scle,scle)

def slot_4(number, ts, te):
    s4x = dx + (spc * 1.5)
    s4 = number(s4x,dy)
    s4.scale(0,ts,te,scle,scle)

# Make a counter for each slot and assign each digit to a number function
#number0 = [0, zero]
#number1 = [1, one]
#number2 = [2, two]
#number3 = [3, three]

# Calculate the times when the numbers change
datetime = 228559
daten = 1945
datedelay = 0
switchslot1 = []
switchslot2 = []
switchslot3 = []
switchslot4 = []
for i in range(2016-1945+1):
    # +1 is a bodge, for some reason it goes 1999, 1990, 2001
    switchslot4.append(datetime)
    if daten%10 == 0:
        switchslot3.append(datetime)
    if daten%100 == 0:
        switchslot2.append(datetime)
    if daten%1000 == 0:
        switchslot1.append(datetime)
    datedelay += 2
    datetime += 3 + datedelay
    daten += 1

s4n = 5
s3n = 4
s2n = 9
s1n = 1
slot3i = 0

for i in range(len(switchslot4)):
    #s4n += 1
    switchstart = switchslot4[i]
    if s4n == 10:
        # Cycle back to 0
        s4n = 0
        s3n += 1
        if s3n == 10:
            s3n = 0
            s2n = 0
    # Slot 4
    if switchstart == switchslot4[-1]:
        # Check if it's the final number
        switchend = 236979
    else:
        switchend = switchslot4[i+1]
    if s4n == 0:
        slot_4(zero,switchstart,switchend)
    elif s4n == 1:
        slot_4(one,switchstart,switchend)
    elif s4n == 2:
        slot_4(two,switchstart,switchend)
    elif s4n == 3:
        slot_4(three,switchstart,switchend)
    elif s4n == 4:
        slot_4(four,switchstart,switchend)
    elif s4n == 5:
        slot_4(five,switchstart,switchend)
    elif s4n == 6:
        slot_4(six,switchstart,switchend)
    elif s4n == 7:
        slot_4(seven,switchstart,switchend)
    elif s4n == 8:
        slot_4(eight,switchstart,switchend)
    elif s4n == 9:
        slot_4(nine,switchstart,switchend)
    # Slot 3
    if switchstart in switchslot3:
        if switchstart == switchslot3[-1]:
            # Check if it's the final number
            switchend = 236979
        else:
            slot3i += 1
            switchend = switchslot3[slot3i]
        if s3n == 0:
            slot_3(zero,switchstart,switchend)
        elif s3n == 1:
            slot_3(one,switchstart,switchend)
        elif s3n == 5:
            slot_3(five,switchstart,switchend)
        elif s3n == 6:
            slot_3(six,switchstart,switchend)
        elif s3n == 7:
            slot_3(seven,switchstart,switchend)
        elif s3n == 8:
            slot_3(eight,switchstart,switchend)
        elif s3n == 9:
            slot_3(nine,switchstart,switchend)
    # Slot 2
    if switchstart == switchslot2[-1]:
        # Check if it's the final number
        switchend = 236979
    if switchstart in switchslot2:
        slot_2(zero,switchstart,switchend)
    if switchstart in switchslot1:
        slot_1(two,switchstart,switchend)
    s4n += 1

# Before and after the switch
# Slot 1
s1x = dx - (spc * 1.5)
s1 = one(s1x,dy)
s1.scale(0,221979,switchslot1[0],scle,scle)

s1 = two(s1x,dy)
s1.scale(0,236979,236979,scle,scle)
s1.fade(0,236979,237076,1,0)

# Slot 2
s2x = dx - (spc * 0.5)
s2 = nine(s2x,dy)
s2.scale(0,221979,switchslot2[0],scle,scle)

s2 = zero(s2x,dy)
s2.scale(0,236979,236979,scle,scle)
s2.fade(0,236979,237076,1,0)

# Slot 3
s3x = dx + (spc * 0.5)
s3 = four(s3x,dy)
s3.scale(0,221979,switchslot3[0],scle,scle)

s3 = one(s3x,dy)
s3.scale(0,236979,236979,scle,scle)
s3.fade(0,236979,237076,1,0)

# Slot 4
s4x = dx + (spc * 1.5)
s4 = five(s4x,dy)
s4.scale(0,221979,switchslot4[0],scle,scle)

s4 = six(s4x,dy)
s4.scale(0,236979,236979,scle,scle)
s4.fade(0,236979,237076,1,0)

# Credits
# This part should follow similar rules to the lyrics
# Import the list from charlist.csv
with open("creditslist.csv", "r") as f:
    creds = []
    for i in f:
        creds.append([x for x in i.split()])

# Initial parameters for the credits
credlens = [15, 11, 16, 17, 12]
credstarts = [6753, 8301, 9850, 11398, 12947]
credx = [434, 518, 485, 472, 536]
credy = 290

creddelay = 50
credlen = 0
credline = 0

for i in range(len(creds)):
    if credlen != credlens[credline]:
        credstart = credstarts[credline]+creddelay*(credlen)
        credlen += 1
    else:
        credline += 1
        credstart = credstarts[credline]
        credlen = 1

    cred = creds[i][0]
    crex = credx[credline]+float(creds[i][1])
    crey = credy+(30*credline)+float(creds[i][2])
    credexit = 17592+creddelay*(credlen)

    d = osbject("sb/g/{}.png".format(cred), "Background", "TopLeft", crex, crey)
    d.scale(0,credstart,credstart,0.5,0.5)
    d.moveX(30,credstart,credstart+500,crex-700,crex)
    d.moveX(0,credexit,credexit+500,crex,crex+700)

# Orbs
# Generate some number of orbs per cycle
# Random location around the bottom
# Float up and to the right slightly
def orbs(oixl,oixh,ofyl,ofyh,ti,tf):
    for i in range(ti,tf):
        if i%800 == 0:
            dupe = randint(2,4)
            for j in range(dupe):
                # Initial and final states
                ox = randint(oixl,oixh)
                oy = 520
                otime = randint(2000,3000)
                osway = randint(100,180)
                ofy = randint(ofyl,ofyh)
                oscale = round(uniform(0.05,0.15),2)
                ocolour = randint(0,2)

                # Generate
                o = osbject("sb/orb.png", "Background", "Centre", ox, oy)

                o.moveX(4,i,i+otime,ox,ox+osway)
                o.moveY(15,i,i+otime,oy,ofy)

                #o.scale(0,i,i,oscale,oscale)

                #o.fade(0,i+otime-250,i+otime,0.5,0)

                o.para(0,i,i,"A")

                # Colours
                # If after 228172 change colour palette
                if i+otime < 228172:
                    if ocolour == 0:
                        o.colour(0,i,i,237,126,27,237,126,27)
                    elif ocolour == 1:
                        o.colour(0,i,i,237,27,27,237,27,27)
                    else:
                        o.colour(0,i,i,237,205,27,237,205,27)
                else:
                    if ocolour == 0:
                        o.colour(0,228172,228172,237,126,27,255,255,255)
                    elif ocolour == 1:
                        o.colour(0,228172,228172,237,27,27,255,255,255)
                    else:
                        o.colour(0,228172,228172,237,205,27,90,220,255)

                # Check if at the start or at the end
                if i <= 1334:
                    #if i+otime < 1334:
                        # Edge case for fade in overlapping fade out
                        #fout = 1334
                    # Fade in with BG
                    o.fade(0,0,1334,0,0.5)
                    o.fade(15,i+otime-500,i+otime,0.5,0)
                    o.scale(0,i+otime-500,i+otime,oscale,0)
                elif 20000 >= i+otime >= 6753:
                    # Kill at the whiteout
                    o.fade(15,6753-500,6753,0.5,0)
                    o.scale(0,6753-500,6753,oscale,0)
                elif 20000 <= i <= 221979:
                    # Outro in
                    o.fade(0,221979,221979,0,0.5)
                    if i+otime-500 < 221979:
                        # Edge case
                        o.fade(15,221979,i+otime,0.5,0)
                        o.scale(0,221979,i+otime,oscale,0)
                    else:
                        o.fade(15,i+otime-500,i+otime,0.5,0)
                        o.scale(0,i+otime-500,i+otime,oscale,0)
                elif i+otime >= 235140:
                    # Outro fade
                    o.fade(15,234366-500,235140,0.5,0)
                    o.scale(0,234366-500,235140,oscale,0)
                else:
                    # Standard fade
                    o.fade(15,i+otime-500,i+otime,0.5,0)
                    o.scale(0,i+otime-500,i+otime,oscale,0)

# Intro
orbs(-260,-70,-60,180,-1000,5205)
orbs(420,610,-10,180,-1000,5205)
orbs(-60,420,200,300,-1000,5205)

# Outro
orbs(-260,-70,-60,180,219656,234366)
orbs(420,610,-10,180,219656,234366)
orbs(-60,420,200,300,219656,234366)

# Petals
# Generate some number of petals per cycle
# Petals rotate random amount 'dupe' and scale periodically at random frequency
# Random size
for i in range(-1500,221979):
    if i%750 == 0:
        dupe = randint(2,4)
        yrng = 600
        ydrng = yrng/dupe
        dupec = 0
        for j in range(dupe):
            # Initial and final states
            px = 777
            py = dupec*ydrng - 120 + randint(0,ydrng)
            ptime = randint(8000,10000)
            pdrop = randint(50,150)
            pscalex = round(uniform(0.2,0.5),2)
            pscaley = round(uniform(0.1,0.4),2)
            protate = 2*pi*round(uniform(2,5),1)*((-1)**randint(1,2))
            pcolour = randint(0,2)

            # Generate
            p = osbject("sb/petal.png", "Background", "Centre", px, py)

            p.moveX(0,i,i+ptime,px,-120)
            p.moveY(0,i,i+ptime,py,py+pdrop)

            p.rotate(0,i,i+ptime,0,protate)

            p.para(0,i,i,"A")

            # Colours
            if pcolour == 0:
                p.colour(0,i,i,178,120,154,178,120,154)
            elif pcolour == 1:
                p.colour(0,i,i,230,120,184,230,120,184)
            else:
                p.colour(0,i,i,226,174,204,226,174,204)

            # Check if at the start or at the end
            if i <= 6753:
                p.fade(0,6753,6753,0,1)
            elif i >= 211979:
                p.fade(0,221979,221979,1,0)

            # Flip vector scale in x so many times
            vectime = 0
            vectime2 = 0
            flip = 0
            switch = randint(2,5)
            for k in range(switch):
                vectime2 += round(ptime/switch)
                if flip == 0:
                    p.vecscale(5,i+vectime,i+vectime2,pscalex,pscaley,-pscalex,pscaley)
                    flip = 1
                else:
                    p.vecscale(5,i+vectime,i+vectime2,-pscalex,pscaley,pscalex,pscaley)
                    flip = 0
                vectime += round(ptime/switch)

            dupec += 1

# Flare
flare = osbject("sb/flare.png", "Background", "Centre", 376, 224)
flare.scale(0,57850,57850,0.56,0.56)
flare.para(0,57850,57850,"A")

flare.fade(0,57850,57850,0,1)
flare.fade(0,82624,83398,1,0)
flare.rotate(0,57850,83398,-0.025,0.025)

flare.fade(0,133721,133721,0,1)
flare.fade(0,158495,159269,1,0)
flare.rotate(0,133721,159269,-0.025,0.025)

flare.fade(0,209398,209592,0,1)
flare.fade(0,221979,221979,1,0)
flare.rotate(0,209398,221979,-0.025,0)

# Background bar for lyrics
bar = osbject("sb/bar.png", "Background", "TopLeft", -107, 358)

ax, ay = 0, 0.05 # Closed
bx, by = 0.515, 0.5 # Opened

# 1st
bar.vecscale(1,17592,18366,ax,ay,bx,ay)
bar.vecscale(1,18366,19140,bx,ay,bx,by)

bar.fade(1,82624,83398,0.5,0)

# 2nd
bar.fade(1,93463,93463,0.5,0.5)
bar.vecscale(1,93463,94237,ax,ay,bx,ay)
bar.vecscale(1,94237,95011,bx,ay,bx,by)

bar.fade(1,158495,159269,0.5,0)

# 3rd
bar.fade(1,181721,181721,0.5,0.5)
bar.vecscale(1,181721,182495,ax,ay,bx,ay)
bar.vecscale(1,182495,183269,bx,ay,bx,by)

bc = 200
bar.colour(0,17592,221979,bc,bc,bc,bc,bc,bc)

#bar.para(0,17592,17592,"A")

### Lyrics ###

# List of line lengths
charlen = [
6, 6, 8, 10,
6, 8, 6, 7,
5, 7, 11,
8, 3, 9, 8, 9, 4, 8, 7,
7, 7, 7, 7,
5, 6, 6, 7,
6, 6, 11,
8, 3, 10, 7, 8, 3, 8, 7,
5, 7, 8,
8, 3, 9, 8, 9, 4, 8, 7]

# List of start times for lyrics
lyrstarts = [
19140, 22237, 25334, 28237,
31527, 34624, 37721, 40818,
43914, 47011, 49721,
57850, 60947, 63850, 66947, 70237, 73334, 76237, 79334,
95011, 98108, 101205, 104301,
107398, 110495, 113592, 116689,
119785, 122882, 125592,
133721, 136818, 139721, 142818, 146108, 149205, 152108, 155205,
183269, 186366, 189076,
197205, 200301, 203205, 206301, 209592, 212689, 215592, 218689]

# List of end times for lyrics
lyrends = [
21850, 24947, 27850, 30753,
34237, 37334, 40430, 43527,
46624, 49334, 56301,
60559, 63463, 66559, 69850, 72947, 75656, 78947, 82624,
97721, 100818, 103914, 106624,
110108, 113205, 116301, 119398,
122495, 125205, 132172,
136430, 139334, 142430, 145721, 148818, 151527, 154818, 158495,
185979, 188689, 195656,
199914, 202624, 205914, 209205, 212301, 215205, 218301, 221979]

# Import the list from charlist.csv
with open("charlist.csv", "r") as f:
    chars = []
    for i in f:
        chars.append([x for x in i.split()])

# Import the list from charlistglow.csv
with open("charlistglow.csv", "r") as f:
    charglows = []
    for i in f:
        charglows.append([x for x in i.split()])

# chatlist.csv and charlistglow.csv is in the format [File name, Relative x coord, Relative y coord]
# They should be TopLeft aligned. Relative 0,0 is the centre of the line.

# Position every character in time
lyrcenx, lyrceny = 196, 364 # Relative centre of lyrics on the SB field

# Retrieve the correct number of characters per line, place and time them,
# Then move onto the next line etc
linelength = 0
linenumber = 0
flip = 0

for i in range(len(chars)):
    # Find file name and its relative position
    char = chars[i][0]
    charx = lyrcenx+float(chars[i][1])
    chary = lyrceny+float(chars[i][2])

    # Check each character's position in the line,
    # Bump the line number when needed and reset line length
    if linelength != charlen[linenumber]:
        charstart = lyrstarts[linenumber]
        charend = lyrends[linenumber]
        linelength += 1
    else:
        linenumber += 1
        charstart = lyrstarts[linenumber]
        charend = lyrends[linenumber]
        linelength = 1
        flip = 0

    # Glow position relative to characters
    chargx = charx-1.5
    chargy = chary-1.5

    # Put it all together,
    # Then start animating, fade in, alternate wipe up/down
    # Glow
    cg = osbject("sb/f/glow/{}.png".format(char), "Background", "TopLeft", chargx, chargy)

    cg.scale(0,charstart,charend,0.5,0.5)

    if charend == 221979:
        # Check if it's at the end of the song
        cbuff = 0
    else:
        cbuff = 500

    cg.fade(1,charstart-500,charstart,0,1)
    cg.fade(1,charend,charend+cbuff,1,0)

    cg.colour(6,charstart-500,charstart,255,255,255,0,0,0)
    cg.colour(7,charend,charend+500,0,0,0,255,255,255)

    # Main characters
    c = osbject("sb/f/{}.png".format(char), "Background", "TopLeft", charx, chary)

    c.scale(0,charstart,charend,0.5,0.5)

    c.fade(1,charstart-150,charstart,0,1)
    c.fade(1,charend,charend+cbuff,1,0)

    # Up/down slide transitions, alternating
    if flip == 0:
        c.moveY(2, charstart-500, charstart, chary-60, chary)
        c.moveY(0, charend, charend+500, chary, chary+60)

        cg.moveY(2, charstart-500, charstart, chargy-60, chargy)
        cg.moveY(0, charend, charend+500, chargy, chargy+60)

        flip = 1
    else:
        c.moveY(2, charstart-500, charstart, chary+60, chary)
        c.moveY(0, charend, charend+500, chary, chary-60)

        cg.moveY(2, charstart-500, charstart, chargy+60, chargy)
        cg.moveY(0, charend, charend+500, chargy, chargy-60)

        flip = 0

# Blackout toggling

def blackout(bs,be,ws,wp,we):
        black = osbject("sb/white.png", "Background", "Centre", 320, 240)
        black.fade(0,bs,be,0,1)
        black.colour(0,ws,wp,0,0,0,255,255,255)
        black.fade(0,wp,we,1,0)

blackout(56301,56689,57656,57850,58043)
blackout(132172,132559,133527,133721,133914)
blackout(195656,196043,197011,197205,197398)

# Whiteout toggling
def whiteout(start,peak,end):
    white = osbject("sb/white.png", "Background", "Centre", 320, 240)
    white.fade(0,start,peak,0,1)
    white.fade(0,peak,end,1,0)

whiteout(5979,6753,6850)
whiteout(221592,221979,222076)
whiteout(228076,228172,228269)

export_path = u"songFolder/senya - Shounen yo, Tokkou no Sakigake to Nare (-Mo-).osb"
osbject.end(export_path)
