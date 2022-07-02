import math
from mido import MidiFile
from note import *

def parseMidi():
  mid = MidiFile('inputs/Ayla_-_M2U.mid')
  tempo = 387097
  offset = 25
  notes = []
  onNotes = {}

  dTime = tempo/480 * 0.001

  for i, track in enumerate(mid.tracks):
    currentTime = 0

    for msg in track:
      currentTime += msg.time
      realTime = round(currentTime * dTime) + offset

      if msg.type == 'note_on':
        if msg.velocity > 0:
          note = Note(msg.note, realTime, channel=i)
          onNotes[msg.note] = note
        else:
          note = onNotes.pop(msg.note)
          note.setEnd(realTime)
          notes.append(note)

  with open('t.txt', 'w') as f:
    for note in notes:
      f.write(note.toString() + '\n')
  
  if len(onNotes) > 0:
    print('Warning - Not all notes have proper end values set')

  return notes

  # with open('parsedMidi.txt', 'w') as f:
  #   for i, track in enumerate(mid.tracks):
  #     f.write('=== Track {} ===\n'.format(i))
  #     for msg in track:
  #       f.write(str(msg) + '\n')
