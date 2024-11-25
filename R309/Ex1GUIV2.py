import sys
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        
        lab = QLabel("Saisir votre nom")
        self.text = QLineEdit("")  # Toujours important de faire de text un attribut de classe
        
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")

        self.lab_mess = QLabel("")
        grid.addWidget(self.lab_mess, 2, 0)
        
        # Ajouter les composants au grid layout
        grid.addWidget(lab, 0, 0)
        grid.addWidget(self.text, 0, 3)
        grid.addWidget(ok, 3, 0)
        grid.addWidget(quit, 3, 3)
        
        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        
        self.setWindowTitle("Une première fenêtre")
        self.resize(250,100)

    def __actionOk(self):
        nom = self.text.text()
        self.lab_mess.setText(f"Bonjour {nom} !")

    def __actionQuitter(self):
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()