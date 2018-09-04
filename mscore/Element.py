#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-
from Preferences import *
from Staff import *


class Element(QObject):
    def __init__(self, s = 0):
        self._parent = 0
        self._selected = False
        self._selectable = True
        self._dropTarget = False
        self._generated = False
        self._visible = True
        self._systemFlag = False
        self._subtype = 0
        self._track = -1
        self._tick = -1
        self._color = Preferences().defaultColor
        self._mag = 1.0
        self._score = s
        self._align = AlignmentFlags.ALIGN_LEFT | AlignmentFlags.ALIGN_TOP
        self._xoff = 0
        self._yoff = 0
        self._offsetType = OffsetType.OFFSET_SPATIUM
        self._mxmlOff = 0
        self._reloff = QRectF()
        self.itemDiscovered = 0
        self._bbox = QRectF()
        self._pos = QPointF()
        self._userOff = QPointF()
        self.itemDiscovered = 0

    def score(self):
        return self._score

    def setScore(self, s):
        self._score = s

    def parent(self):
        return self._parent

    def setParent(self, e):
        self._parent = e

    def spatium(self):
        s = Staff()
        v = self._score.spatium()
        if s:
            return v* s.mag()
        else:
            return v

    def setSubtype(self, val):
        self._subtype = val

    def subtype(self):
        return self._subtype

    def selected(self):
        return self._selected

    def setSelected(self, f):
        self._selected = f

    def setVisible(self, f):
        self._visible = f

    def visible(self):
        return self._visible

    def setSelectable(self, val):
        self._selectable = val

    def selectable(self):
        return self._selectable

    def generated(self):
        return self._generated

    def setGenerated(self, val):
        self._generated = val

    def dropTarget(self):
        return self._dropTarget

    def setDropTarget(self, f):
        self._dropTarget = f

    def ipos(self):
        return self._pos

    def pos(self):
        return self._pos + self._userOff

    def x(self):
        return self._pos.x() + self._userOff.x()

    def y(self):
        return self._pos.y() + self._userOff.y()

    def setPos(self, x, y):
        self._pos.rx = x
        self._pos.ry = y

    def setPos1(self, p):
        self._pos = p

    def movePos(self, p):
        self._pos = self._pos + p

    def rxpos(self):
        return self._pos.rx()

    def rypos(self):
        return self._pos.ry()

    def move(self, xd, yd):
        self._pos  = self._pos + QPointF(xd, yd)

    def move1(self, s):
        self._pos =  self._pos + s

    def userOff(self):
        return self._userOff

    def setUserOff(self, o):
        self._userOff = o

    def setUserXoffset(self, v):
        self._userOff.setX(v)

    def setUserYoffset(self, v):
        self._userOff.setY(v)

    def mxmlOff(self):
        return self._mxmlOff

    def setMxmlOff(self, o):
        self._mxmlOff = o

    def height(self):
        return self.bbox().height()

    def setHeight(self, v):
        return self._bbox.setHeight(v)

    def  width(self):
        return self.bbox().width()

    def setWidth(self, v):
        return self._bbox.setWidth(v)

    def baseLine(self):
        return -self.height()

    def subtype(self):
        return self._subtype

    def setSubtype(self, val):
        self._subtype = val

    def isChordRest(self):
        return self.type() == ElementType.REST or self.type() == ElementType.CHORD

    def isDurationElement(self):
        return self.isChordRest() or  (self.type() ==  ElementType.TUPLET)

    def isSLine(self):
        return self.type() == ElementType.HAIRPIN or self.type() == ElementType.OTTAVA or self.type() == ElementType.PEDAL\
               or self.type() == ElementType.TRILL or self.type() == ElementType.VOLTA or self.type() == ElementType.TEXTLINE

    def isMovable(self):
        return False

    def dragAnchor(self):
        return QLineF()

    def isEditable(self):
        return not self._generated

    def track(self):
        return self._track

    def setTrack(self, val):
        self._track = val

    def staffIdx(self):
        return self._track / VOICES

    def  voice(self):
        return self._track % VOICES

    def setVoice(self, v):
        self._track = (self._track / VOICES) + v

    def tick(self):
        return self._tick

    def setTick(self, t):
        self._tick = t

    def setColor(self, c):
        self._color = c

    def color(self):
        return self._color

    def setSystemFlag(self, f):
        self._systemFlag = f

    def  setbbox(self, r):
        self._bbox = r

    def bbox(self):
        return self._bbox

    def  mag(self):
        return self._mag

    def setMag(self, val):
        self._mag = val

    def align(self):
        return self._align

    def offsetType(self):
        return self._offsetType

    def xoff(self):
        return self._xoff

    def yoff(self):
        return self._yoff

    def reloff(self):
        return self._reloff

    def setReloff(self, val):
        self._reloff = val

    def setAlign(self, val):
        self._align  = val

    def setXoff(self, val):
        self._xoff   = val

    def setYoff(self, val):
        self._yoff   = val

    def setOffsetType(self, val):
        self._offsetType = val

    def systemFlag(self):
        return self._systemFlag

    def setSystemFlag(self, f):
        self._systemFlag = f


    def canvasPos(self):
        p =  QPointF(self._pos + self._userOff)
        if self.parent():
            p = p +  self.parent().canvasPos()
        return p

    def abbox(self):
        return self.bbox().translated(self.canvasPos())

    def readType(self, e):
        type = ElementType.INVALID
        dragOffset = 0
        duration = 0
        e = e.firstChildElement()
        while not e.isNull():
            if e.tagName() == "dragOffset":
                dragOffset = self.readPoint(e)
            elif e.tagName() == "duration":
                duration = self.readFraction(e)
            elif self.name2type(e.tagName()) == ElementType.INVALID:
                type = self.name2type(e.tagName())
                self.domError(e)
                break
            if type != ElementType.INVALID:
                break
            e = e.nextSiblingElement()
        return (type, dragOffset, duration)

class Cursor(Element):
    def __init__(self, s, v):
        Element.__init__(self, s)
        self.viewer = v
        self._on = False
        self._blink = True
        self._h        = 6 * self.spatium()
        self._seg      = 0

class Compound(Element):

    def __init__(self, s):
        Element.__init__(self, s)


class Icon(Element):

    def __init__(self, s):
        #super(Icon, self).__init__(s)
        Element.__init__(self, s)
        self._action = None

    def setAction(self, a):
        self._action = a

    def type(self):
        return ElementType.ICON

    def icon(self):
        return self._action.icon()

    def action(self):
        return self._action



