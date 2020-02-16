from __future__ import print_function, division
from builtins import *
from osbpy import *

# Temporary, Collab Names
# Background bar for names
bar = osbject("sb/bar.png", "Foreground", "TopLeft", -107, 410)

ax, ay = 0, 0.05 # Closed
bx, by = 0.3, 0.32 # Opened

# 1st
bar.vecscale(1,6753,7527,ax,ay,bx,ay)
bar.vecscale(1,7527,8301,bx,ay,bx,by)

bar.fade(0,56301,56689,0.5,0)
bar.fade(0,57850,58043,0,0.5)

bar.fade(1,82624,83398,0.5,0)

# 2nd
bar.fade(1,88818,88818,0.5,0.5)
bar.vecscale(1,88818,89592,ax,ay,bx,ay)
bar.vecscale(1,89592,90366,bx,ay,bx,by)

bar.fade(0,132172,132559,0.5,0)
bar.fade(0,133721,133914,0,0.5)
bar.fade(0,195656,196043,0.5,0)

# 3rd
bar.fade(1,203398,203398,0.5,0.5)
bar.vecscale(1,203398,204172,ax,ay,bx,ay)
bar.vecscale(1,204172,204947,bx,ay,bx,by)

bar.fade(0,221592,221979,0.5,0)
bar.fade(0,221979,222076,0,0.5)

bar.fade(1,234366,235140,0.5,0)

bc = 200
bar.colour(1,182882,183656,240,210,110,130,200,240)
bar.colour(1,221979,221979,240,130,150,bc,bc,bc)

# Import Satellite
with open("satellite.csv", "r") as f:
    sat = []
    for i in f:
        sat.append([x for x in i.split()])

# Import -Mo-
with open("mo.csv", "r") as f:
    mo = []
    for i in f:
        mo.append([x for x in i.split()])

namey = 404

def name(user,start,end,fadestart,fadeend):
    namedelay = 0

    if user == sat:
        rng = 9
        userx = 94
    elif user == mo:
        rng = 4
        userx = 144

    if fadestart == -1:
        # Bodge it all
        endp = 388
    else:
        endp = 774

    for i in range(rng):
        char = user[i][0]
        charx = userx+float(user[i][1])
        chary = namey+float(user[i][2])

        namestart = start+namedelay

        u = osbject("sb/u/{}.png".format(char), "Foreground", "TopLeft", charx, chary)
        u.scale(0,start,start,0.4,0.4)
        u.moveX(30,namestart,namestart+500,charx-320,charx)
        u.fade(0,end,end+endp,1,0)

        if fadestart != -1:
            if user == sat:
                u.fade(0,fadestart,fadestart+388,1,0)
                u.fade(0,fadeend,fadeend+194,0,1)
            else:
                u.fade(0,fadestart,fadestart+388,1,0)
                u.fade(0,fadeend,fadeend+97,0,1)

        namedelay += 100

name(sat,7527,82624,56301,57850)
name(sat,89592,182882,132172,133721)
name(mo,182882,195656,-1,0)
name(mo,204172,234366,221592,221979)

export_path = u"names.txt"
osbject.end(export_path)
