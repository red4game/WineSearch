import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from WS_MainUI import Ui_WineSearcher
from PySide6.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_WineSearcher()
        self.ui.setupUi(self)


        self.ui.SearchButtonCatalog.clicked.connect(self.ManualSearch)
        self.ui.AddButtonCatalog.clicked.connect(self.AddWine)
        self.ui.RemoveButtonCatalog.clicked.connect(self.RemoveWine)
        self.ui.AutoSearchButton.clicked.connect(self.AutoSearch)
        self.ui.SearchBarCatalog.returnPressed.connect(self.ManualSearch)

    
    @Slot()
    def ManualSearch(self):
        print("This is a manual search with the search : " + self.ui.SearchBarCatalog.text())
        pass

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