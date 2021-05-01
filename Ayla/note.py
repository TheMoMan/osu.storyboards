class Note:
  def __init__(self, noteNumber, start=0, end=0, channel=0):
    self.noteNumber = noteNumber
    self.name = Note.midiNumberToName(noteNumber)
    self.octave = Note.midiNumberToOctave(noteNumber)
    self.note = self.name + self.octave
    self.start = start
    self.end = max(start, end)
    self.duration = self.end - self.start
    self.channel = channel

  def setEnd(self, end):
    self.end = max(self.start, end)
    self.duration = self.end - self.start

  @staticmethod
  def midiNumberToName(num):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes[num % 12]

  @staticmethod
  def midiNumberToOctave(num):
    return str(num // 12 - 1)

  @staticmethod
  def nameToMidiNumber(name):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    octave = int(name[-1]) * 12 + 12
    note = notes.index(name[:-1])

    return note + octave

  def isBlackKey(self):
    return self.name in ['C#', 'D#', 'F#', 'G#', 'A#']
  
  def toString(self):
    return 'Number: ' + str(self.noteNumber) \
    + ', Name: ' + self.name \
    + ', Octave: ' + self.octave \
    + ', Note: ' + self.note \
    + ', Start: '+ str(self.start) \
    + ', End: ' + str(self.end) \
    + ', Duration: ' + str(self.duration) \
    + ', Channel: ' + str(self.channel)
