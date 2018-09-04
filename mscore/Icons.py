#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Sym import *



def symIcon(sc, size, width, height):
    scc = Sym(0, 0, 0)
    scc = sc
    mag  = .6 * (size/20.0) * GL.PDPI / GL.DPI
    bb   =  QRectF(sc.bbox(mag))

    w   = bb.width()
    h   = bb.height()
    x   = (width  - w) * .5 - bb.x()
    y   = (height - h) * .5 - bb.y()

    wi = QWidget()
    image = QPixmap(width, height)
    bg = QColor(wi.palette().brush(QPalette.Normal, QPalette.Window).color())
    
    image.fill(QColor(255, 255, 255, 0))
    painter = QPainter(image)
    painter.setRenderHint(QPainter.TextAntialiasing, True)
    painter.setFont(sc.font())

    pen = QPen(wi.palette().brush(QPalette.Normal, QPalette.Text).color())
    painter.setPen(pen)
    scc.draw(painter, mag, x, y)
    painter.end()
    return QIcon(image)

def genIcons():
    iw = Preferences().noteEntryIconWidth
    ih = Preferences().noteEntryIconHeight
    
    GL.icons[IconNames2.longaUp_ICON]        = QIcon("data/longaUp.svg")
    GL.icons[IconNames2.brevis_ICON]         = QIcon("data/brevis.svg")
    GL.icons[IconNames2.note_ICON]           = QIcon("data/note.svg")
    GL.icons[IconNames2.note2_ICON]          = QIcon("data/note2.svg")
    GL.icons[IconNames2.note4_ICON]          = QIcon("data/note4.svg")
    GL.icons[IconNames2.note8_ICON]          = QIcon("data/note8.svg")
    GL.icons[IconNames2.note16_ICON]         = QIcon("data/note16.svg")
    GL.icons[IconNames2.note32_ICON]         = QIcon("data/note32.svg")
    GL.icons[IconNames2.note64_ICON]         = QIcon("data/note64.svg")
    GL.icons[IconNames2.natural_ICON]        = QIcon("data/natural.svg")
    GL.icons[IconNames2.sharp_ICON]          = QIcon("data/sharp.svg")
    GL.icons[IconNames2.sharpsharp_ICON]     = QIcon("data/sharpsharp.svg")
    GL.icons[IconNames2.flat_ICON]           = QIcon("data/flat.svg")
    GL.icons[IconNames2.flatflat_ICON]       = QIcon("data/flatflat.svg")
    GL.icons[IconNames2.quartrest_ICON]      = QIcon("data/quartrest.svg")
    GL.icons[IconNames2.dot_ICON]            = QIcon("data/dot.svg")
    GL.icons[IconNames2.dotdot_ICON]         = QIcon("data/dotdot.svg")
    
    GL.icons[IconNames2.sforzatoaccent_ICON] = symIcon(GL.symbols[SymName.sforzatoaccentSym], 20, iw, ih)
    GL.icons[IconNames2.staccato_ICON]       = symIcon(GL.symbols[SymName.staccatoSym], 20, iw, ih)
    GL.icons[IconNames2.tenuto_ICON]         = symIcon(GL.symbols[SymName.tenutoSym], 20, iw, ih)
    GL.icons[IconNames2.plus_ICON]           = symIcon(GL.symbols[SymName.plusSym], 30, iw, ih)
    GL.icons[IconNames2.clef_ICON]           = symIcon(GL.symbols[SymName.trebleclefSym], 17, iw, ih)
    GL.icons[IconNames2.staccato_ICON]       = symIcon(GL.symbols[SymName.dotSym], 30, iw, ih) 

    GL.icons[IconNames2.acciaccatura_ICON]   = QIcon("data/acciaccatura.svg")
    GL.icons[IconNames2.appoggiatura_ICON]   = QIcon("data/appoggiatura.svg")

    vtext = [ "1","2","3","4" ]
    for i in range(0, VOICES):
        GL.icons[IconNames2.voice1_ICON + i] = QIcon()
        image = QPixmap(iw, ih)
        c = Preferences().selectColor[i]
        image.fill(c)
        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black))
        painter.drawText(QRect(0, 0, iw, ih), Qt.AlignCenter, vtext[i])
        painter.end()
        GL.icons[IconNames2.voice1_ICON +i].addPixmap(image)

        painter.begin(image)
        c = QColor(Preferences().selectColor[i].light(140))
        painter.fillRect(0, 0, iw, ih, c)
        painter.setPen(QPen(Qt.black))
        painter.drawText(QRect(0, 0, iw, ih), Qt.AlignCenter, vtext[i])
        painter.end()
        GL.icons[IconNames2.voice1_ICON + i].addPixmap(image, QIcon.Normal, QIcon.On)

    GL.icons[IconNames2.flip_ICON]    =  QIcon("data/flip.svg")
    GL.icons[IconNames2.cut_ICON]     =  QIcon("data/cut.png")
    GL.icons[IconNames2.copy_ICON]    =  QIcon("data/copy.png")
    GL.icons[IconNames2.paste_ICON]   =  QIcon("data/paste.png")
    GL.icons[IconNames2.print_ICON]   =  QIcon("data/print.png")

    GL.icons[IconNames2.undo_ICON]       =  QIcon("data/undo.svg")
    GL.icons[IconNames2.redo_ICON]       =  QIcon("data/redo.svg")
    GL.icons[IconNames2.midiin_ICON]     =  QIcon("data/midiin.svg")
    GL.icons[IconNames2.speaker_ICON]    =  QIcon("data/speaker.svg")
    GL.icons[IconNames2.start_ICON]      =  QIcon("data/start.svg")
    GL.icons[IconNames2.play_ICON]       =  QIcon("data/play.svg")
    GL.icons[IconNames2.sbeam_ICON]      =  QIcon("data/sbeam.svg")
    GL.icons[IconNames2.mbeam_ICON]      =  QIcon("data/mbeam.svg")
    GL.icons[IconNames2.nbeam_ICON]      =  QIcon("data/nbeam.svg")
    GL.icons[IconNames2.beam32_ICON]     =  QIcon("data/beam32.svg")
    GL.icons[IconNames2.abeam_ICON]      =  QIcon("data/abeam.svg")
    GL.icons[IconNames2.fileOpen_ICON]   =  QIcon("data/fileopen.svg")
    GL.icons[IconNames2.fileNew_ICON]    =  QIcon("data/filenew.svg")
    GL.icons[IconNames2.fileSave_ICON]   =  QIcon("data/filesave.svg")
    GL.icons[IconNames2.fileSaveAs_ICON] =  QIcon("data/filesaveas.svg")
    GL.icons[IconNames2.exit_ICON]       =  QIcon("data/exit.svg")
    GL.icons[IconNames2.viewmag_ICON]    =  QIcon("data/viewmag.svg")
    GL.icons[IconNames2.repeat_ICON]     =  QIcon("data/repeat.svg")
    GL.icons[IconNames2.noteEntry_ICON]  =  QIcon("data/noteentry.svg")
    GL.icons[IconNames2.grace4_ICON]     =  QIcon("data/grace4.svg")
    GL.icons[IconNames2.grace16_ICON]    =  QIcon("data/grace16.svg")
    GL.icons[IconNames2.grace32_ICON]    =  QIcon("data/grace32.svg")
    GL.icons[IconNames2.keys_ICON]       =  QIcon("data/keyboard.svg")
    GL.icons[IconNames2.tie_ICON]        =  QIcon("data/tie.svg")
    GL.icons[IconNames2.window_ICON]     =  QIcon("data/mscore.png")
    GL.icons[IconNames2.community_ICON]     =  QIcon("data/community.svg")

