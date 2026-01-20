'''
Ejercicio 2 (ejercicio_2.py).
Escribir un programa que cuente cuantas líneas tiene un fichero de texto.
'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys


def calcula_lineas():
    with open("fichero.txt", "r", encoding="utf-8") as fichero:
        num_lineas = 0
        for _ in fichero:
            num_lineas += 1
    return num_lineas

def analiza_fichero():
    num_lineas = calcula_lineas()
    label_lineas.setText(f"El fichero tiene {num_lineas} lineas")

app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Hola PyQt6")
#ventana.resize(400, 300)
# ventana.move(100, 100)
# ventana.setFixedSize(400,300)  # Fija el tamaño a 400x300
ventana.setGeometry(10, 10, 400, 300) # Pone l aventana el la posicion (10,10) y tamaño 400 de ancho, 300 de alto


label = QLabel("Fichero:", ventana)
label.move(20,20)

edit_filename =QLineEdit(ventana)
edit_filename.move(100, 20)
edit_filename.resize(100, 25)

btn_cargar = QPushButton("Analizar", ventana)
btn_cargar.move(200, 20)
btn_cargar.clicked.connect(analiza_fichero)

label = QLabel("Nº de lineas del fichero: ", ventana)
label.setStyleSheet("font-weight: bold")
label.move(20, 60)

label_lineas = QLabel("", ventana)
label_lineas.move(20, 80)
label_lineas.resize(350,25)
label_lineas.setStyleSheet("background-color: rgb(255, 255, 0);")

ventana.show()

sys.exit(app.exec())