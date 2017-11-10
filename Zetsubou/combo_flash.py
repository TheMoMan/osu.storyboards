from __future__ import print_function, division
from builtins import *
from math import atan2
from osbpy import *

diff = "easy"
file_name = "{}.txt".format(diff)

with open(file_name) as f:
    objects = []
    for i in f:
        objects.append([x for x in i.split(",")])

# Times

intro1 = list(range(13798, 19229))
verse1chorus1 = list(range(22073, 79573))
verse2chorus2 = list(range(113108, 183367))

fullTimes = intro1 + verse1chorus1 + verse2chorus2

addExceptions = [34832, 35177, 45867, 46211, 80005, 82763, 85522, 88280, 88280, 91039, 93798, 96556,
99315, 102073, 123108, 123453]

aEplus1 = [x+1 for x in addExceptions]
aEminus1 = [x-1 for x in addExceptions]

aE = addExceptions + aEplus1 + aEminus1

minusExceptions = [18970, 24487, 30005, 35522, 41039, 46556, 52073, 57591, 63108, 68625, 74142,
118280, 123798, 129315, 134832, 140349, 145867, 151384, 156901, 157936, 159315, 165177, 170694, 176211]

mEplus1 = [x+1 for x in minusExceptions]
mEminus1 = [x-1 for x in minusExceptions]

mE = minusExceptions + mEplus1 + mEminus1

newFullTimes = fullTimes + aE

for i in range(len(mE)):
    rem = mE[i]
    newFullTimes.remove(rem)

# circles 5, 21, 37
# sliders 6, 22, 38

for i in range(len(objects)):
    if (int(objects[i][3]) in [6, 22, 38, 5, 21, 37] and int(objects[i][2]) in newFullTimes) or int(objects[i][2]) in aE:
        headX = int(objects[i][0])
        headY = int(objects[i][1])
        sliderTime = int(objects[i][2])

        if int(objects[i][3]) in [2, 6, 22, 38]: # Sliders
            tailX = int(objects[i][6])
            tailY = int(objects[i][7])
        elif int(objects[i][3]) in [1, 5, 21, 37]: # Circles
            tailX = int(objects[i+1][0])
            tailY = int(objects[i+1][1])

        dY = (headY * -1) - (tailY * -1)
        dX = headX - tailX

        if dX != 0:
            grad = dY / dX
        elif dY > 0:
            grad = 1
        else:
            grad = -1

        angle = atan2((dY * -1), dX)

        o = osbject("sb/flash.png", "Foreground", "CentreLeft", tailX+64, tailY+56)
        o.scale(0, sliderTime, sliderTime, 0.9, 0.9)
        o.rotate(0, sliderTime, sliderTime, angle, angle)
        o.fade(1, sliderTime, sliderTime+1000, 1, 0)

export_path = u"{} sb.txt".format(diff)
osbject.end(export_path)
