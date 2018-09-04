#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Durationtype import *

class InputState:

    def __init__(self):
        self.noteEntryMode = False
        self.rest = False
        self._duration = Duration()
        self.track = 0
        self.noteType = NoteType()
        self.beamMode = BeamMode()


    def duration(self):
        return self._duration

    def voice(self):
        return self.track % VOICES