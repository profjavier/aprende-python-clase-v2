from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Hola PyQt6")
ventana.resize(400, 300)
ventana.show()

sys.exit(app.exec())
