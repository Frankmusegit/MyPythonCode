#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from Element import *
from Style import *
#import Score


class TextBase:
    def __init__(self):
        #super(TextBase, self).__init__()
        self._refCount     = 1
        self._doc          = QTextDocument()
        self._doc.setDocumentMargin(1.0)
        self._doc.setUseDesignMetrics(True)
        self._doc.setUndoRedoEnabled(True)
        self._doc.documentLayout().setProperty("cursorWidth", QVariant(2))

        self._hasFrame     = False
        self._frameWidth   = 0.35
        self._paddingWidth = 0.0
        self._frameColor   = Preferences().defaultColor
        self._frameRound   = 25
        self._circle       = False
        self._layoutWidth  = -1

        to = self._doc.defaultTextOption()
        to.setUseDesignMetrics(True)
        to.setWrapMode(QTextOption.NoWrap)
        self._doc.setDefaultTextOption(to)

    def refCount(self):
        return self._refCount

    def incRefCount(self):
        self._refCount = self._refCount + 1

    def decRefCount(self):
        self._refCount = self._refCount - 1

    def doc(self):
        return self._doc

    def setHasFrame(self, v):
        self._hasFrame = v

    def hasFrame(self):
        return self._hasFrame

    def frameWidth(self):
        return self._frameWidth

    def setFrameWidth(self, v):
        self._frameWidth = v

    def paddingWidth(self):
        return self._paddingWidth

    def setPaddingWidth(self,v):
        self._paddingWidth = v
        
    def setFrameColor(self, v):
        self._frameColor = v

    def frameColor(self):
        return self._frameColor

    def setFrameRound(self, v):
        self._frameRound = v

    def frameRound(self):
        return self._frameRound
        
    def setCircle(self, v):
        self._circle = v

    def circle(self):
        return self._circle

    def clear(self):
        self._doc.clear()

    def bbox(self):
        return self._bbox

    def isEmpty(self):
        return self._doc.isEmpty()

    def setModified(self, v):
        self._doc.setModified(v)
        
    def setText(self, s, align):
        self._doc.clear()
        cursor = QTextCursor(self._doc)
        cursor.movePosition(QTextCursor.Start)
        if align & (AlignmentFlags.ALIGN_HCENTER | AlignmentFlags.ALIGN_RIGHT):
            if align & AlignmentFlags.ALIGN_HCENTER:
                a = Qt.AlignHCenter
            elif align & AlignmentFlags.ALIGN_RIGHT:
                a = Qt.AlignRight
            bf = cursor.blockFormat()
            bf.setAlignment(a)
            cursor.setBlockFormat(bf)
        tf = cursor.charFormat()
        tf.setFont(self._doc.defaultFont())
        cursor.setBlockCharFormat(tf)
        cursor.insertText(s)
        self._doc.setTextWidth(self._doc.idealWidth())

    def setHtml(self, s):
        self._doc.clear()
        self._doc.setHtml(s)

      
class TextB(Element):
    def __init__(self, s):
        Element.__init__(self, s)
        self._editMode   = False
        self.cursorPos  = 0
        self.cursor     = 0
        self._movable   = True
        self._textStyle = -1
        self._reloff = QPointF()

    def type(self):
        return ElementType.TEXT
        
    def isMovable(self):
        return self._movable

    def setMovable(self, val):
        self._movable = val

    def clear(self):
        self.textBase().clear()


    def setText(self, s):
        self.textBase().setText(s, self._align)
        
    def getText(self):
        return self.textBase().getText()

    def getHtml(self):
        return self.textBase().getHtml()

    def setHtml(self, s):
        self.textBase().setHtml(s)

    def doc(self):
        return self.textBase().doc()

    def frameWidth(self):
        return self.textBase().frameWidth()

    def paddingWidth(self):
        return self.textBase().paddingWidth()

    def frameColor(self):
        return self.textBase().frameColor()

    def frameRound(self):
        return self.textBase().frameRound()

    def circle(self):
        return self.textBase().circle()

    def sizeIsSpatiumDependent(self):
        return self._sizeIsSpatiumDependent

    def setSizeIsSpatiumDependent(self, v):
        self._sizeIsSpatiumDependent = v

    def setFrameWidth(self, val):
        self.textBase().setFrameWidth(val)

    def setPaddingWidth(self, val):
        self.textBase().setPaddingWidth(val)

    def setFrameColor(self, val):
        self.textBase().setFrameColor(val)

    def setFrameRound(self, val):
        self.textBase().setFrameRound(val)

    def setCircle(self, val):
        self.textBase().setCircle(val)

    def defaultFont(self):
        return self.textBase().defaultFont()

    def setDefaultFont(self, f):
        self. textBase().setDefaultFont(f)

    def getCursor(self):
        return self.cursor

    def textStyle(self):
        return self._textStyle

    def editMode(self):
        return self._editMode

    def setTextStyle(self, idx):
        self._textStyle   = idx
        s = GL.gscore.textStyle(idx)
        TextBase()._doc.setDefaultFont(s.font(self.spatium()))

        self._align         = s.align
        self._xoff          = s.xoff
        self._yoff          = s.yoff
        self._reloff.x   = s.rxoff
        self._reloff.y   = s.ryoff
        self._offsetType    = s.offsetType
        self.setColor(s.foregroundColor)
        self._sizeIsSpatiumDependent = s.sizeIsSpatiumDependent
        self.setSystemFlag(s.systemFlag)

        TextBase().setFrameWidth(s.frameWidth)
        TextBase().setHasFrame(s.hasFrame)
        TextBase().setPaddingWidth(s.paddingWidth)
        TextBase().setFrameColor(s.frameColor)
        TextBase().setFrameRound(s.frameRound)
        TextBase().setCircle(s.circle)

class TextC(TextB):
    def __init__(self, s):
        TextB.__init__(self, s)
        self._tb = TextBase()
        self.setSubtype(TEXT.TEXT_STAFF)

    def textBase(self):
        return self._tb

class Text(TextB):
    def __init__(self, s):
        TextB.__init__(self, s)
        self._tb = TextBase()
        self.setSubtype(0)

    def textBase(self):
        return self._tb
