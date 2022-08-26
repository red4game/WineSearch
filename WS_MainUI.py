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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_WineSearcher(object):
    def setupUi(self, WineSearcher):
        if not WineSearcher.objectName():
            WineSearcher.setObjectName(u"WineSearcher")
        WineSearcher.resize(1354, 912)
        self.centralwidget = QWidget(WineSearcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WineCatalogue = QTableWidget(self.centralwidget)
        if (self.WineCatalogue.columnCount() < 10):
            self.WineCatalogue.setColumnCount(10)
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
        __qtablewidgetitem8 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.WineCatalogue.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.WineCatalogue.setObjectName(u"WineCatalogue")
        self.WineCatalogue.setGeometry(QRect(10, 30, 1331, 651))
        font = QFont()
        font.setPointSize(16)
        self.WineCatalogue.setFont(font)
        self.WineCatalogue.setSortingEnabled(True)
        self.WineCatalogue.horizontalHeader().setCascadingSectionResizes(False)
        self.WineCatalogue.horizontalHeader().setMinimumSectionSize(64)
        self.WineCatalogue.horizontalHeader().setDefaultSectionSize(192)
        self.WineCatalogue.horizontalHeader().setProperty("showSortIndicator", True)
        self.WineCatalogue.verticalHeader().setCascadingSectionResizes(False)
        self.WineCatalogue.verticalHeader().setProperty("showSortIndicator", False)
        self.WineCatalogue.verticalHeader().setStretchLastSection(False)
        self.WineSearchInput = QLineEdit(self.centralwidget)
        self.WineSearchInput.setObjectName(u"WineSearchInput")
        self.WineSearchInput.setGeometry(QRect(560, 740, 361, 41))
        self.CatalogSearchButton = QPushButton(self.centralwidget)
        self.CatalogSearchButton.setObjectName(u"CatalogSearchButton")
        self.CatalogSearchButton.setGeometry(QRect(1160, 690, 181, 81))
        self.CatalogSearchButton.setFont(font)
        self.AddButtonCatalog = QPushButton(self.centralwidget)
        self.AddButtonCatalog.setObjectName(u"AddButtonCatalog")
        self.AddButtonCatalog.setGeometry(QRect(10, 690, 161, 61))
        self.RemoveButtonCatalog = QPushButton(self.centralwidget)
        self.RemoveButtonCatalog.setObjectName(u"RemoveButtonCatalog")
        self.RemoveButtonCatalog.setGeometry(QRect(180, 690, 161, 61))
        self.AutoSearchButton = QPushButton(self.centralwidget)
        self.AutoSearchButton.setObjectName(u"AutoSearchButton")
        self.AutoSearchButton.setGeometry(QRect(1160, 780, 181, 81))
        self.AutoSearchButton.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 740, 121, 41))
        self.label.setFont(font)
        self.WinerySearchInput = QLineEdit(self.centralwidget)
        self.WinerySearchInput.setObjectName(u"WinerySearchInput")
        self.WinerySearchInput.setGeometry(QRect(610, 690, 311, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 690, 211, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(930, 690, 81, 41))
        self.label_3.setFont(font)
        self.YearSearchInput = QSpinBox(self.centralwidget)
        self.YearSearchInput.setObjectName(u"YearSearchInput")
        self.YearSearchInput.setGeometry(QRect(1010, 690, 141, 41))
        self.YearSearchInput.setFont(font)
        self.YearSearchInput.setMinimum(1900)
        self.YearSearchInput.setMaximum(2050)
        self.YearSearchInput.setValue(2015)
        self.SearchYearCheckBox = QCheckBox(self.centralwidget)
        self.SearchYearCheckBox.setObjectName(u"SearchYearCheckBox")
        self.SearchYearCheckBox.setGeometry(QRect(930, 750, 231, 26))
        self.SearchYearCheckBox.setFont(font)
        self.SearchYearCheckBox.setIconSize(QSize(16, 16))
        self.SearchYearCheckBox.setChecked(False)
        self.SearchYearCheckBox.setAutoRepeat(False)
        self.SearchCountryCheckBox = QCheckBox(self.centralwidget)
        self.SearchCountryCheckBox.setObjectName(u"SearchCountryCheckBox")
        self.SearchCountryCheckBox.setGeometry(QRect(930, 830, 231, 26))
        self.SearchCountryCheckBox.setFont(font)
        self.SearchCountryCheckBox.setIconSize(QSize(16, 16))
        self.SearchCountryCheckBox.setChecked(False)
        self.SearchCountryCheckBox.setAutoRepeat(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(930, 780, 81, 41))
        self.label_4.setFont(font)
        self.CountrySearchCombo = QComboBox(self.centralwidget)
        self.CountrySearchCombo.setObjectName(u"CountrySearchCombo")
        self.CountrySearchCombo.setGeometry(QRect(990, 780, 161, 41))
        self.CountrySearchCombo.setFont(font)
        WineSearcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WineSearcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1354, 27))
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
        ___qtablewidgetitem.setText(QCoreApplication.translate("WineSearcher", u"Vignoble", None));
        ___qtablewidgetitem1 = self.WineCatalogue.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WineSearcher", u"Nom", None));
        ___qtablewidgetitem2 = self.WineCatalogue.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WineSearcher", u"Ann\u00e9e", None));
        ___qtablewidgetitem3 = self.WineCatalogue.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WineSearcher", u"Pays", None));
        ___qtablewidgetitem4 = self.WineCatalogue.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WineSearcher", u"Score", None));
        ___qtablewidgetitem5 = self.WineCatalogue.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WineSearcher", u"Volume", None));
        ___qtablewidgetitem6 = self.WineCatalogue.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WineSearcher", u"Photo", None));
        ___qtablewidgetitem7 = self.WineCatalogue.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WineSearcher", u"ID", None));
        ___qtablewidgetitem8 = self.WineCatalogue.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WineSearcher", u"Prix", None));
        ___qtablewidgetitem9 = self.WineCatalogue.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WineSearcher", u"URL", None));
        self.CatalogSearchButton.setText(QCoreApplication.translate("WineSearcher", u"Search", None))
        self.AddButtonCatalog.setText(QCoreApplication.translate("WineSearcher", u"Add to catalogue", None))
        self.RemoveButtonCatalog.setText(QCoreApplication.translate("WineSearcher", u"Remove from catalogue", None))
        self.AutoSearchButton.setText(QCoreApplication.translate("WineSearcher", u"Automatic Seach", None))
        self.label.setText(QCoreApplication.translate("WineSearcher", u"Nom du vin :", None))
        self.WinerySearchInput.setText("")
        self.label_2.setText(QCoreApplication.translate("WineSearcher", u"Nom du vignoble :", None))
        self.label_3.setText(QCoreApplication.translate("WineSearcher", u"Ann\u00e9e : ", None))
        self.SearchYearCheckBox.setText(QCoreApplication.translate("WineSearcher", u"Recherche par ann\u00e9e", None))
        self.SearchCountryCheckBox.setText(QCoreApplication.translate("WineSearcher", u"Recherche par pays", None))
        self.label_4.setText(QCoreApplication.translate("WineSearcher", u"Pays :", None))
    # retranslateUi

