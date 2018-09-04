#!/usr/bin/env python
#-*- coding:utf-8 -*-
from globals import *

class Duration:
    def __init__(self):
        self._val = DurationType.V_INVALID
        self._dots = 0

    def dots(self):
        return self._dots
