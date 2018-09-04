#!/usr/bin/env python
#-*- coding:utf-8 -*-

from palette_ui import *
from cellproperties import *
from Symbol import *
from Xml import *
from Image import *
from Style import *

def needsStaff(e):
    if e == 0:
        return False
    if e.type() == (ElementType.CHORD or ElementType.BAR_LINE or ElementType.CLEF or  ElementType.KEYSIG or ElementType.REST):
        return True
    else:
        return False


def applyDrop(score,  viewer, target, e):
    pt = QPointF()
    if target.acceptDrop(viewer, pt, e.type(), e.subtype()):
        ne = e.clone()
        ne.setScore(score)
        ne = target.drop(viewer, pt, pt, ne)
        if ne:
            score.select(ne, SelectType.SELECT_SINGLE, 0)
            viewer.setDropTarget(0)

def paintPaletteElement(data, e):
    p = QPainter(data)
    p.save()
    p.translate(e.pos())
    e.draw(p)
    p.restore()

class Palette(QWidget):
    changed = pyqtSignal()
    startDragElement = pyqtSignal(Element)
    def __init__(self, parent = None):
        super(Palette, self).__init__(parent)
        self.extraMag      = 1.0
        self.currentIdx    = -1
        self.selectedIdx   = -1
        self._yOffset      = 0.0
        self.hgrid         = 50
        self.vgrid         = 60
        self._drawGrid     = False
        self._selectable   = False
        self._drumPalette  = False
        self.setMouseTracking(True)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.setReadOnly(True)
        self.cells = list()

    def element(self, idx):
        return self.cells[idx].element

    def setDrawGrid(self, val):
        self._drawGrid = val

    def drawGrid(self):
        return self._drawGrid

    def setName(self, s):
        self._name = s

    def name(self):
        return self._name

    def columns(self):
        return self.width() / self.hgrid

    def setGrid(self, hh, vv):
        self.hgrid = hh
        self.vgrid = vv

    def setSelectable(self, val):
        self._selectable = val

    def selectable(self):
        return self._selectable

    def getSelectedIdx(self):
        return self.selectedIdx

    def setSelected(self, idx):
        self. selectedIdx = idx

    def resizeWidth(self, w):
        c = w / self.hgrid
        if c <= 0:
            c = 1
        r = (len(self.cells) + c - 1) / c
        if r <= 0:
             r = 1
        h = r * self.vgrid
        self.setFixedSize(w, h)
        return h

    def readOnly(self):
        return self._readOnly

    def setReadOnly(self, val):
        self._readOnly = val
        self.setAcceptDrops( not val)

    def setMag(self,val):
        self.extraMag = val

    def mag(self):
        return self.extraMag

    def setYOffset(self, val):
        self._yOffset = val

    def yOffset(self):
        return self._yOffset

    def size(self):
        return len(self.cells)

    def drumPalette(self):
        return self._drumPalette

    def setDrumPalette(self, val):
        self._drumPalette = val

    def gridWidth(self):
        return self.hgrid

    def gridHeight(self):
        return self.vgrid

    def idx(self, p):
        x = p.x()
        y = p.y()

        row = y / self.vgrid
        col = x / self.hgrid

        nc = self.columns()
        if col > nc:
            return -1
        idx = row * nc + col
        if idx >= len(self.cells):
            return -1
        return idx

    def idxRect(self, i):
        if i == -1:
            return QRect()
        if self.columns() == 0:
            return QRect()
        cc = i % self.columns()
        cr = i % self.columns()
        return QRect(cc * self.hgrid, cr * self.vgrid, self.hgrid, self.vgrid)


    def contextMenuEvent(self, event):
        if self.readOnly:
            return
        i = self.idx(event.pos())
        if i == -1:
            return
        menu = QMenu()
        deleteAction = menu.addAction(self.tr("Delete Contents"))
        contextAction = menu.addAction(self.tr("Properties..."))
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == deleteAction:
            cell = self.cells[i]
            if cell:
                del cell.element
            del cell
            if len(self.cells) == i+1:
                self.cells.remove(i)
            else:
                self.cells[i] = 0
            self.update()
            self.changed.emit()
        elif action == contextAction:
            c = self.cells[i]
            if c == 0:
                return
            cell = PaletteCell(c)
            props = PaletteCellProperties(cell)
            if props.exec_():
                self.cells[i] = cell
                self.update()
                self.changed.emit()

    def actionToggled(self):
        self.selectedIdx = -1
        nn = len(self.cells)
        for n in range(0, nn):
            e = self.cells[n].element
            if e and e.type() == ElementType.ICON:
                if e.action().isChecked():
                    self.selectedIdx = n
                    break
        self.update()


    def mousePressEvent(self, ev):
        self.dragStartPosition = ev.pos()
        if self._selectable:
            i = self.idx(self.dragStartPosition)
            if i == -1:
                return
            if i != self.selectedIdx:
                self.update(self.idxRect(i) | self.idxRect(self.selectedIdx))
                self.selectedIdx = i
                self.boxClicked.emit(i)
            if self._drumPalette and GL.mscore.playEnabled():
                cs    = GL.mscore.currentScore()
                staffIdx = cs.inputTrack() / VOICES
                part   = cs.part(staffIdx)

                cell = self.cells[i]
                ch         = self.cell.element
                note        = ch.downNote()

                ticks   = preferences.defaultPlayDuration
                pitch   = note.pitch()
                GL.seq.startNote(part.channel(0), pitch, 80, ticks, 0.0)

    def mouseDoubleClickEvent(self, ev):
        i = self.idx(ev.pos())
        if i == -1:
            return
        score   = GL.mscore.currentScore()
        if score == 0:
            return
        sel = score.selection()

        if sel.state() == SelState.SEL_NONE:
            return

        mimeData = QMimeData()
        element    = self.cells[i].element
        if element == 0:
            return
        viewer      = GL.mscore.currentScoreView()
        mimeData.setData(mimeSymbolFormat, element.mimeData(QPointF()))
        score.startCmd()
        if sel.state() == SelState.SEL_LIST:
            for e in sel.elements():
                applyDrop(score, viewer, e, element)
        elif sel.state() == SelState.SEL_RANGE:
            track1 = sel.staffStart() * VOICES
            track2 = sel.staffEnd() * VOICES
            ss = sel.startSegment()
            es = sel.endSegment()
            s = ss
            while (s and s != es):
                for track in range(track1, track2):
                    e = s.element(track)
                    if e == 0:
                        continue
                    if e.type() == ElementType.CHORD:
                        chord = e
                        for n in chord.notes():
                            applyDrop(score, viewer, n, element)
                    else:
                        applyDrop(score, viewer, e, element)
                s = s.next1()
        else:
            print "unknown selection state\n"
        score.endCmd()

    def mouseMoveEvent(self, ev):
        if ((self.currentIdx != -1) and (ev.buttons() & Qt.LeftButton) and (ev.pos() - self.dragStartPosition).manhattanLength() > QApplication.startDragDistance()):
            drag = QDrag(self)
            mimeData = QMimeData()
            if self.cells[self.currentIdx]:
                el  = self.cells[self.currentIdx].element
                ir     = self.idxRect(self.currentIdx)
                mag    = PALETTE_SPATIUM * self.extraMag / GL.gscore.spatium()
                spos = QPointF(self.dragStartPosition) / mag
                spos = spos - QPointF(self.cells[self.currentIdx].x, self.cells[self.currentIdx].y)
                spos.setX(0.0)
                mimeData.setData(mimeSymbolFormat, el.mimeData(spos))
                drag.setMimeData(mimeData)
                dragSrcIdx = self.currentIdx
                self.startDragElement(el)
                if self._readOnly:
                    drag.start(Qt.CopyAction)
                else:
                    drag.start(Qt.CopyAction | Qt.MoveAction)
        else:
            if self.currentIdx != -1:
                r = self.idxRect(self.currentIdx)
            self.currentIdx = self.idx(ev.pos())
            if self.currentIdx != -1:
                if self.cells[self.currentIdx] == 0:
                    self.currentIdx = -1
                else:
                    r = r | self.idxRect(self.currentIdx)
            self.update(r)

    def leaveEvent(self, QEvent):
        if self.currentIdx != -1:
            r = self.idxRect(self.currentIdx)
            self.currentIdx = -1
            self.update(r)

    def append(self, symIdx):
        if not GL.symbols[symIdx].isValid():
            return
        s = Symbol(GL.gscore)
        s.setSym(symIdx)
        self.append1(s, qApp.translate("symbol", GL.symbols[symIdx].name()))

    def append1(self, s, name):
        cell = PaletteCell()

        self.cells.append(cell)
        cell.element   = s
        cell.name      = name
        cell.drawStaff = needsStaff(s)
        cell.xoffset   = 0
        cell.yoffset   = 0
        self.update()
        if s and s.type() == ElementType.ICON:
            icon = s
            self.connect(icon.action(), SIGNAL("toggled(bool)"), self.actionToggled)
        if self.columns():
            self.resizeWidth(self.width())


    def add(self, idx, s, name):
        cell = PaletteCell()

        if idx < len(self.cells):
            del self.cells[idx]
        else:
            i = len(self.cells)
            while i<= idx:
                self.cells.append(0)
                i = i + 1
        self.cells[idx]      = cell
        self.cell.element   = s
        self.cell.name      = name
        self.cell.drawStaff = needsStaff(s)
        self.cell.xoffset   = 0
        self.cell.yoffset   = 0
        self.update()
        if s and s.type() == ElementType.ICON:
            icon = s
            self.connect(icon.action(), SIGNAL("toggled(bool)"), self.actionToggled)
        if self.columns():
            self.resizeWidth(self.width())

    def paintEvent(self, QPaintEvent):
        _spatium = GL.gscore.spatium()
        mag = PALETTE_SPATIUM * self.extraMag / _spatium
        GL.gscore.setSpatium(SPATIUM20  * GL.DPI)
        GL.gscore.setPaintDevice(self)

        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)

        c = self.columns()
        if self._drawGrid:
            p.setPen(Qt.gray)
            for row in range(1, self.rows()):
                p.drawLine(0, row*self.vgrid, c * self.hgrid, row*self.vgrid)
            for column  in range(1, c):
                p.drawLine(self.hgrid*column, 0, self.hgrid*column, self.rows()*self.vgrid)

        dy = 2 * PALETTE_SPATIUM * self.extraMag

        pen = QPen(self.palette().brush(QPalette.Normal, QPalette.Text).color())
        pen.setWidthF(defaultStyle[StyleIdx.ST_staffLineWidth].toSpatium().val() * PALETTE_SPATIUM * self.extraMag)

        for idx in range(0, len(self.cells)):
            r = self.idxRect(idx)
            p.setPen(pen)
            if idx == self.selectedIdx:
                p.fillRect(r, self.palette().brush(QPalette.Normal, QPalette.Highlight).color())
            elif idx == self.currentIdx:
                p.fillRect(r, p.background().color().light(118))
            if self.cells.isEmpty() or self.cells[idx] == 0:
                continue
            el = self.cells[idx].element
            if el == 0:
                continue
            drawStaff = self.cells[idx].drawStaff
            if el.type() != ElementType.ICON:
                row    = idx / c
                column = idx % c

                el.layout()
                el.setPos(0.0, 0.0)

                if drawStaff:
                    y = r.y() + self.vgrid * .5 - dy + self._yOffset
                    x = r.x() + 3
                    w = self.hgrid - 6
                    for i in range(0, 5):
                        yy = y + PALETTE_SPATIUM * i * self.extraMag
                        p.drawLine(QLineF(x, yy, x + w, yy))
                p.save()
                p.scale(mag, mag)

                gw = self.hgrid / mag
                gh = self.vgrid / mag
                gx = column * gw + self.cells[idx].xoffset / mag
                gy = row    * gh + self.cells[idx].yoffset / mag

                sw = el.width()
                sh = el.height()

                if drawStaff:
                    sy = gy + gh * .5 - 2.0 * GL.gscore.spatium()
                else:
                    sy  = gy + (gh - sh) * .5 - el.bbox().y()
                sx  = gx + (gw - sw) * .5 - el.bbox().x()

                sy += self._yOffset / mag

                p.translate(QPointF(sx, sy))
                self.cells[idx].x = sx
                self.cells[idx].y = sy

                if idx == self.selectedIdx:
                    p.setPen(QPen(self.palette().brush(QPalette.Normal, QPalette.HighlightedText.color())))
                else:
                    p.setPen(QPen(self.palette().brush(QPalette.Normal, QPalette.Text.color())))
                el.scanElements(p, paintPaletteElement)
                p.restore()
            else:
                x      = r.x()
                y      = r.y()
                icon = el.icon()
                border = 2
                if self.hgrid < self.vgrid:
                    size   = self.hgrid - 2 * border
                else:
                     size   = self.vgrid - 2 * border
                p.drawPixmap(x + (self.hgrid - size) / 2, y + (self.vgrid - size) / 2, icon.pixmap(size, QIcon.Normal, QIcon.On))

    def event(self, evt):
        ev = QEvent(evt)
        if ev.type() == QEvent.ToolTip:
            he = ev
            x = he.pos().x()
            y = he.pos().y()

            row = y / self.vgrid
            col = x / self.hgrid

            if (row < 0 or row >= self.rows()):
                return False
            if (col < 0 or col >= self.columns()):
                return False
            idx = row * self.columns() + col
            if idx >= len(self.cells):
                return False
            if self.cells[idx] == 0:
                return False
            QToolTip.showText(he.globalPos(), self.cells[idx].name, self)
            return False
        return QWidget().event(ev)

    def dragEnterEvent(self, event):
        data = self.event.mimeData()
        if data.hasUrls():
            ul = event.mimeData().urls()
            u = ul.front()
            print "scheme <%s> path <%s>\n" %(u.scheme().toLatin1().data(), u.path().toLatin1().data())
            if u.scheme() == "file":
                fi = QFileInfo(u.path())
                suffix = QString(fi.suffix().toLower())
                if suffix == "svg" or suffix == "jpg" or suffix == "png" or suffix == "xpm":
                    event.acceptProposedAction()

        elif data.hasFormat(mimeSymbolFormat):
            event.acceptProposedAction()

    def dragMoveEvent(self, ev):
        i = self.idx(ev.pos())
        if i == -1:
            return

        n = len(self.cells)
        ii = i
        while ii<n:
            if self.cells[ii] == 0:
                break
            ii = ii + 1
        if ii == n:
            return
        if self.currentIdx != -1:
            r = self.idxRect(self.currentIdx)
        self.update(r | self.idxRect(ii))
        self.currentIdx = ii

    def dropEvent(self, event):
        data = event.mimeData()
        if data.hasUrls():
            ul = event.mimeData().urls()
            u = ul.front()
            if u.scheme() == "file":
                fi = QFileInfo(u.path())
                s = Image(None)
                suffix = QString(fi.suffix().toLower())
                if suffix == "svg":
                    s = SvgImage(GL.gscore)
                elif suffix == "jpg" or suffix == "png" or suffix == "xpm":
                    s = RasterImage(GL.gscore)
                else:
                    return
                mag = PALETTE_SPATIUM * self.extraMag / GL.gscore.spatium()
                s.setPath(u.toLocalFile())
                s.setSize(QSizeF(self.hgrid / mag, self.hgrid / mag))
                e = s
                name = s.path()
        elif data.hasFormat(mimeSymbolFormat):
            data = QByteArray(event.mimeData().data(mimeSymbolFormat))
            doc = QDomDocument()
            (ok, err, line, column) = doc.setContent(data)
            if not ok:
                print "error reading drag data\n"
                return
            docName = "--"
            el = doc.documentElement()
            (type, dragOffset, duration)  = Element.readType(el)

            if type ==  ElementType.IMAGE:
                path = QString()
                ee = el.firstChildElement()
                while not ee.isNull():
                    tag = QString(ee.tagName())
                    if tag == "path":
                        path = ee.text()
                        break
                    ee = ee.nextSiblingElement()
                image =  0
                s =   QString(path.toLower())
                if s.endsWith(".svg"):
                    image = SvgImage(GL.gscore)
                elif s.endsWith(".jpg") or s.endsWith(".png") or s.endsWith(".xpm"):
                    image = RasterImage(GL.gscore)
                else:
                    print "unknown image format <%s>\n" %path.toLatin1().data()
                if image:
                    image.read(el)
                    e = image
            elif type == ElementType.SYMBOL:
                s = Symbol(GL.gscore)
                s.read(el)
                e = s
            else:
                e = Element.create(type, GL.gscore)
                if e:
                    e.read(el)
                if e.type() == ElementType.TEXTLINE:
                    tl = e
                    tl.setLen(GL.gscore.spatium() * 7)
                    tl.setTrack(0)
        if e:
            e.setSelected(False)
            ok = False
            if event.source() == self:
                i = self.idx(event.pos())
                if i == -1:
                    self.cells.append(self.cells[self.dragSrcIdx])
                    self.cells[self.dragSrcIdx] = 0
                    ok = True
                elif self.dragSrcIdx != i:
                    c = self.cells[self.dragSrcIdx]
                    self.cells[self.dragSrcIdx] = self.cells[i]
                    self.cells[i] = c
                    del e
                    ok = True
                event.setDropAction(Qt.MoveAction)
            else:
                self.append(e, name)
                ok = True
            if ok:
                event.acceptProposedAction()
                self.update()
                self.changed.emit()


class PaletteProperties(QDialog, Ui_PaletteProperties):
    def __init__(self, p,  parent = None):
        super(PaletteProperties, self).__init__(parent)
        self.palette = p
        self.setupUi(self)
        self.name.setText(self.palette.name())
        self.cellWidth.setValue(self.palette.gridWidth())
        self.cellHeight.setValue(self.palette.gridHeight())
        self.showGrid.setChecked(self.palette.drawGrid())
        self.elementOffset.setValue(self.palette.yOffset())
        self.mag.setValue(self.palette.mag())
        
    def accept(self):
        self.palette.setName(self.name.text())
        self.palette.setGrid(self.cellWidth.value(), self.cellHeight.value())
        self.palette.setDrawGrid(self.showGrid.isChecked())
        self.palette.setYOffset(self.elementOffset.value())
        self.palette.setMag(self.mag.value())
        QDialog.accept()

class PaletteCellProperties(QDialog, Ui_PaletteCellProperties):
    def __init__(self, p,  parent = None):
        super(PaletteCellProperties, self).__init__(parent)
        self.palette = p
        self.setupUi(self)
        self.xoffset.setValue(self.cell.xoffset)
        self.yoffset.setValue(self.cell.yoffset)

    def accept(self):
        self.cell.xoffset = self.xoffset.value()
        self.cell.yoffset = self.yoffset.value()
        QDialog.accept()


class PaletteScrollArea(QScrollArea):
    def __init__(self, w, parent = None):
        super(PaletteScrollArea, self).__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setWidget(w)
        self._restrictHeight = True

    def setRestrictHeight(self, val):
        self._restrictHeight = val

    def resizeEvent(self, re):
        palette = self.widget()
        h = palette.resizeWidth(self.width())
        if self._restrictHeight:
            self.setMaximumHeight(h+8)
        QScrollArea().resizeEvent(re)

class PaletteCell:
    def  __init__(self):
        self.element = 0
        self.name = 0
        self.drawStaff = 0
        self.x = 0
        self.y = 0
        self.xoffset = 0
        self.yoffset = 0

    def PaletteCell1(self, c):
        self.element = c.element
        self.name = c.name
        self.drawStaff = c.drawStaff
        self.x = c.x
        self.y = c.y
        self.xoffset = c.xoffset
        self.yoffset = c.yoffset

class PaletteBoxButton(QToolButton):
    paletteCmd = pyqtSignal(int, int)
    def __init__(self, w, p, parent = None):
        super(PaletteBoxButton, self).__init__(parent)
        self.id = 0
        self.palette = p
        self.setCheckable(True)
        self.setFocusPolicy(Qt.NoFocus)
        self.connect(self, SIGNAL("clicked(bool)"), w.setVisible)
        self.setFixedHeight(QFontMetrics(self.font()).height() + 3)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        menu = QMenu()
        self.connect(menu, SIGNAL("aboutToShow()"), self.beforePulldown)

        action = menu.addAction(self.tr("Palette Properties"))
        self.connect(action, SIGNAL("triggered()"), self.propertiesTriggered)

        action = menu.addAction(self.tr("Insert new Palette"))
        self.connect(action, SIGNAL("triggered()"), self.newTriggered)

        action = menu.addAction(self.tr("Move Palette Up"))
        self.connect(action, SIGNAL("triggered()"), self.upTriggered)

        action = menu.addAction(self.tr("Move Palette Down"))
        self.connect(action, SIGNAL("triggered()"), self.downTriggered)

        editAction = menu.addAction(self.tr("Enable Editing"))
        editAction.setCheckable(True)
        self.connect(editAction, SIGNAL("triggered(bool)"), self.enableEditing)

        menu.addSeparator()
        action = menu.addAction(self.tr("Delete Palette"))
        self.connect(action, SIGNAL("triggered()"), self.deleteTriggered)
        self.setMenu(menu)

    def setId(self, v):
        self.id = v

    def beforePulldown(self):
        self.editAction.setChecked(not self.palette.readOnly())

    def enableEditing(self, val):
        self.palette.setReadOnly(not val)

    def changeEvent(self, ev):
        if ev.type() == QEvent.FontChange:
            self.setFixedHeight(QFontMetrics(self.font()).height() + 2)

    def deleteTriggered(self):
        self.paletteCmd(PaletteCommand.PALETTE_DELETE, id)

    def propertiesTriggered(self):
        self.paletteCmd(PaletteCommand.PALETTE_EDIT, id)

    def upTriggered(self):
        self.paletteCmd(PaletteCommand.PALETTE_UP, id)

    def downTriggered(self):
        self.paletteCmd(PaletteCommand.PALETTE_DOWN, id)

    def newTriggered(self):
        self.paletteCmd(PaletteCommand.PALETTE_NEW, id)

class PaletteBox(QDockWidget):
    paletteVisible = pyqtSignal(bool)
    def __init__(self, parent = None):
        super(PaletteBox, self).__init__(parent)
        QDockWidget(self.tr("Palettes"))
        self.setObjectName("palette-box")
        mainWidget = QWidget()
        self.vbox = QVBoxLayout()
        self.vbox.setMargin(0)
        self.vbox.setSpacing(0)
        mainWidget.setLayout(self.vbox)
        self.vbox.addStretch(1)
        mainWidget.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Ignored)
        self.setWidget(mainWidget)
        self._dirty = False

    def  setDirty(self):
        self._dirty = True

    def dirty(self):
        return self._dirty

    def paletteCmd(self, cmd, slot):
        item = self.vbox.itemAt(slot)
        b = item.widget()
        if cmd == PaletteCommand.PALETTE_DELETE:
            self.vbox.removeItem(item)
            b.deleteLater()
            del item
            item = self.vbox.itemAt(slot)
            self.vbox.removeItem(item)
            tb = item.widget()
            del tb
            del item
            for i in range(0, (self.vbox.count() - 1) / 2):
                (self.vbox.itemAt(i * 2).widget()).setId(i*2)
        elif cmd == PaletteCommand.PALETTE_NEW:
            p = Palette()
            p.setReadOnly(False)
            sa = PaletteScrollArea(p)
            b   = PaletteBoxButton(sa, p)
            sa.setVisible(False)
            p.setName("new Palette")
            b.setText(p.name())
            self.vbox.insertWidget(slot, b)
            self.vbox.insertWidget(slot+1, sa, 1000)
            self.connect(b, SIGNAL("paletteCmd(int,int)"), self.paletteCmd)
            self.connect(p, SIGNAL("changed()"), self.setDirty)
            for i in range(0, (self.vbox.count() - 1) / 2):
                (self.vbox.itemAt(i * 2).widget()).setId(i*2)
        elif cmd == PaletteCommand.PALETTE_EDIT:
            sa = self.vbox.itemAt(slot+1).widget()
            palette = sa.widget()
            item = self.vbox.itemAt(slot)
            b = item.widget()

            pp = PaletteProperties(palette, 0)
            rv = pp.exec_()
            if rv == 1:
                self._dirty = True
                b.setText(palette.name())
                palette.update()
        elif cmd == PaletteCommand.PALETTE_UP:
            if slot:
                i1 = self.vbox.itemAt(slot)
                i2 = self.vbox.itemAt(slot+1)
                self.vbox.removeItem(i1)
                self.vbox.removeItem(i2)
                self.vbox.insertWidget(slot-2, i2.widget())
                self.vbox.insertWidget(slot-2, i1.widget())
                del i1
                del i2
                for i in range(0, (self.vbox.count() - 1) / 2):
                    (self.vbox.itemAt(i * 2).widget()).setId(i*2)

        elif cmd == PaletteCommand.PALETTE_DOWN:
            if slot < (self.vbox.count() - 3):
                i1 = self.vbox.itemAt(slot)
                i2 = self.vbox.itemAt(slot+1)
                self.vbox.removeItem(i1)
                self.vbox.removeItem(i2)
                self.vbox.insertWidget(slot+2, i2.widget())
                self.vbox.insertWidget(slot+2, i1.widget())
                del i1
                del i2
                for i in range(0, (self.vbox.count() - 1) / 2):
                    (self.vbox.itemAt(i * 2).widget()).setId(i*2)

        self._dirty = True

      
    def addPalette(self, w):
        sa = PaletteScrollArea(w)
        b   = PaletteBoxButton(sa, w)
        sa.setVisible(False)
        b.setText(w.name())
        slotIdx = self.vbox.count() - 1
        self.vbox.insertWidget(slotIdx, b)
        self.vbox.insertWidget(slotIdx+1, sa, 1000)
        b.setId(slotIdx)
        self.connect(b, SIGNAL("paletteCmd(int,int)"), self.paletteCmd)
        self.connect(w, SIGNAL("changed()"), self.setDirty)

        if w.drumPalette():
            GL.mscore.setDrumPalette(w)
            GL.mscore.updateDrumset()
            self.connect(w, SIGNAL("boxClicked(int)"), GL.mscore.drumPaletteSelected)

    def closeEvent(self, ev):
        self.paletteVisible(False)
        QWidget.closeEvent(ev)
