# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WS_MainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_WineSearcher(object):
    def setupUi(self, WineSearcher):
        if not WineSearcher.objectName():
            WineSearcher.setObjectName(u"WineSearcher")
        WineSearcher.resize(827, 862)
        self.centralwidget = QWidget(WineSearcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WineCatalogue = QTableWidget(self.centralwidget)
        if (self.WineCatalogue.columnCount() < 8):
            self.WineCatalogue.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.WineCatalogue.setObjectName(u"WineCatalogue")
        self.WineCatalogue.setGeometry(QRect(10, 30, 811, 651))
        self.SearchBarCatalog = QLineEdit(self.centralwidget)
        self.SearchBarCatalog.setObjectName(u"SearchBarCatalog")
        self.SearchBarCatalog.setGeometry(QRect(10, 690, 511, 41))
        self.SearchButtonCatalog = QPushButton(self.centralwidget)
        self.SearchButtonCatalog.setObjectName(u"SearchButtonCatalog")
        self.SearchButtonCatalog.setGeometry(QRect(530, 690, 291, 41))
        self.AddButtonCatalog = QPushButton(self.centralwidget)
        self.AddButtonCatalog.setObjectName(u"AddButtonCatalog")
        self.AddButtonCatalog.setGeometry(QRect(10, 740, 161, 61))
        self.RemoveButtonCatalog = QPushButton(self.centralwidget)
        self.RemoveButtonCatalog.setObjectName(u"RemoveButtonCatalog")
        self.RemoveButtonCatalog.setGeometry(QRect(180, 740, 161, 61))
        self.AutoSearchButton = QPushButton(self.centralwidget)
        self.AutoSearchButton.setObjectName(u"AutoSearchButton")
        self.AutoSearchButton.setGeometry(QRect(350, 740, 161, 61))
        WineSearcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WineSearcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 827, 27))
        WineSearcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WineSearcher)
        self.statusbar.setObjectName(u"statusbar")
        WineSearcher.setStatusBar(self.statusbar)

        self.retranslateUi(WineSearcher)

        QMetaObject.connectSlotsByName(WineSearcher)
    # setupUi

    def retranslateUi(self, WineSearcher):
        WineSearcher.setWindowTitle(QCoreApplication.translate("WineSearcher", u"WineSearcher", None))
        ___qtablewidgetitem = self.WineCatalogue.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WineSearcher", u"Nom", None));
        ___qtablewidgetitem1 = self.WineCatalogue.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WineSearcher", u"Ann\u00e9e", None));
        ___qtablewidgetitem2 = self.WineCatalogue.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WineSearcher", u"Photo", None));
        ___qtablewidgetitem3 = self.WineCatalogue.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WineSearcher", u"Pays", None));
        ___qtablewidgetitem4 = self.WineCatalogue.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WineSearcher", u"R\u00e9gion", None));
        ___qtablewidgetitem5 = self.WineCatalogue.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WineSearcher", u"Score", None));
        ___qtablewidgetitem6 = self.WineCatalogue.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WineSearcher", u"Prix", None));
        ___qtablewidgetitem7 = self.WineCatalogue.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WineSearcher", u"Description", None));
        self.SearchButtonCatalog.setText(QCoreApplication.translate("WineSearcher", u"Search", None))
        self.AddButtonCatalog.setText(QCoreApplication.translate("WineSearcher", u"Add to catalogue", None))
        self.RemoveButtonCatalog.setText(QCoreApplication.translate("WineSearcher", u"Remove from catalogue", None))
        self.AutoSearchButton.setText(QCoreApplication.translate("WineSearcher", u"Automatic Seach", None))
    # retranslateUi

