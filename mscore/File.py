#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from PyQt4.QtCore import *

class LoadFile:

    def __init__(self):
        self.popenFlag = False
        self._name = QString()
        self.error = QString()

