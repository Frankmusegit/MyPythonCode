#!/usr/bin/env python
#-*- coding:utf-8 -*-
from BSymbol import *
from globals import *
import GL
from Xml import *
from PyQt4.QtSvg import *

class Image(BSymbol):
    def __init__(self, s):
        BSymbol.__init__(self, s)
        self._ip              = 0
        self._dirty           = False
        self._lockAspectRatio = True
        self.sz = 0
        self.buffer = 0

    def isEditable(self):
        return True

    def type(self):
        return ElementType.IMAGE

    def setSize(self, s):
        self.sz = s

    def lockAspectRatio(self):
        return self._lockAspectRatio

    def setLockAspectRatio(self, v):
        self._lockAspectRatio = v

    def setPath(self, ss):
        self._ip = self.score().addImage(ss)

    def path(self):
        return self._ip.path()

    def reference(self):
        self._ip.reference()

    def dereference(self):
        self._ip.dereference()

    def draw(self, p):
        p.drawPixmap(0, 0, self.buffer)
        if self.selected() and not (self.score() and self.score().printing()):
            p.setBrush(Qt.NoBrush)
            p.setPen(QPen(Qt.blue, 0, Qt.SolidLine))
            p.drawRect(QRect(QPoint(), len(self.buffer)))

    def write(self, xml):
        xml.stag("Image")
        Element().writeProperties(xml)
        xml.tag("path", self.path())
        xml.tag("size", self.sz / GL.DPMM)
        if not self._lockAspectRatio:
            xml.tag("lockAspectRatio", self._lockAspectRatio)
        xml.etag()

    def read(self, e):
        e = e.firstChildElement()
        while not e.isNull():
            tag = QString(e.tagName())
            if tag == "path":
                self.setPath(e.text())
            elif tag == "size":
                self.sz = self.readSize(e)
                if self.score().mscVersion() >= 109:
                    self.sz = self.sz *  GL.DPMM
            elif tag == "lockAspectRatio":
                self._lockAspectRatio = e.text().toInt()
            elif not Element.readProperties(e):
                domError(e)
            e = e.nextSiblingElement()

    def bbox(self):
        return QRectF(0.0, 0.0, self.sz.width(), self.sz.height())

    def editDrag(self, curGrip, d):
        ratio = self.sz.width() / self.sz.height()
        if curGrip == 0:
            self.sz.setWidth(self.sz.width() + d.x())
            if self._lockAspectRatio:
                self.sz.setHeight(self.sz.width() / ratio)
        else:
            self.sz.setHeight(self.sz.height() + d.y())
            if self._lockAspectRatio:
                self.sz.setWidth(self.sz.height() * ratio)

    def updateGrips(self, grips, grip):
        grips = 2
        r = QRectF(self.abbox())
        grip[0].translate(QPointF(r.x() + r.width(), r.y() + r.height() * .5))
        grip[1].translate(QPointF(r.x() + r.width() * .5, r.y() + r.height()))


    def gripAnchor(self, i):
        return QPointF()

    def endEdit(self):
        pass


class RasterImage(Image):
    def __init__(self, s):
        Image.__init__(self, s)

    def clone(self):
        return self

    def draw(self, p):
        p.save()
        if self.score().printing():
            p.scale(self.sz.width() / self.doc.width(), self.sz.height() / self.doc.height())
            p.drawPixmap(0, 0, QPixmap.fromImage(self.doc))
        else:
            t = p.worldTransform()
            s = QSizeF(self.sz.width() * t.m11(), self.sz.height() * t.m22()).toSize()
            t.setMatrix(1.0, t.m12(), t.m13(), t.m21(), 1.0, t.m23(), t.m31(), t.m32(), t.m33())
            p.setWorldTransform(t)
            if len(self.buffer) != s or self._dirty:
                self.buffer = QPixmap.fromImage(self.doc.scaled(s, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
                self._dirty = False
            Image().draw(p)
        p.restore()

    def setPath(self, s):
        Image().setPath(s)
        if self._ip.loaded():
            self.doc.loadFromData(self._ip.buffer().buffer())
        else:
            self.doc.load(self.path())
        if not self.doc.isNull():
            self.sz = self.doc.size() * 0.4 * GL.DPI / GL.PDPI
            self._dirty = True


class SvgImage(Image):
    def __init__(self, s):
        Image.__init__(self, s)
        self.doc = 0

    def clone(self):
        return self

    def draw(self, painter):
        if not self.doc:
            painter.setBrush(Qt.NoBrush)
            painter.setPen(Qt.black)
            painter.drawRect(self.bbox())
        else:
            self.doc.render(painter, self.bbox())
        if self.selected() and not (self.score() and self.score().printing()):
            painter.setBrush(Qt.NoBrush)
            painter.setPen(Qt.blue)
            painter.drawRect(self.bbox())
            
    def setPath(self, s):
        Image.setPath(s)
        if self.doc == 0:
            self.doc = QSvgRenderer()
        if self._ip.loaded():
            self.doc.load(self._ip.buffer().buffer())
        else:
            self.doc.load(self.path())
        if self.doc.isValid():
            self.sz = self.doc.defaultSize()
            self._dirty = True
