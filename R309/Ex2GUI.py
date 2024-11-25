import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversion de Température")
        self.resize(400,250)

        # Layout
        grid = QGridLayout()
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        # Widgets
        self.T_entre = QLineEdit()
        self.C_entre = QLineEdit(readOnly=True)
        
        self.T_unit = QComboBox()
        self.T_unit.addItems(["°C", "K"])
        
        self.conv_unit = QLabel("K")
        convertir_button = QPushButton("Convertir")
        aide_button = QPushButton("?")
        self.conversion_direction = QComboBox()
        self.conversion_direction.addItems(["°C -> K", "K -> °C"])

        # Ajouter les widgets au layout
        grid.addWidget(QLabel("Température:"), 0, 0)
        grid.addWidget(self.T_entre, 0, 1)
        grid.addWidget(self.T_unit, 0, 2)
        grid.addWidget(QLabel("Conversion:"), 2, 0)
        grid.addWidget(self.C_entre, 2, 1)
        grid.addWidget(self.conv_unit, 2, 2)
        grid.addWidget(convertir_button, 1, 1)
        grid.addWidget(self.conversion_direction, 1, 2)
        grid.addWidget(aide_button, 3, 1)

        # Connecter les signaux aux slots
        convertir_button.clicked.connect(self.convertir_temperature)
        aide_button.clicked.connect(self.afficher_aide)
        self.conversion_direction.currentIndexChanged.connect(self.changer_unites)

    def convertir_temperature(self):
        try:
            temp = float(self.T_entre.text())
            if self.conversion_direction.currentText() == "°C -> K":
                resultat = temp + 273.15 if temp >= -273.15 else None
                unite = "K"
            else:
                resultat = temp - 273.15 if temp >= 0 else None
                unite = "°C"

            if resultat is not None:
                self.C_entre.setText(f"{resultat:.2f}")
                self.conv_unit.setText(unite)
            else:
                raise ValueError("Température inférieure au zéro absolu.")

        except ValueError as e:
            QMessageBox.warning(self, "Erreur", str(e))
        except Exception:
            QMessageBox.warning(self, "Erreur", "Entrée invalide.")

    def afficher_aide(self):
        QMessageBox.information(self, "Aide", "Permet de convertir une température entre Celsius et Kelvin.")

    def changer_unites(self):
        if self.conversion_direction.currentText() == "°C -> K":
            self.conv_unit.setText("K")
        else:
            self.conv_unit.setText("°C")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
