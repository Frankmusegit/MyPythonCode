#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from Key import *
from globals import *


class Staff:

    def __init__(self):
        self._score        = 0
        self._rstaff       = 0
        self._part         = 0
        self._clefList     = []
        self._keymap       = KeyList()
        self._keymap = [0]
        self._show         = True
        self._lines        = 5
        self._small        = False
        self._slashStyle   = False
        self._barLineSpan  = 1
        self._invisible    = False

    def Staff1(self, s, p, rs):
        
        self._score        = s
        self._rstaff       = rs
        self._part         = p

    def score(self):
        return self._score

        
    def mag(self):
        if self._small:
           return  self.score().styleD(StyleIdx.ST_smallStaffMag)
        else:
            return 1.0

















      
