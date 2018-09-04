#!/usr/bin/env python
#-*- coding:utf-8 -*-

from Icons import *
from muse import *



def main():
    revision = 3.0
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("Muse");
    QCoreApplication.setOrganizationDomain("muse.org")
    QCoreApplication.setApplicationName("Muse 3.0")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    #if app.isRunning():
    #    return 0
    if GL.dataPath.isEmpty():
          GL.dataPath = QDesktopServices.storageLocation(QDesktopServices.DataLocation)
    dir = QDir()
    dir.mkpath(GL.dataPath + "/plugins")
    setDefaultStyle()

    localeName = QSettings().value("language", "system").toString()
    setMscoreLocale(localeName)
    initShortcuts()
    sc = QSplashScreen()
    if  Preferences().showSplashScreen:
        pm = QPixmap("data\splash.jpg")
        sc = QSplashScreen(pm)
        sc.setWindowTitle(QString("Muse Startup"))
        sc.setWindowFlags(Qt.FramelessWindowHint)
        sc.show()
        qApp.processEvents()


    qApp.setStyleSheet("background-color.blue;")
    qApp.setStyleSheet(appStyleSheet())
    if Preferences().style.isEmpty() == False:
        QApplication.setStyle(Preferences().style)

    if QFontDatabase.addApplicationFont("fonts\mscore-20.ttf") == -1:
        print "Muse: fatal error: cannot load internal font\n"
        exit(1)
    if QFontDatabase.addApplicationFont("fonts\mscore1-20.ttf") == -1:
        print "Muse: fatal error: cannot load internal font\n"
        exit(1)
    if QFontDatabase.addApplicationFont("fonts\MuseJazz.ttf") == -1:
        print "Muse: fatal error: cannot load internal font\n"
        exit(1)

    GL.PDPI =  QWidget().logicalDpiX()
    GL.DPI = GL.PDPI
    GL.DPMM = GL.DPI / INCH

    initSymbols()
    genIcons()
    qApp.setWindowIcon(GL.icons[IconNames2.window_ICON])
    #initDrumset()
    GL.gscore = Score(defaultStyle)
    GL.mscore = MuseScore()
    #GL.mscore.readLanguages(GL.mscoreGlobalShare + "locale\languages.xml")
    GL.mscore.show()
    if sc:
        sc.finish(GL.mscore)
    return qApp.exec_()
    #sys.exit(app.exec_())

if __name__ == '__main__':
    main()

