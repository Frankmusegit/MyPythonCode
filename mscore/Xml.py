#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtXml import *

docName = QString()

def getSharePath():
      dir = QDir(QCoreApplication.applicationDirPath())
      return dir.absolutePath()


def readPoint(e):
    p = QPointF()
    x, ok = e.attribute("x", "0.0").toDouble()
    p.setX(x)
    y, ok = e.attribute("y", "0.0").toDouble()
    p.setY(y)
    return p

def readColor(e):
    c = QColor()
    c.setRed(e.attribute("r").toInt())
    c.setGreen(e.attribute("g").toInt())
    c.setBlue(e.attribute("b").toInt())
    return c

def readSize(e):
    p = QSizeF()
    p.setWidth(e.attribute("w", "0.0").toDouble())
    p.setHeight(e.attribute("h", "0.0").toDouble())
    return p

def readRectF(e):
    p =  QRectF()
    x, ok = e.attribute("x", "0.0").toDouble()
    p.setX(x)
    y, ok = e.attribute("y", "0.0").toDouble()
    p.setY(y)
    w, ok = e.attribute("w", "0.0").toDouble()
    p.setWidth(w)
    h, ok = e.attribute("h", "0.0").toDouble()
    p.setWidth(h)
    return p

def domElementPath(e):
    s = QString()
    dn = QDomNode(e)
    while not dn.parentNode().isNull():
        dn = dn.parentNode()
        e = dn.toElement()
        k = QString(e.tagName())
        if not s.isEmpty():
            s += ":"
            s += k
    return s

def domError(e):
    s = QString(domElementPath(e))
    if not docName.isEmpty():
        print "<%s>:" %docName.toAscii().constData()
    ln = e.lineNumber()
    if ln != -1:
        print "line:%d " %ln
    col = e.columnNumber()
    if col != -1:
        print "col:%d " %col
    print "%s: Unknown Node <%s>, type %d\n" %(s.toAscii().constData(), e.tagName().toAscii().constData(), e.nodeType())
    if e.isText():
        print "  text node <%s>\n"  %e.toText().data().toAscii().constData()

class Prop:
    def __init__(self, n, d):
        self.name = n
        self.data = d

class Xml(QTextStream):

    def __init__(self, device = None):
        super(QTextStream, self).__init__(device)
        self.setCodec("utf8")
        self.BS = 2048
        self.stack = []

    def putLevel(self):
        level = len(self.stack)
        for i in range(0, level * 2):
            self << ' '

    def header(self):
        self << "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"

    def stag(self, s):
        self.putLevel()
        self << '<'
        self << s
        self << '>'
        endl(self)
        self.stack.append(s.split(' ')[0])

    def etag(self):
        self.putLevel()
        self << "</"
        self << self.stack[len(self.stack)-1]
        self << '>'
        endl(self)

    def tagE(self, s):
        self.putLevel()
        self << '<'
        self << s
        self << "/>\n"

    def ntag(self, name):
        self.putLevel()
        self << "<"
        self << name
        self << ">"

    def netag(self, s):
        self << "</"
        self << s
        self << '>'
        endl(self)

    def tag(self, name, data):
        ename = QString(name.split(' ')[0])
        self.putLevel()
        if data.type() == QVariant.Bool or data.type() == QVariant.Char or data.type() == QVariant.Int or data.type() == QVariant.UInt:
            self << "<"
            self << name
            self << ">"
            (res, ok) =  data.toInt()
            if ok:
                self << res
            self << "</"
            self << ename
            self << ">\n"
        elif data.type() == QVariant.Double:
            self << "<"
            self << name
            self << ">"
            self << data.value()
            self << "</"
            self << ename
            self << ">\n"
        elif data.type() == QVariant.String:
            self << "<"
            self << name
            self << ">"
            self << self.xmlString(data.value<QString>())
            self << "</"
            self << ename
            self << ">\n"
        elif data.type() == QVariant.Color:
            color = QColor(data.value<QColor>())
            self << QString("<%1 r=\"%2\" g=\"%3\" b=\"%4\"/>\n").arg(name).arg(color.red()).arg(color.green()).arg(color.blue())
        elif data.type() == QVariant.Color.Rect:
            r = QRect(data.value<QRect>())
            self << QString("<%1 x=\"%2\" y=\"%3\" w=\"%4\" h=\"%5\"/>\n").arg(name).arg(r.x()).arg(r.y()).arg(r.width()).arg(r.height())
        elif data.type() == QVariant.Color.RectF:
            r = QRectF(data.value<QRectF>())
            self << QString("<%1 x=\"%2\" y=\"%3\" w=\"%4\" h=\"%5\"/>\n").arg(name).arg(r.x()).arg(r.y()).arg(r.width()).arg(r.height())
        elif data.type() == QVariant.Color.PointF:
            p = QPointF(data.value<QPointF>())
            self << QString("<%1 x=\"%2\" y=\"%3\"/>\n").arg(name).arg(p.x()).arg(p.y())
        elif data.type() == QVariant.SizeF:
            p = QSizeF(data.value<QSizeF>())
            self << QString("<%1 w=\"%2\" h=\"%3\"/>\n").arg(name).arg(p.width()).arg(p.height())
        else:
            print "Xml::tag: unsupported type %d\n" %data.type()

    def tag1(self, name, g):
        self.tag(name, QRect(g.pos(), g.size()))

    def tag2(self, name, s):
        self.tag(name, QVariant(s))

    def xmlString(self, ss):
        s =  QString(ss)
        s.replace('&',  "&amp;")
        s.replace('<',  "&lt;")
        s.replace('>',  "&gt;")
        s.replace('\'', "&apos;")
        s.replace('"',  "&quot;")
        return s

    def dump(self, leng, p):
        self.putLevel()
        col = 0
        self.setFieldWidth(5)
        self.setNumberFlags(self.numberFlags() | QTextStream.ShowBase)
        self.setIntegerBase(16)
        for i in range(0, leng):
            if col >= 16:
                self.setFieldWidth(0)
                endl(self)
                col = 0
                self.putLevel()
                self.setFieldWidth(5)
            self << (p[i] & 0xff)
            col = col + 1
        if col:
            self << endl << dec
        self.setFieldWidth(0)
        self.setIntegerBase(10)

    def htmlToString(self, e, level):
        s = QString()
        s = s + QString("<%1").arg(e.tagName())
        map = e.attributes()
        n = map.size()
        for i in range(0, n):
            a = map.item(i).toAttr()
            s = s + QString(" %1=\"%2\"").arg(a.name()).arg(a.value())
        s = s + ">"
        level = level + 1
        ee = e.firstChild()
        while not ee.isNull():
            if ee.nodeType() == QDomNode.ElementNode:
                self.htmlToString(ee.toElement(), level, s)
            elif ee.nodeType() == QDomNode.TextNode:
                s = s + Qt.escape(ee.toText().data())
            ee = ee.nextSibling()
        s = s + QString("</%1>").arg(e.tagName())
        level = level - 1
        return s

    def htmlToString1(self, e):
        return self.htmlToString(e, 0)

    def writeHtml(self, s):
        sl = QStringList(s.split("\n"))
        for i in range(1, sl.size()):
            self << sl[i] << "\n"
