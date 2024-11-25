import socket, time
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox, QTextEdit
from PyQt6.QtCore import QCoreApplication
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket()
        reply = "hello"
        widget = QWidget()
        self.setCentralWidget(widget)
        grid1 = QGridLayout()
        widget.setLayout(grid1)
        
        lab1 = QLabel("Serveur :")
        lab2 = QLabel("Port :")
        lab3 = QLabel("Nombre de Clients :")
        self.text1 = QLineEdit("127.0.0.1")
        self.text2 = QLineEdit("4200")
        self.text3 = QLineEdit("1")
        
        self.ok = QPushButton("Démarrage du Serveur")
        quit = QPushButton("Quitter")

        self.txt_mess = QTextEdit()
        self.txt_mess.setReadOnly(True)
        grid1.addWidget(self.txt_mess, 2, 3)
        
        # Ajouter les composants au grid layout
        grid1.addWidget(lab1, 0, 0)
        grid1.addWidget(self.text1, 0, 3)
        grid1.addWidget(lab2, 1, 0)
        grid1.addWidget(self.text2, 1, 1)
        grid1.addWidget(lab3, 1, 2)
        grid1.addWidget(self.text3, 1, 3)
        grid1.addWidget(self.ok, 3, 0)
        grid1.addWidget(quit, 3, 3)
        
        self.ok.clicked.connect(self.actionOk)
        quit.clicked.connect(self.actionQuitter)
        
        self.setWindowTitle("Serveur de Tchat")
        self.resize(400,250)

    def actionOk(self):
        self.ok.setText('Arrêt du Serveur')
        try:
            hostname = self.text1.text()
            port = int(self.text2.text())
            self.server_socket = socket.socket()
            self.server_socket.bind((hostname, port))
            self.server_socket.listen(1)
            self.ok.clicked.connect(self.actionArret)
           
        except ConnectionRefusedError as erorr:
            self.text.append(f"Connexion refusée : {erorr}")
        
        except TimeoutError as erorr:
            self.text.append(f'delai dépassé : {erorr}')
    def actionArret(self):
        self.ok.setText('Démmarage du Serveur')
        try:
            self.conn.send("Serveur arrêté.".encode())
            self.conn.close()
            self.server.close()
           
        except ConnectionRefusedError as erorr:
            self.text.append(f"Connexion refusée : {erorr}")
        
        except TimeoutError as erorr:
            self.text.append(f'delai dépassé : {erorr}')

    def actionQuitter(self):
        QCoreApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()