import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow,QComboBox
from PySide6.QtCore import QFile,Qt,QSortFilterProxyModel
from PySide6.QtGui import QStandardItem,QPixmap,QIcon
import requests
from PySide6.QtWidgets import QTableWidgetItem
import PySide6.QtWidgets as QtWidgets
from WS_MainUI import Ui_WineSearcher
from PySide6.QtCore import Slot
import csv 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_WineSearcher()
        self.ui.setupUi(self)

        WineDataFrame = pd.read_csv("wine_data.csv",sep="|")
        WineDataFrame = WineDataFrame[['winery_name','wine_name','year','country','rating', 'volume_ml','bottle_photo','wine_id','price','url']]


        self.ui.CatalogSearchButton.clicked.connect(self.allFilter)
        self.ui.AddButtonCatalog.clicked.connect(self.AddWine)
        self.ui.RemoveButtonCatalog.clicked.connect(self.RemoveWine)
        self.ui.AutoSearchButton.clicked.connect(self.AutoSearch)
        self.ui.WineSearchInput.returnPressed.connect(self.allFilter)
        self.ui.WinerySearchInput.returnPressed.connect(self.allFilter)
        self.ui.SearchYearCheckBox.stateChanged.connect(self.allFilter)
        self.ui.SearchCountryCheckBox.stateChanged.connect(self.allFilter)


        for row in WineDataFrame.itertuples():
            rowPos = self.ui.WineCatalogue.rowCount()
            self.ui.WineCatalogue.insertRow(rowPos)  
            rowList = list(row)
            for index in range(1,len(rowList)):
                self.ui.WineCatalogue.setItem(rowPos , index-1,QTableWidgetItem(str(rowList[index])))
        
        self.ui.CountrySearchCombo.setDuplicatesEnabled(False)
        self.ui.CountrySearchCombo.setInsertPolicy(QComboBox.InsertAlphabetically)
        items =  set()
        for element in WineDataFrame["country"].unique():
            if element != "" and "Found" not in element:
                items.add(element.split(" - ")[-1])
        items = sorted(list(items))
        self.ui.CountrySearchCombo.addItems(items)
            
            
    
    def allFilter(self):
        for i in range(self.ui.WineCatalogue.rowCount()):
            self.ui.WineCatalogue.setRowHidden(i,False)
        if self.ui.WinerySearchInput.text() != "":
            self.filterWinery(self.ui.WinerySearchInput.text())
        if self.ui.WineSearchInput.text() != "":
            self.filterWine(self.ui.WineSearchInput.text())
        if self.ui.SearchCountryCheckBox.isChecked():
            self.filterCountry(self.ui.CountrySearchCombo.currentText())
        if self.ui.SearchYearCheckBox.isChecked():
            self.filterYear(self.ui.YearSearchInput.text())

    def filterWinery(self, filter_text):
        for i in range(self.ui.WineCatalogue.rowCount()):
            item = self.ui.WineCatalogue.item(i, 0)
            match = filter_text.lower() not in item.text().lower()
            if match:
                self.ui.WineCatalogue.setRowHidden(i, match)  
    
    def filterWine(self, filter_text):
        for i in range(self.ui.WineCatalogue.rowCount()):
            item = self.ui.WineCatalogue.item(i, 1)
            match = filter_text.lower() not in item.text().lower()
            if match:
                self.ui.WineCatalogue.setRowHidden(i, match)      
        
    def filterYear(self, filter_text):
        for i in range(self.ui.WineCatalogue.rowCount()):
            item = self.ui.WineCatalogue.item(i, 2)
            match = filter_text.lower() not in item.text().lower()
            if match:
                self.ui.WineCatalogue.setRowHidden(i, match)
     
                
    def filterCountry(self, filter_text):
        for i in range(self.ui.WineCatalogue.rowCount()):
            item = self.ui.WineCatalogue.item(i, 3)
            match = filter_text.lower() not in item.text().lower()
            if match:
                self.ui.WineCatalogue.setRowHidden(i, match)    



    @Slot()
    def AutoSearch(self):
        print("Auto search with camera and/or webcam")
        pass

    @Slot()
    def AddWine(self):
        print("Add Wine to the catalogue")
        pass

    @Slot()
    def RemoveWine(self):
        print("Remove Wine from the catalogue")
        pass
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())