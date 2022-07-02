from random import randint, seed
from osbpy import *
from parseMidi import parseMidi
from note import *

testing = False

seed('f2fab7bd275158bb5ee1b274bb8ad969')
endOfMap = 174605

# Background
bg = osbject('bg.jpg', 'Background', 'Centre', 320, 240)
bg.scale(0, -3500, endOfMap, 0.444444, 0.444444)
bg.fade(0, -1500, -1500, 1, 0)
bg.fade(0, 171702, 171702, 0, 1)
bg.fade(0, 174218, endOfMap, 1, 0)

bgBlur = osbject('sb/blur.jpg', 'Background', 'Centre', 320, 240)
bgBlur.scale(0, -3000, endOfMap, 0.444444, 0.444444)
bgBlur.fade(0, -3000, -1500, 0, 1)
bgBlur.fade(0, 171702, endOfMap, 1, 0)

# Piano
noteWidth = 20         # Width of the note image file in px
pWidth = 58            # Width of keys in the image file in px
pHeight = 300          # Height of keys in the image file in px
keyRange = 49          # Number of white keys to generate (should be odd)
whiteKeySpacing = 12   # Spacing between white key
noteWidthScale = 0.55  # Width scaling of a note for a white key
splashHeight = 0.2     # Scale height of splash
splashWidth = 0.6      # Scale width of splash

pScale = (noteWidth / pWidth) * noteWidthScale
c4Index = keyRange // 2

keyNames = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
keyFiles = {
  'C': '10',
  'D': '00',
  'E': '01',
  'F': '10',
  'G': '00',
  'A': '00',
  'B': '01',
}

keyHighlights = {}
keyPositions = {}
keys = []
keyOctave = 3 - c4Index // 7

def getKeyFile(keyType, getHl=False):
  return 'sb/keys/{}hl.png'.format(keyType) if getHl else 'sb/keys/{}.png'.format(keyType)

for i in range(keyRange):
  keyNameIndex = (i - int(c4Index)) % 7
  if keyNameIndex == 0:
    keyOctave += 1

  keyName = keyNames[keyNameIndex]
  keyFullName = keyName + str(keyOctave)
  keyType = keyFiles[keyName]
  keyFile = getKeyFile(keyType)

  if i == 0:
    chars = list(keyFile)
    chars[-6] = '1'
    keyFile = ''.join(chars)
  elif i == (keyRange - 1):
    chars = list(keyFile)
    chars[-5] = '1'
    keyFile = ''.join(chars)

  pX = 320 + (i - c4Index) * whiteKeySpacing

  p = osbject(keyFile, 'Foreground', 'TopCentre', pX, 240)
  p.scale(0, -3000, 174702, pScale, pScale)

  hl = osbject(getKeyFile(keyType, True), 'Foreground', 'TopCentre', pX, 240)
  hl.scale(0, -3000, -3000, pScale, pScale)
  hl.fade(0, -3000, -3000, 0, 0)

  sp = osbject('sb/splash.png', 'Foreground', 'BottomCentre', pX, 240)
  sp.vecscale(0, -3000, -3000, splashWidth, splashHeight, splashWidth, splashHeight)

  keyHighlights[keyFullName] = [hl, sp]
  keyPositions[keyFullName] = pX
  keys.append(p)

  # Add black keys
  if (keyFile[-5] == '0'):
    pX += int(whiteKeySpacing * 0.5)

    pb = osbject('sb/keys/bb.png', 'Foreground', 'TopCentre', pX, 240)
    pb.scale(0, -3000, 174702, pScale, pScale)

    pbhl = osbject('sb/keys/bbhl.png', 'Foreground', 'TopCentre', pX, 240)
    pbhl.scale(0, -3000, -3000, pScale, pScale)
    pbhl.fade(0, -3000, -3000, 0, 0)

    sp = osbject('sb/splash.png', 'Foreground', 'BottomCentre', pX, 240)
    sp.vecscale(0, -3000, -3000, splashWidth * 0.5, splashHeight, splashWidth * 0.5, splashHeight)

    keyFullName = keyName + '#' + str(keyOctave)
    keyHighlights[keyFullName] = [pbhl, sp]
    keyPositions[keyFullName] = pX
    keys.append(pb)

# Fade in/out
delay = round(689 / len(keys))
keyTime = 0

for key in keys:
  introStartTime = -1843 + keyTime
  introEndTime = introStartTime + 100
  outroStartTime = 171756 + keyTime
  outroEndTime = outroStartTime + 100
  key.fade(0, introStartTime, introEndTime, 0, 1)
  key.fade(0, outroStartTime, outroEndTime, 1, 0)

  keyTime += delay

def particles(note):
  minHeight = 100
  maxHeight = 300
  maxDeviation = 50
  maxLife = 4000
  fadeTime = 3000
  fadeOffset = 500
  scale = 0.03
  rate = 16

  pX = keyPositions[note.name + note.octave]
  start = note.start
  end = note.end

  currentTime = start
  while currentTime < end:
    height = randint(minHeight, maxHeight)
    deviation = randint(-maxDeviation, maxDeviation)
    fadeEnd = min(currentTime + maxLife - fadeOffset, endOfMap)
    fadeStart = fadeEnd - fadeTime
    endTime = min(currentTime + maxLife, endOfMap)

    p = osbject('sb/particle.png', 'Background', 'Centre', pX, 240)
    p.scale(0, currentTime, currentTime, scale, scale)
    p.moveX(4, currentTime, endTime, pX, pX + deviation)
    p.moveY(4, currentTime, endTime, 240, 240 - height)
    p.fade(2, fadeStart, fadeEnd, 0.6, 0)
    p.para(0, currentTime, currentTime, 'A')

    currentTime += rate

# Notes
scrollTime = 2500     # Time for notes to travel top of screen to piano in ms
noteHeight = 20       # Height of the note image file in px
noteWidthBlackScale = 0.6 # Width scaling of a note for a black key

scrollSpeed = 290 / scrollTime
lengthMultiplier = (1 / noteHeight) * scrollSpeed

def testNotes():
  notes = []

  for i in range(24):
    n = Note(60 + i, i*500, i*500 + 500)
    notes.append(n)
  
  return notes

notes: [Note] = testNotes() if testing else parseMidi()

def getKeyOffset(noteName, spacing):
  return {
    'A' : 5,
    'A#': 5.5,
    'B' : 6,
    'C' : 0,
    'C#': 0.5,
    'D' : 1,
    'D#': 1.5,
    'E' : 2,
    'F' : 3,
    'F#': 3.5,
    'G' : 4,
    'G#': 4.5,
  }[noteName] * spacing

def getOctaveOffset(octave, spacing):
  return (int(octave) - 4) * 7 * spacing

def getNoteXPosition(note):
  keyOffset = getKeyOffset(note.name, whiteKeySpacing)
  octaveOffset = getOctaveOffset(note.octave, whiteKeySpacing)

  return 320 + keyOffset + octaveOffset

for note in notes:
  noteLength = (note.duration * lengthMultiplier)
  noteWidth = noteWidthScale * noteWidthBlackScale if note.isBlackKey() else noteWidthScale
  noteDisplacement = noteLength * noteHeight + 240

  n = osbject('sb/note.png', 'Foreground', 'BottomCentre', getNoteXPosition(note), 240)
  n.moveY(0, note.start - scrollTime, note.start, -50, 240)
  n.vecscale(0, note.start, note.end, noteWidth, noteLength, noteWidth, 0)
  # n.fade(0, note.start, note.start, 0.8, 0.8)
  n.para(0, note.start, note.start, 'A')

  if note.channel == 0:
    R = 200
    G = 255
    B = 255
    n.colour(0, note.start, note.start, R, G, B, R, G, B)
  else:
    R = 120
    G = 120
    B = 255
    n.colour(0, note.start, note.start, R, G, B, R, G, B)
  
  highlights = keyHighlights[note.name + note.octave]

  for highlight in highlights:
    highlight.fade(0, note.start, note.start, 0, 1)
    highlight.fade(0, note.end, note.end, 1, 0)
  
  particles(note)

l = osbject('sb/px.png', 'Foreground', 'CentreLeft', -107, 240)
l.vecscale(0, -2000, -1000, 0, 2, 854, 2)
l.fade(0, 0, 171702, 0.5, 0.5)

l = osbject('sb/px.png', 'Foreground', 'CentreRight', 747, 240)
l.vecscale(0, 171702, 172702, 854, 2, 0, 2)
l.fade(0, 171702, 171702, 0.5, 0.5)

# Spectrum
har = 31 # Number of bars
gap = 12 # Spacing between bars
posx = 320 - (har // 2) * gap

specs = spectrum(
  'inputs/audio.wav',
  'sb/note.png',
  mi=0.1,
  mx=10,
  har=har,
  start=-1523,
  end=173444,
  posx=posx,
  posy=380,
  layer='Background',
  origin='Centre',
  gap=gap,
  width = 0.1,
)

delay = 24
keyTime = 0

for spec in specs:
  spec.para(0, 0, 0, 'A')
  spec.fade(0, 0, 0, 0.75, 0.75)

  introStartTime = -1843 + keyTime
  introEndTime = introStartTime + 100
  outroStartTime = 171756 + keyTime
  outroEndTime = outroStartTime + 100
  spec.fade(0, introStartTime, introEndTime, 0, 1)
  spec.fade(0, outroStartTime, outroEndTime, 1, 0)

  keyTime += delay

with open ('inputs/loc.txt', 'r', encoding='utf-8') as f:
  loc = f.readline().rstrip()

osbject.end(loc + 'M2U - Ayla (-Mo-).osb')
