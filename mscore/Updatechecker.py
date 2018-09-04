#!/usr/bin/env python                                                                            
#-*- coding:utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *


class UpdateChecker(QObject):

    def __init__(self):
        super(UpdateChecker, self).__init__()
        self.manager = QNetworkAccessManager(self)
        self.connect(self.manager, SIGNAL("finished(QNetworkReply)"), self.onRequestFinished)
        self.os = QString()
        self.release = QString()
        self.revision = QString()

    def onRequestFinished(self, reply):
        if reply.error() != QNetworkReply.NoError :
            print "Error while checking update [%s]\n" %reply.errorString().toAscii().constData()
            return
        
        s = QSettings()
        s.beginGroup("Update")
        s.setValue("lastUpdateDate", QDateTime.currentDateTime())
        s.endGroup()

        data = QByteArray(reply.readAll())
        reader = QXmlStreamReader(data)
        version = QString()
        upgradeRevision = QString()
        downloadUrl = QString()
        infoUrl = QString()
        description = QString()
        releaseType = QString()

        while not reader.atEnd() and not reader.hasError():
            token = reader.readNext()
            if token == QXmlStreamReader.StartDocument:
                continue
            if token == QXmlStreamReader.StartElement:
                if reader.name() == "version":
                    version = self.parseText(reader)
                elif reader.name() == "revision":
                    upgradeRevision = self.parseText(reader)
                elif reader.name() == "downloadUrl":
                    downloadUrl = self.parseText(reader)
                elif reader.name() == "infoUrl":
                    infoUrl = self.parseText(reader)
                elif reader.name() == "description":
                    description = self.parseText(reader)

        message = QString(self.tr("An update for MuseScore is available: <a href=\"%1\">MuseScore %2 r.%3</a>")).arg(downloadUrl).arg(version).arg(upgradeRevision)
        print "revision %s\n" %self.revision.toAscii().constData()
        if not version.isEmpty() and  upgradeRevision > self.revision:
            msgBox = QMessageBox()
            msgBox.setWindowTitle(self.tr("Update Available"))
            msgBox.setText(message)
            msgBox.setTextFormat(Qt.RichText)
            msgBox.exec_()

    def parseText(self, reader1):
        result = QString()
        reader = QXmlStreamReader()
        reader = reader1
        reader.readNext()
        if reader.tokenType() == QXmlStreamReader.Characters:
              result = reader.text().toString()
        return result
