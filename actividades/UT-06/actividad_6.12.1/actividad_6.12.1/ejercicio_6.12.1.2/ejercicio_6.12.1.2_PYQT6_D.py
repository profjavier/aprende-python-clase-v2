'''
Ejercicio 2 (ejercicio_2.py).
Escribir un programa que cuente cuantas líneas tiene un fichero de texto.
'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys


class ContadorLineas(QWidget):

    def __init__(self):
        super().__init__()
        self.config_ui()
        self.show()

    def config_ui(self):
        self.setWindowTitle("Contador de lineas")
        self.setFixedSize(400,300)  # Fija el tamaño a 400x300
        self.move(100, 100)
        self.crea_widgets()

    def crea_widgets(self):
        label = QLabel("Fichero:", self)
        label.move(20, 20)

        self.edit_filename = QLineEdit(self)
        self.edit_filename.move(100, 20)
        self.edit_filename.resize(100, 25)

        btn_cargar = QPushButton("Analizar", self)
        btn_cargar.move(200, 20)
        btn_cargar.clicked.connect(self.analiza_fichero)

        label = QLabel("Nº de lineas del fichero: ", self)
        label.setStyleSheet("font-weight: bold")
        label.move(20, 60)

        self.label_lineas = QLabel("", self)
        self.label_lineas.move(20, 80)
        self.label_lineas.resize(350, 25)
        self.label_lineas.setStyleSheet("background-color: rgb(255, 255, 0);")

    def calcula_lineas(self):
        filename = self.edit_filename.text()
        with open(filename, "r", encoding="utf-8") as fichero:
            num_lineas = 0
            for _ in fichero:
                num_lineas += 1
        return num_lineas

    def analiza_fichero(self):
        num_lineas = self.calcula_lineas()
        self.label_lineas.setText(f"El fichero tiene {num_lineas} lineas")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ContadorLineas()
    sys.exit(app.exec())

