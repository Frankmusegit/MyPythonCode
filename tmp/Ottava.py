#!/usr/bin/env python
#-*- coding:utf-8 -*-
from Textline import *

class Ottava(TextLine):
    def __init__(self, s):
        TextLine.__init__(self, s)
        self.setSubtype(0)