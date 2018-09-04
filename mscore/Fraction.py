#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Fraction:

    def __init__(self, z = 0, n = 1):
        self._numerator = z
        self._denominator = n

    def isValid(self):
        return self._denominator != 0

    def numerator(self):
        return self._numerator

    def denominator(self):
        return self._denominator