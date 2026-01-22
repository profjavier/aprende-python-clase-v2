"""
Escribir un programa que pida dos números y muestra su suma.
En caso de no introducir números correctos se mostrará un mensaje en un QMessageBox.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox
)


class Suma(QWidget):

    def __init__(self):
        super().__init__()
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Suma")
        self.resize(400, 300)

        label = QLabel("Numero 1", self)
        label.move(20, 20)
        self.numero1 = QLineEdit(self)
        self.numero1.move(100, 20)
        self.numero1.resize(150, 25)

        label = QLabel("Numero 2", self)
        label.move(20, 60)
        self.numero2 = QLineEdit(self)
        self.numero2.move(100, 60)
        self.numero2.resize(150, 25)

        label = QLabel("Suma", self)
        label.move(20, 100)
        self.lbl_suma = QLabel("", self)
        self.lbl_suma.setGeometry(100, 100, 50,25)
        self.lbl_suma.setStyleSheet("QLabel { color:#ff0000; background-color: #ffff00;}")


        btn_suma = QPushButton("Sumar", self)
        btn_suma.setGeometry(300, 60, 50,25)
        btn_suma.resize(70,25)
        btn_suma.clicked.connect(self.sumar)

    def sumar(self):
        try:
            numero1 = float(self.numero1.text())
            numero2 = float(self.numero2.text())
            suma = numero1 + numero2
            self.lbl_suma.setText(str(suma))
        except Exception:
            QMessageBox.warning(self, "Error", "Numeros incorrectos")



# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Suma()
    ventana.show()
    sys.exit(app.exec())
