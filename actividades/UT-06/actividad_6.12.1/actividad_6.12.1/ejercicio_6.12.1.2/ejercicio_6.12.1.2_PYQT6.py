'''
Ejercicio 2 (ejercicio_2.py).
Escribir un programa que cuente cuantas líneas tiene un fichero de texto.
'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys


def calcula_lineas():
    with open("fichero.txt", "r", encoding="utf-8") as fichero:
        num_lineas = 0
        for _ in fichero:
            num_lineas += 1
    return num_lineas

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Hola PyQt6")
ventana.resize(400, 300)

label = QLabel("Nº de lineas del fichero: ", ventana)
label.setStyleSheet("font-weight: bold")
label.move(20, 20)
label_lineas = QLabel("", ventana)
label_lineas.move(160, 20)
num_lineas = calcula_lineas()
label_lineas.setText(f"El fichero tiene {num_lineas} lineas")
label_lineas.setStyleSheet("background-color: rgb(255, 255, 0);")
ventana.show()
label_lineas.move(160, 20)
ventana.show()

sys.exit(app.exec())