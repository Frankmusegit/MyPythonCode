#!/usr/bin/env python
#-*- coding:utf-8 -*-
import AL
from Fraction import *

def ticks_measure(f):
    return (AL.division * 4 * f.numerator()) / f.denominator()


class SigEvent:

    def __init__(self, f):
        self.actual  = f
        self.nominal = f
        self.bar     = 0
        self.ticks   = ticks_measure(f)

class TimeSigMap(dict):

    def __init__(self):
        super(TimeSigMap, self).__init__()
        self. _serial = 0

    def normalize(self):
        z    = 4
        n    = 4
        tick = 0
        bar  = 0
        tm   = ticks_measure(Fraction(z, n))
        i = self.iteritems()
        #need update


    def add(self,tick, f):
        if not f.isValid():
            print "illegal signature %d/%d\n" %(f.numerator(), f.denominator())
        tick = SigEvent(f)
        self.normalize()