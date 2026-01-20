'''
Ejercicio 1  (ejercicio_1.py). Escribir un programa que simule un contador.
Tendrá dos botones: boton + que incrementara el
contador ; botón - que lo decrementará. EL valor del contador debe mostrarse en todo momento en la ventana.
'''
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys


def incrementa():
    # Sin utilizar variable global contador
    contador = int( lbl_contador.text() ) + 1
    lbl_contador.setText(str(contador))

    # Utilizando variable global contador
    ''' global contador
    contador += 1
    lbl_contador.setText(str(contador))'''

def decrementa():
    # Sin utilizar variable global contador
    contador = int( lbl_contador.text() ) - 1
    lbl_contador.setText(str(contador))

    # Utilizando variable global contador
    '''global contador
    contador -= 1
    lbl_contador.setText(str(contador))'''

def crea_ventana():
    global ventana
    ventana = QWidget()
    ventana.setWindowTitle("Contador")
    # ventana.resize(400, 300)
    # ventana.move(100, 100)
    # ventana.setFixedSize(400,300)  # Fija el tamaño a 400x300
    ventana.setGeometry(10, 10, 400, 300)  # Pone l aventana el la posicion (10,10) y tamaño 400 de ancho, 300 de alto
    return ventana


def crea_widgets(ventana):
    global lbl_contador
    # Si usamos una variable contador
    # global contador
    # contador = 0

    btn_decrementa = QPushButton("-", ventana)
    btn_decrementa.move(20, 20)
    btn_decrementa.resize(40,25)
    btn_decrementa.clicked.connect(decrementa)
    btn_decrementa.setStyleSheet("""
        QPushButton {
            background-color: #ff00ff;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #fa000a;
            color: #ffffff;
        }
    """)

    btn_incrementa = QPushButton("+", ventana)
    btn_incrementa.move(80, 20)
    btn_incrementa.resize(40, 25)
    btn_incrementa.clicked.connect(incrementa)

    lbl_contador = QLabel("0", ventana)
    lbl_contador.move(150, 20)
    lbl_contador.resize(40, 25)
    lbl_contador.setStyleSheet("font-weight: bold; "
                               "background-color: #ffff00;"
                               "font-size: 20px;"
                               "color:#ff0000;"
                               "border: 1px solid #ff00ab;"
                               "border-radius: 10px;"
                               "padding: 2px;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = crea_ventana()
    crea_widgets(ventana)
    ventana.show()
    sys.exit(app.exec())

