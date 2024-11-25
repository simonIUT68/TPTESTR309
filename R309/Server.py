import sys
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,  QLabel, QLineEdit, QPushButton,  QVBoxLayout, QTextEdit
import socket, threading

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.server_socket = socket.socket()

        
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QVBoxLayout()
        widget.setLayout(grid)
        grid.addWidget(QLabel("Adresse IP :"))
        self.ip = QLineEdit("127.0.0.1")
        grid.addWidget(self.ip)
        grid.addWidget(QLabel("Port :"))
        self.port = QLineEdit("4200")
        grid.addWidget(self.port)
        grid.addWidget(QLabel("Nbr clients max :"))
        self.nbrclient = QLineEdit("5")
        grid.addWidget(self.nbrclient)
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        grid.addWidget(self.text)


        self.demarer = QPushButton('demarer')
        self.demarer.clicked.connect(self.serverOn)
        grid.addWidget(self.demarer)

        arret = QPushButton('arret')
        
        
        self.setWindowTitle("Chatbox serveur")
        self.resize(250,100)

    def serverOn(self):
        try:
            ip = self.ip.text()
            port = int(self.port.text())
            self.server_socket = socket.socket()
            self.server_socket.bind((ip, port))
            self.server_socket.listen(1)
            self.demarer.setText('arret')
            self.demarer.clicked.connect(self.quit)
           
        except ConnectionRefusedError as erorr:
         self.text.append(f"Connexion refusée : {erorr}")
        
        except TimeoutError as erorr:
         self.text.append(f'delai dépassé : {erorr}')
    def quit(self):
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

