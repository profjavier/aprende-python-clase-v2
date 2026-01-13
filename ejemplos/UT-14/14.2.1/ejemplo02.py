from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

app = QApplication(sys.argv)

ventana = QMainWindow()
ventana.setWindowTitle("Ventana principal")
ventana.resize(500, 400)

# Área central
label = QLabel("Hola PyQt6")
ventana.setCentralWidget(label)

ventana.show()
sys.exit(app.exec())
