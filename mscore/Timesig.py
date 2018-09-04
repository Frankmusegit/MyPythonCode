#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Element import *
from Fraction import *

class TimeSig(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self.sz = QString()
        self.sn = QString()
        self.pz = QString()
        self.pn =  QString()

    def sigtype(self, n, z1, z2 = 0, z3 = 0, z4 = 0):
        return (z4 << 24) + (z3 << 18) + (z2 << 12) + (z1 << 6) + n

    def setSig(self, n, z1, z2, z3, z4):
        self.setSubtype(self.sigtype(n, z1, z2, z3, z4))

    def getSig(self):
        return self.getSig1(self.subtype())

    def getSig1(self, st):
        return Fraction(((st >> 24) & 0x3f) + ((st >> 18) & 0x3f) + ((st >> 12 )& 0x3f) + ((st >> 6) & 0x3f), st & 0x3f)

    def getSig2(self, n, z1, z2, z3, z4):
        st = self.subtype()
        n = st & 0x3f
        if z4:
            z4 = (st>>24)& 0x3f
        if z3:
            z3 = (st>>18)& 0x3f
        if z2:
            z2 = (st>>12)& 0x3f
        z1 = (st>>6) & 0x3f

    def TimeSig1(self, st):
        self.setSubtype(st)

    def TimeSig2(self, n, z1,  z2=0,  z3=0, z4=0):
        self.setSig(n, z1, z2, z3, z4)

    def type(self):
        return ElementType.TIMESIG
