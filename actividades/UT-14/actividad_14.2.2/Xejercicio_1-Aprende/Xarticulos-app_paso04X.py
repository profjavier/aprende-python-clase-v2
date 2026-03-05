import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, \
    QLineEdit, QTextEdit, QFrame, QFormLayout


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
        layout = QVBoxLayout(panel)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Contenedor del formulario con borde
        widget_form = QFrame()
        widget_form.setMaximumWidth(500)
        widget_form.setFrameShape(QFrame.Shape.Box)
        widget_form.setFrameShadow(QFrame.Shadow.Raised)
        widget_form.setLineWidth(2)
        widget_form.setStyleSheet("background-color: white;")

        # Formulario con QFormLayout
        form_layout = QFormLayout(widget_form)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setHorizontalSpacing(10)
        form_layout.setVerticalSpacing(15)

        # --- Fila vacía para simular stretch arriba ---
        form_layout.addRow(QLabel(), QLabel())

        # Campos
        self.referencia = QLineEdit()
        self.referencia.setMaximumWidth(100)
        form_layout.addRow("Referencia:", self.referencia)

        self.descripcion = QLineEdit()
        self.descripcion.setMaximumWidth(400)
        form_layout.addRow("Descripcion:", self.descripcion)

        self.precio = QLineEdit()
        self.precio.setMaximumWidth(70)
        form_layout.addRow("Precio:", self.precio)

        self.stock = QLineEdit()
        self.stock.setMaximumWidth(70)
        form_layout.addRow("Stock:", self.stock)

        # Observaciones en fila separada (label arriba, QTextEdit abajo)
        label_obs = QLabel("Observaciones:")
        self.observaciones = QTextEdit()
        self.observaciones.setMaximumWidth(400)
        self.observaciones.setFixedHeight(80)
        form_layout.addRow(label_obs, self.observaciones)

        # Botón Guardar alineado a la derecha
        boton_guardar = QPushButton("Guardar")
        boton_guardar.setFixedWidth(75)
        boton_guardar.clicked.connect(self.guardar_articulo)

        boton_layout = QVBoxLayout()
        boton_layout.addWidget(boton_guardar, alignment=Qt.AlignmentFlag.AlignRight)
        form_layout.addRow(boton_layout)

        # Añadir el formulario al layout principal
        layout.addWidget(widget_form)

        # Stretch abajo para centrar verticalmente
        layout.addStretch(1)

        self.panelCentral.addWidget(panel)

    # def crear_widgets_nuevo(self):
    #     panel = QWidget()
    #     layout = QVBoxLayout(panel)
    #     layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    #
    #     # Contenedor del formulario con borde
    #     widget_form = QFrame()
    #     widget_form.setMaximumWidth(500)
    #     widget_form.setFrameShape(QFrame.Shape.Box)
    #     widget_form.setFrameShadow(QFrame.Shadow.Raised)
    #     widget_form.setLineWidth(2)
    #     widget_form.setStyleSheet("background-color: white;")
    #
    #     # Formulario con QFormLayout
    #     form_layout = QFormLayout(widget_form)
    #     form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
    #     form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
    #     form_layout.setContentsMargins(20, 20, 20, 20)
    #     form_layout.setHorizontalSpacing(10)
    #     form_layout.setVerticalSpacing(15)
    #
    #     # --- Fila vacía para simular stretch arriba ---
    #     form_layout.addRow(QLabel(), QLabel())
    #
    #     # Campos
    #     self.referencia = QLineEdit()
    #     self.referencia.setMaximumWidth(100)
    #     form_layout.addRow("Referencia:", self.referencia)
    #
    #     self.descripcion = QLineEdit()
    #     self.descripcion.setMaximumWidth(400)
    #     form_layout.addRow("Descripcion:", self.descripcion)
    #
    #     self.precio = QLineEdit()
    #     self.precio.setMaximumWidth(70)
    #     form_layout.addRow("Precio:", self.precio)
    #
    #     self.stock = QLineEdit()
    #     self.stock.setMaximumWidth(70)
    #     form_layout.addRow("Stock:", self.stock)
    #
    #     # Observaciones en fila separada (label arriba, QTextEdit abajo)
    #     label_obs = QLabel("Observaciones:")
    #     self.observaciones = QTextEdit()
    #     self.observaciones.setMaximumWidth(400)
    #     self.observaciones.setFixedHeight(80)
    #     form_layout.addRow(label_obs, self.observaciones)
    #
    #     # Botón Guardar alineado a la derecha
    #     boton_guardar = QPushButton("Guardar")
    #     boton_guardar.setFixedWidth(75)
    #     boton_guardar.clicked.connect(self.guardar_articulo)
    #
    #     boton_layout = QVBoxLayout()
    #     boton_layout.addWidget(boton_guardar, alignment=Qt.AlignmentFlag.AlignRight)
    #     form_layout.addRow(boton_layout)
    #
    #     # Añadir el formulario al layout principal
    #     layout.addWidget(widget_form)
    #
    #     # Stretch abajo para centrar verticalmente
    #     layout.addStretch(1)
    #
    #     self.panelCentral.addWidget(panel)

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