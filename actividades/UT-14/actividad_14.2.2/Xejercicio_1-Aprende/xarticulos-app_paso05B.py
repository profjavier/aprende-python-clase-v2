import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, \
    QLineEdit


class ArticulosApp(QWidget):
    def __init__(self):
        super().__init__()
        self.articulos = []
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Menu botones - Entradas")
        self.resize(600, 500)

        # Configuracion layouts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.panelMenu = QWidget(self)
        layout.addWidget(self.panelMenu)
        self.panelMenu.setStyleSheet("background-color: #AA0000;")
        self.panelMenu.setFixedHeight(50)

        self.panelCentral = QStackedWidget(self)
        layout.addWidget(self.panelCentral)
        self.panelCentral.setStyleSheet("background-color: #00AAAA;")

        self.panelStatus = QWidget(self)
        layout.addWidget(self.panelStatus)
        self.panelStatus.setStyleSheet("background-color: #00AA00;")
        self.panelStatus.setFixedHeight(50)


        self.crear_menu()
        self.crear_widgets_nuevo()
        self.crear_widgets_consulta()
        self.crear_widgets_baja()
        self.crear_widgets_edita()
        self.crear_widgets_listado()

        self.panelCentral.setCurrentIndex(0)

    def crear_menu(self):
        layout = QHBoxLayout(self.panelMenu)

        self.boton_nuevo = QPushButton("Nuevo")
        self.boton_nuevo.setStyleSheet("background-color: #00AA00;")
        self.boton_nuevo.clicked.connect(self.opcion_nuevo)
        layout.addWidget(self.boton_nuevo)

        self.boton_consulta = QPushButton("Consulta")
        self.boton_consulta.setStyleSheet("background-color: #00AA00;")
        self.boton_consulta.clicked.connect(self.opcion_consulta)
        layout.addWidget(self.boton_consulta)

        self.boton_baja = QPushButton("Baja")
        self.boton_baja.setStyleSheet("background-color: #00AA00;")
        self.boton_baja.clicked.connect(self.opcion_baja)
        layout.addWidget(self.boton_baja)

        self.boton_edita = QPushButton("Edicion")
        self.boton_edita.setStyleSheet("background-color: #00AA00;")
        self.boton_edita.clicked.connect(self.opcion_edita)
        layout.addWidget(self.boton_edita)

        self.boton_listado = QPushButton("Listado")
        self.boton_listado.setStyleSheet("background-color: #00AA00;")
        self.boton_listado.clicked.connect(self.opcion_listado)
        layout.addWidget(self.boton_listado)

        self.boton_salir = QPushButton("Salir")
        self.boton_salir.setStyleSheet("background-color: #00AA00;")
        self.boton_salir.clicked.connect(self.opcion_cerrar_app)
        layout.addWidget(self.boton_salir)

    def crear_widgets_nuevo(self):
        panel = QWidget()
        # layout_centrado = QHBoxLayout(panel)
        layout = QVBoxLayout(panel)

        layout.addStretch(1)   # Para que esté centrado verticalmente

        layout_fila = QHBoxLayout()
        layout_fila.addStretch(1)
        layout_fila.setSpacing(10)
        label = QLabel("Referencia")
        label.setFixedWidth(100)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.referencia = QLineEdit()
        self.referencia.setMaximumWidth(100)
        layout_fila.addWidget(label)
        layout_fila.addWidget(self.referencia)
        layout_fila.addStretch(1)
        layout.addLayout(layout_fila)

        layout_fila = QHBoxLayout()
        layout_fila.addStretch(1)
        layout_fila.setSpacing(10)
        label = QLabel("Descripcion")
        label.setFixedWidth(100)
        self.descripcion = QLineEdit()
        self.descripcion.setMaximumWidth(100)
        layout_fila.addWidget(label)
        layout_fila.addWidget(self.descripcion)
        layout_fila.addStretch(1)
        layout.addLayout(layout_fila)

        layout_fila = QHBoxLayout()
        layout_fila.addStretch(1)
        layout_fila.setSpacing(10)
        label = QLabel("Precio")
        label.setFixedWidth(100)
        self.precio = QLineEdit()
        self.precio.setMaximumWidth(100)
        layout_fila.addWidget(label)
        layout_fila.addWidget(self.precio)
        layout_fila.addStretch(1)
        layout.addLayout(layout_fila)

        layout_fila = QHBoxLayout()
        layout_fila.addStretch(1)
        layout_fila.setSpacing(10)
        label = QLabel("Stock")
        label.setFixedWidth(100)
        self.stock = QLineEdit()
        self.stock.setMaximumWidth(100)
        layout_fila.addWidget(label)
        layout_fila.addWidget(self.stock)
        layout_fila.addStretch(1)
        layout.addLayout(layout_fila)

        layout_fila = QHBoxLayout()
        layout_fila.addStretch(1)
        layout_fila.setSpacing(10)
        label = QLabel("Observaciones")
        label.setFixedWidth(100)
        self.observaciones = QLineEdit()
        self.observaciones.setMaximumWidth(100)
        layout_fila.addWidget(label)
        layout_fila.addWidget(self.observaciones)
        layout_fila.addStretch(1)
        layout.addLayout(layout_fila)

        layout.addStretch(1)   # Para que esté centrado verticalmente

        layout_fila = QHBoxLayout()
        layout_fila.setAlignment(Qt.AlignmentFlag.AlignRight)
        boton_guardar = QPushButton("Guardar")
        boton_guardar.setFixedWidth(75)
        boton_guardar.clicked.connect(self.guardar_articulo)
        layout_fila.addWidget(boton_guardar)
        layout.addLayout(layout_fila)

        self.panelCentral.addWidget(panel)

    def crear_widgets_consulta(self):
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Consulta"))
        self.panelCentral.addWidget(panel)

    def crear_widgets_baja(self):
        panel= QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Baja"))
        self.panelCentral.addWidget(panel)

    def crear_widgets_edita(self):
        panel= QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Edición"))
        self.panelCentral.addWidget(panel)

    def crear_widgets_listado(self):
        panel= QWidget(self.panelCentral)
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Listado"))
        self.panelCentral.addWidget(panel)



    def opcion_nuevo(self):
        self.panelCentral.setCurrentIndex(0)

    def opcion_consulta(self):
        self.panelCentral.setCurrentIndex(1)

    def opcion_baja(self):
        self.panelCentral.setCurrentIndex(2)

    def opcion_edita(self):
        self.panelCentral.setCurrentIndex(3)

    def opcion_listado(self):
        self.panelCentral.setCurrentIndex(4)

    def opcion_cerrar_app(self):
        QApplication.quit()


    def guardar_articulo(self):
        print("Guardar articulo")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())