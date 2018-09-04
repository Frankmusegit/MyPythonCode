#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from Note import *
from Element import *
from Image import *
from Segment import *

class CommandEvent(QEvent):
    def __init__(self, c):
        QEvent(QEvent.Type(QEvent.User+1))
        self.value = c

class ScoreView(QWidget):
    def __init__(self, parent = None):
        super(ScoreView, self).__init__(parent)
        self._score      = 0
        self.dropTarget  = 0
        self._editText   = 0
        self._matrix     = QTransform(GL.PDPI/GL.DPI, 0.0, 0.0, GL.PDPI/GL.DPI, 0.0, 0.0)
        self.imatrix     = self._matrix.inverted()
        self._magIdx     = MAG.MAG_100
        self.focusFrame  = 0
        self.level       = 0
        self.dragElement = 0
        self.curElement  = 0
        self._bgColor    = Qt.darkBlue
        self._fgColor    = Qt.white
        self.fgPixmap    = 0
        self.bgPixmap    = 0
        self.lasso       = 0
        self.cursor      = 0
        self.shadowNote  = 0
        self.grips       = 0
        self.origEditObject   = 0
        self.editObject  = 0
        self.sm          = QStateMachine(self)
        self.stateActive = QState()

    def dataChanged(self, r):
        self.redraw(r)

    def redraw(self, fr):
        self.update(self._matrix.mapRect(fr).toRect())

    def score(self):
        return self._score

    def setScore(self, s):
        self._score = s
        if self.cursor == 0:
            self.cursor = Cursor(self._score, self)
            self.shadowNote = ShadowNote(self._score)
            self.cursor.setVisible(False)
            self.shadowNote.setVisible(False)
        else:
            self.cursor.setScore(self._score)
            self.shadowNote.setScore(self._score)
        self.connect(s, SIGNAL("updateAll()"), self.update)
        self.connect(s, SIGNAL("dataChanged(QRectF)"), self.dataChanged)

    def paintElement(self, data, e):
        p = QPainter(data)
        p.save()
        p.setPen(QPen(e.curColor()))
        p.translate(e.canvasPos())
        e.draw(p)
        p.restore()


    def paintEvent(self, ev):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, preferences.antialiasedDrawing)
        p.setRenderHint(QPainter.TextAntialiasing, True)

        self.paint(ev.rect(), p)

        p.setTransform(self._matrix)
        p.setClipping(False)

        self.cursor.draw(p)
        self.lasso.draw(p)
        self.shadowNote.draw(p)
        if not self.dropAnchor.isNull():
            pen = QPen(QBrush(QColor(80, 0, 0)), 2.0 / p.worldMatrix().m11(), Qt.DotLine)
            p.setPen(pen)
            p.drawLine(self.dropAnchor)
        if self.dragElement:
            self.dragElement.scanElements(p, self.paintElement)
            
    def paint(self, rr, p):
        p.save()
        if self.fgPixmap == 0 or self.fgPixmap.isNull():
            p.fillRect(rr, self._fgColor)
        else:
            p.drawTiledPixmap(rr, self.fgPixmap, rr.topLeft() - QPoint(self._matrix.dx(), self._matrix.dy()))

        p.setTransform(self._matrix)
        fr = self.imatrix.mapRect(QRectF(rr))

        r1 = QRegion(rr)
        for page in self._score.pages():
            pr = QRectF(page.abbox())
            r1 = r1 - self._matrix.mapRect(pr).toAlignedRect()

        ell = self._score.items(fr)
        qStableSort(ell.begin(), ell.end(), self.elementLessThan)
        self.drawElements(p, ell)

        if self.dropRectangle.isValid():
            p.fillRect(self.dropRectangle, QColor(80, 0, 0, 80))

        if self._editText:
            r = self._editText.abbox()
            w = 6.0 / self.matrix().m11()
            r.adjust(-w, -w, w, w)
            w = 2.0 / self.matrix().m11()
            p.setPen(QPen(QBrush(Qt.blue), w))
            p.setBrush(QBrush(Qt.NoBrush))
            p.drawRect(r)

        if self.grips:
            lw = 2.0/p.matrix().m11()
            pen = QPen(preferences.defaultColor)
            pen.setWidthF(lw)
            p.setPen(pen)
            for i in range(0, self.grips):
                if i == self.curGrip and self.hasFocus():
                     p.setBrush(QBrush(Qt.blue))
                else:
                     p.setBrush(QBrush(Qt.NoBrush))
                p.drawRect(self.grip[i])

        sel = self._score.selection()

        if sel.state() == SelState.SEL_RANGE:
            ss = sel.startSegment()
            es = sel.endSegment()
            if not ss:
                  return
            p.setBrush(Qt.NoBrush)

            pen = QPen(Qt.blue)
            pen.setWidthF(2.0 / p.matrix().m11())

            pen.setStyle(Qt.SolidLine)

            p.setPen(pen)
            _spatium = self.score().spatium()
            x2      = ss.canvasPos().x() - _spatium
            staffStart = sel.staffStart()
            staffEnd   = sel.staffEnd()

            system2 = ss.measure().system()
            pt      = ss.canvasPos()
            y        = pt.y()
            ss1   = system2.staff(staffStart)
            ss2   = system2.staff(staffEnd - 1)
            y1       = ss1.y() - 2 * _spatium + y
            y2       = ss2.y() + ss2.bbox().height() + 2 * _spatium + y

            p.drawLine(QLineF(x2, y1, x2, y2))

            system1 = system2
            x1 = 0.0
            s = ss
            while s and s != es:
                ns = s.next1()
                system1  = system2
                system2  = s.measure().system()
                pt       = s.canvasPos()
                x1  = x2
                x2  = pt.x() + _spatium * 2

                if ns == 0 or ns == es:
                    e = s.element(staffStart * VOICES)
                    if e and e.type() == ElementType.REST and e.duration().type() == DurationType.V_MEASURE:
                        x2 = s.measure().abbox().right() - _spatium
                if system2 != system1:
                    x1  = x2 - 2 * _spatium
                y   = pt.y()
                ss1 = system2.staff(staffStart)
                ss2 = system2.staff(staffEnd - 1)
                y1  = ss1.y() - 2 * _spatium + y
                y2  = ss2.y() + ss2.bbox().height() + 2 * _spatium + y
                p.drawLine(QLineF(x1, y1, x2, y1))
                p.drawLine(QLineF(x1, y2, x2, y2))
                s = ns
            p.drawLine(QLineF(x2, y1, x2, y2))

        p.setMatrixEnabled(False)
        if not r1.isEmpty():
            p.setClipRegion(r1)
            if self.bgPixmap == 0 or self.bgPixmap.isNull():
                p.fillRect(rr, self._bgColor)
            else:
                p.drawTiledPixmap(rr, self.bgPixmap, rr.topLeft() - QPoint(self._matrix.m31(), self._matrix.m32()))
        p.restore()
        
    def event(self, event):
        if event.type() == QEvent.KeyPress and self.editObject:
            ke = event
            if ke.key() == Qt.Key_Tab or ke.key() == Qt.Key_Backtab:
                if self.editObject.isTextB():
                    return True
                rv = True
                if ke.key() == Qt.Key_Tab:
                    self.curGrip = self.curGrip + 1
                    if self.curGrip >= self.grips:
                        self.curGrip = 0
                        rv = False
                        self.updateGrips()
                        self._score.end()
                        if self.curGrip:
                            return True
                        elif ke.key() == Qt.Key_Backtab:
                            self.curGrip = self.curGrip - 1
                            if self.curGrip < 0:
                                self.curGrip = self.grips - 1
                                rv = False
                        self.updateGrips()
                        self._score.end()
                        if rv:
                            return True
        return QWidget().event(event)

    def resizeEvent(self, QResizeEvent):
        if self._magIdx == MAG.MAG_PAGE_WIDTH or self._magIdx == MAG.MAG_PAGE or self._magIdx == MAG.MAG_DBL_PAGE:
            m = GL.mscore.getMag(self)
            self.setMag(m)
        self.update()
        
    def wheelEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            QApplication.sendPostedEvents(self, 0)
            self.zoom(event.delta() / 120, event.pos())
            return

        dx = 0
        dy = 0
        if event.modifiers() & Qt.ShiftModifier or event.orientation() == Qt.Horizontal:
            n = self.width() / 10
            if n < 2:
                n = 2
            dx = event.delta() * n / 120
        else:
            n = self.height() / 10
            if n < 2:
                n = 2
            dy = event.delta() * n / 120

        self._matrix.setMatrix(self._matrix.m11(), self._matrix.m12(), self._matrix.m13(), self._matrix.m21(),
         self._matrix.m22(), self._matrix.m23(), self._matrix.dx()+dx, self._matrix.dy()+dy, self._matrix.m33())
        self.imatrix = self._matrix.inverted()

        self.scroll(dx, dy, QRect(0, 0, self.width(), self.height()))
        self.viewRectChanged()

    def dragEnterEvent(self, event):
        _spatium = self.score().spatium()
        self.dragElement = 0

        data = event.mimeData()

        if data.hasFormat(mimeSymbolListFormat) or data.hasFormat(mimeStaffListFormat):
            event.acceptProposedAction()
            return

        if data.hasFormat(mimeSymbolFormat):
            event.acceptProposedAction()

            a = data.data(mimeSymbolFormat)

            doc = QDomDocument()
            line = 0
            column = 0
            err = QString()
            (ok, err, line, column) = doc.setContent(a)
            if not ok:
                print "error reading drag data at %d/%d: %s\n<%s>\n" %(line, column, err.toLatin1().data(), a.data())
                return
            docName = "--"
            e = doc.documentElement()

            dragOffset = QPoint()

            type = Element().readType(e, dragOffset, self.duration)

            el = Element(None)
            if type == ElementType.IMAGE:
                path = QString()
                ee = e.firstChildElement()
                while not ee.isNull():
                    tag = QString(ee.tagName())
                    if tag == "path":
                        path = ee.text()
                        break
                    ee = ee.nextSiblingElement()
                image = Image(None)
                lp = QString(path.toLower())

                if lp.endsWith(".svg"):
                    image = SvgImage(self.score())
                elif lp.endsWith(".jpg") or lp.endsWith(".png") or lp.endsWith(".gif") or lp.endsWith(".xpm"):
                    image = RasterImage(self.score())
                else:
                    print "unknown image format <%s>\n" %path.toLatin1().data()
                el = image
            elif type == ElementType.SLUR or\
                  type == ElementType.VOLTA or\
                  type == ElementType.OTTAVA or \
                  type == ElementType.TRILL or \
                  type == ElementType.PEDAL or \
                  type == ElementType.HAIRPIN or \
                  type == ElementType.TEXTLINE or \
                  type == ElementType.KEYSIG or \
                  type == ElementType.CLEF or \
                  type == ElementType.TIMESIG or \
                  type == ElementType.BREATH or \
                  type == ElementType.GLISSANDO or \
                  type == ElementType.ARTICULATION or \
                  type == ElementType.ACCIDENTAL or \
                  type == ElementType.DYNAMIC or \
                  type == ElementType.TEXT or \
                  type == ElementType.TEMPO_TEXT or \
                  type == ElementType.STAFF_TEXT or \
                  type == ElementType.NOTEHEAD or \
                  type == ElementType.TREMOLO or \
                  type == ElementType.LAYOUT_BREAK or \
                  type == ElementType.MARKER or \
                  type == ElementType.JUMP or \
                  type == ElementType.REPEAT_MEASURE or \
                  type == ElementType.ICON or \
                  type == ElementType.NOTE or \
                  type == ElementType.SYMBOL or \
                  type == ElementType.CHORD or \
                  type == ElementType.SPACER or \
                  type == ElementType.ACCIDENTAL_BRACKET:
                el = Element().create(type, self.score())
            elif type == ElementType.BAR_LINE or type == ElementType.ARPEGGIO or type == ElementType.BRACKET:
                el = Element().create(type, self.score())
                el.setHeight(_spatium * 5)
            else:
                print "dragEnter %s\n" %Element().name(type)

            if el:
                self.dragElement = el
                self.dragElement.setParent(None)
                self.dragElement.read(e)
                self.dragElement.layout()
            return

        if data.hasUrls():
            ul = data.urls()
            for u in ul:
                if u.scheme() == "file":
                    fi = QFileInfo(u.path())
                    suffix = QString(fi.suffix().toLower())
                    if suffix == "svg" or suffix == "jpg" or suffix == "png" or suffix == "gif" or suffix == "xpm":
                        event.acceptProposedAction()
            return
        s = QString(self.tr("unknown drop format: formats %1:\n").arg(data.hasFormat(mimeSymbolFormat)))

        for ss in data.formats():
            s = s +  (QString("   <%1>\n").arg(ss))
        QMessageBox.warning(0, "Drop:", s, QString.null, "Quit", QString.null, 0, 1)

    def dragLeaveEvent(self):
        if self.dragElement:
            self._score.setLayoutAll(False)
            self._score.addRefresh(self.dragElement.abbox())
            del self.dragElement
            self.dragElement = 0
            self._score.end()
        self.setDropTarget(0)

    def dragMoveEvent(self, event):

        event.acceptProposedAction()

        pos = QPointF(self.imatrix.map(QPointF(event.pos())))

        if self.dragElement:
            if self.dragElement.type() == ElementType.VOLTA:
                self.dragMeasureAnchorElement(pos)
            elif self.dragElement.type() == ElementType.PEDAL or\
                self.dragElement.type() == ElementType.DYNAMIC or \
                self.dragElement.type() == ElementType.OTTAVA or \
                self.dragElement.type() == ElementType.TRILL or \
                self.dragElement.type() == ElementType.HAIRPIN or \
                self.dragElement.type() == ElementType.TEXTLINE:
                self.dragTimeAnchorElement(pos)
            elif self.dragElement.type() == ElementType.IMAGE or \
                self.dragElement.type() == ElementType.SYMBOL:
                self.dragSymbol(pos)
            elif self.dragElement.type() == ElementType.KEYSIG or\
                self.dragElement.type() == ElementType.CLEF or \
                self.dragElement.type() == ElementType.TIMESIG or \
                self.dragElement.type() == ElementType.BAR_LINE or \
                self.dragElement.type() == ElementType.ARPEGGIO or \
                self.dragElement.type() == ElementType.BREATH or \
                self.dragElement.type() == ElementType.GLISSANDO or \
                self.dragElement.type() == ElementType.BRACKET or \
                self.dragElement.type() == ElementType.ARTICULATION or \
                self.dragElement.type() == ElementType.ACCIDENTAL or \
                self.dragElement.type() == ElementType.TEXT or \
                self.dragElement.type() == ElementType.TEMPO_TEXT or\
                self.dragElement.type() == ElementType.STAFF_TEXT or\
                self.dragElement.type() == ElementType.NOTEHEAD or\
                self.dragElement.type() == ElementType.TREMOLO or\
                self.dragElement.type() == ElementType.LAYOUT_BREAK or\
                self.dragElement.type() == ElementType.MARKER or\
                self.dragElement.type() == ElementType.JUMP or\
                self.dragElement.type() == ElementType.REPEAT_MEASURE or\
                self.dragElement.type() == ElementType.ICON or\
                self.dragElement.type() == ElementType.CHORD or\
                self.dragElement.type() == ElementType.SPACER or\
                self.dragElement.type() == ElementType.SLUR or\
                self.dragElement.type() == ElementType.ACCIDENTAL_BRACKET:
                el = self.elementsAt(pos)
                found = False
                for e in el:
                    if e.acceptDrop(self, pos, self.dragElement.type(), self.dragElement.subtype()):
                        if e.type() != ElementType.MEASURE:
                            self.setDropTarget(e)
                            found = True
                if not found:
                    self.setDropTarget(0)
            else:
                pass
            w = 8.0 / self.matrix().m11()
            self.score().addRefresh(self.dragElement.abbox().adjusted(-w, -w, w, w))
            self.dragElement.setPos(pos - self.dragOffset)
            self.score().addRefresh(self.dragElement.abbox().adjusted(-w, -w, w, w))
            self._score.end()
            return

        if event.mimeData().hasUrls():
            ul = event.mimeData().urls()
            u = ul.front()
            if u.scheme() == "file":
                fi = QFileInfo(u.path())
                suffix = QString(fi.suffix().toLower())
                if suffix != "svg" and suffix != "jpg" and suffix != "png" and suffix != "gif" and suffix != "xpm":
                    return
                el = self.elementAt(pos)
                if el and (el.type() == ElementType.NOTE or el.type() == ElementType.REST):
                    self.setDropTarget(el)
                else:
                    self.setDropTarget(0)
            self._score.end()
            return
        md = event.mimeData()
        data = QByteArray()
        if md.hasFormat(mimeSymbolListFormat):
            etype = ElementType.ELEMENT_LIST
            data = md.data(mimeSymbolListFormat)
        elif md.hasFormat(mimeStaffListFormat):
            etype = ElementType.STAFF_LIST
            data = md.data(mimeStaffListFormat)
        else:
            self._score.end()
            return
        el = self.elementAt(pos)
        if el == 0 or el.type() != ElementType.MEASURE:
            self._score.end()
            return
        elif etype == ElementType.ELEMENT_LIST:
            print "accept drop element list\n"
        elif etype == ElementType.STAFF_LIST or etype == ElementType.MEASURE_LIST:
            pass
        self._score.end()

    def dropEvent(self, event):
        pos = QPointF(self.imatrix.map(QPointF(event.pos())))

        if self.dragElement:
            self._score.startCmd()
            self.dragElement.setScore(self._score)
            self._score.addRefresh(self.dragElement.abbox())
            if self.dragElement.type() == ElementType.VOLTA or\
               self.dragElement.type() == ElementType.OTTAVA or \
               self.dragElement.type() == ElementType.TRILL or\
               self.dragElement.type() == ElementType.PEDAL or\
               self.dragElement.type() == ElementType.DYNAMIC or\
               self.dragElement.type() == ElementType.HAIRPIN or\
               self.dragElement.type() == ElementType.TEXTLINE:
                self.dragElement.setScore(self.score())
                self.score().cmdAdd1(self.dragElement, pos, self.dragOffset)
                self.event.acceptProposedAction()
            elif self.dragElement.type() == ElementType.SYMBOL or\
                  self.dragElement.type() == ElementType.IMAGE:
                el = self.elementAt(pos)
                if el == 0:
                    staffIdx = -1
                    seg = Segment()
                    tick = 0
                    el = self._score.pos2measure(pos, tick, staffIdx, 0, seg, 0)
                    if el == 0:
                        print "cannot drop here\n"
                        del self.dragElement

                self._score.addRefresh(el.abbox())
                self._score.addRefresh(self.dragElement.abbox())
                dropElement = el.drop(self, pos, self.dragOffset, self.dragElement)
                self._score.addRefresh(el.abbox())
                if dropElement:
                    self._score.select(dropElement, SelectType.SELECT_SINGLE, 0)
                    self._score.addRefresh(dropElement.abbox())
                    event.acceptProposedAction()
            elif self.dragElement.type() == ElementType.KEYSIG or\
                  self.dragElement.type() == ElementType.CLEF or\
                  self.dragElement.type() == ElementType.TIMESIG or\
                  self.dragElement.type() == ElementType.BAR_LINE or\
                  self.dragElement.type() == ElementType.ARPEGGIO or\
                  self.dragElement.type() == ElementType.BREATH or\
                  self.dragElement.type() == ElementType.GLISSANDO or\
                  self.dragElement.type() == ElementType.BRACKET or\
                  self.dragElement.type() == ElementType.ARTICULATION or\
                  self.dragElement.type() == ElementType.ACCIDENTAL or\
                  self.dragElement.type() == ElementType.TEXT or\
                  self.dragElement.type() == ElementType.TEMPO_TEXT or\
                  self.dragElement.type() == ElementType.STAFF_TEXT or\
                  self.dragElement.type() == ElementType.NOTEHEAD or\
                  self.dragElement.type() == ElementType.TREMOLO or\
                  self.dragElement.type() == ElementType.LAYOUT_BREAK or\
                  self.dragElement.type() == ElementType.MARKER or\
                  self.dragElement.type() == ElementType.JUMP or\
                  self.dragElement.type() == ElementType.REPEAT_MEASURE or\
                  self.dragElement.type() == ElementType.ICON or\
                  self.dragElement.type() == ElementType.NOTE or\
                  self.dragElement.type() == ElementType.CHORD or\
                  self.dragElement.type() == ElementType.SPACER or\
                  self.dragElement.type() == ElementType.SLUR or\
                  self.dragElement.type() == ElementType.ACCIDENTAL_BRACKET:
                el = Element()
                for e in self.elementsAt(pos):
                    if e.acceptDrop(self, pos, self.dragElement.type(), self.dragElement.subtype()):
                        el = e
                        break
                if not el:
                    print "cannot drop here\n"
                    del self.dragElement
                self._score.addRefresh(el.abbox())
                self._score.addRefresh(self.dragElement.abbox())
                dropElement = el.drop(self, pos, self.dragOffset, self.dragElement)
                self._score.addRefresh(el.abbox())
                if dropElement:
                    if not self._score.noteEntryMode():
                        self._score.select(dropElement, SelectType.SELECT_SINGLE, 0)
                        self._score.addRefresh(dropElement.abbox())
                        event.acceptProposedAction()
            else:
                del self.dragElement

            self.dragElement = 0
            self.setDropTarget(0)
            self.score().endCmd()
            return

        if event.mimeData().hasUrls():
            ul = event.mimeData().urls()
            u = ul.front()
            if u.scheme() == "file":
                fi = QFileInfo(u.path())
                s = Image()
                suffix = fi.suffix().toLower()
                if suffix == "svg":
                    s = SvgImage(self.score())
                elif suffix == "jpg" or suffix == "png" or suffix == "gif" or suffix == "xpm":
                    s = RasterImage(self.score())
                else:
                    return
                self._score.startCmd()
                s.setPath(u.toLocalFile())

                el = self.elementAt(pos)
                if el and (el.type() == ElementType.NOTE or el.type() == ElementType.REST):
                    s.setTrack(el.track())
                    if el.type() == ElementType.NOTE:
                        note = el
                        s.setTick(note.chord().tick())
                        s.setParent(note.chord().segment().measure())
                    else:
                        rest = el
                        s.setTick(rest.tick())
                        s.setParent(rest.segment().measure())
                        self.score().undoAddElement(s)
                else:
                    self.score().cmdAddBSymbol(s, pos, self.dragOffset)

                event.acceptProposedAction()
                self.score().endCmd()
                self.setDropTarget(0)
                return
            return

        md = event.mimeData()
        data = QFileInfo()
        if md.hasFormat(mimeSymbolListFormat):
            etype = ElementType.ELEMENT_LIST
            data = md.data(mimeSymbolListFormat)
        elif md.hasFormat(mimeStaffListFormat):
            etype = ElementType.STAFF_LIST
            data = md.data(mimeStaffListFormat)
        else:
            print "cannot drop this object: unknown mime type\n"
            sl = md.formats()
            for s in sl:
                print "  %s\n" %s.toAscii().data()
            self._score.end()
            return


        doc = QDomDocument()

        (ok, err, line, column) = doc.setContent(data)
        if not ok:
            qWarning("error reading drag data at %d/%d: %s\n   %s\n" %(line, column, err.toAscii().data(), data.data()))
            return
        docName = "--"
        el = self.elementAt(pos)
        if el == 0 or el.type() != ElementType.MEASURE:
            self.setDropTarget(0)
            return
        measure = el

        if etype == ElementType.ELEMENT_LIST:
            print "drop element list\n"
        elif etype == ElementType.MEASURE_LIST or etype == ElementType.STAFF_LIST:
            self._score.startCmd()
            s = measure.system()
            idx   = s.y2staff(pos.y())
            if idx != -1:
                seg = measure.first()
                while seg.subtype() != SegmentType.SegChordRest:
                    seg = seg.next()
                self.score().pasteStaff(doc.documentElement(), seg.element(idx * VOICES))
            event.acceptProposedAction()
            self._score.setLayoutAll(True)
            self._score.endCmd()
        self.setDropTarget(0)

    def dragLeaveEvent(self, QDragLeaveEvent):
        if self.dragElement:
            self._score.setLayoutAll(False)
            self._score.addRefresh(self.dragElement.abbox())
            del self.dragElement
            self.dragElement = 0
            self._score.end()
        self.setDropTarget(0)
