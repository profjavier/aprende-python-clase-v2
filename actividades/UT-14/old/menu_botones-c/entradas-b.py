import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget, QLabel, QLineEdit, QVBoxLayout, \
    QHBoxLayout, QFormLayout, QGridLayout, QSizePolicy

from ui import BotonMenu, LabelItem, EditItem, BotonAction


class Entradas(QWidget):
    def __init__(self):
        super().__init__()
        self.entradas = []
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Menu botones - Entradas")
        self.resize(600, 500)
        self.crear_widgets()

    def crear_widgets(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        panel_menu = QWidget()
        panel_menu.setStyleSheet("background-color: #c71585;")
        self.crear_menu(panel_menu)

        self.panel_central = QStackedWidget()
        self.panel_central.setStyleSheet("background-color: #8B0000;")
        self.crear_widgets_entrada(self.panel_central)
        self.crear_widgets_listado(self.panel_central)

        panel_estado = QWidget()
        panel_estado.setStyleSheet("background-color: #c71585;")

        panel_menu.setFixedHeight(50)
        panel_estado.setFixedHeight(50)

        layout.addWidget(panel_menu)
        layout.addWidget(self.panel_central, 1)  # 👈 se estira
        layout.addWidget(panel_estado)


        self.setLayout(layout)




    def crear_menu(self,panel_menu):
        layout = QHBoxLayout(panel_menu)
        self.boton_nueva = BotonMenu("Nueva", panel_menu)
        self.boton_nueva.setCheckable(True)
        self.boton_nueva.setChecked(True)
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = BotonMenu("Listado", panel_menu)
        self.boton_listado.setCheckable(True)
        self.boton_listado.setChecked(False)
        self.boton_listado.clicked.connect(self.listado_entradas)

        self.boton_salir = BotonMenu("Salir", panel_menu)
        self.boton_salir.setCheckable(True)
        self.boton_salir.clicked.connect(self.cerrar_app)

        layout.addWidget(self.boton_nueva)
        layout.addWidget(self.boton_listado)
        layout.addWidget(self.boton_salir)
        panel_menu.setLayout(layout)

    def crear_widgets_entrada(self, panel_central):
        panel_nuevo = QWidget()

        # Layout principal
        main_layout = QVBoxLayout(panel_nuevo)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # 🔹 Stretch superior → centra verticalmente
        main_layout.addStretch(1)

        # --- Fila centrada (Label + Edit) ---
        center_row = QHBoxLayout()
        center_row.setSpacing(10)

        label = LabelItem("Entrada")
        self.edit_entrada = EditItem()
        self.edit_entrada.setMinimumWidth(70)
        self.edit_entrada.setMaximumWidth(150)

        # 🔹 Stretch izquierda
        center_row.addStretch(1)
        center_row.addWidget(label)
        center_row.addWidget(self.edit_entrada)
        # 🔹 Stretch derecha
        center_row.addStretch(1)

        main_layout.addLayout(center_row)


        # 🔹 Stretch inferior → centra verticalmente
        main_layout.addStretch(1)

        # --- Botón abajo a la derecha ---
        button_layout = QHBoxLayout()

        boton_guardar = BotonAction("Guardar")
        boton_guardar.setMinimumWidth(70)
        boton_guardar.setMaximumWidth(150)
        boton_guardar.clicked.connect(self.guardar)

        button_layout.addStretch(1)
        button_layout.addWidget(boton_guardar)

        main_layout.addLayout(button_layout)

        panel_central.addWidget(panel_nuevo)
        self.panel_nuevo = panel_nuevo

    # def crear_widgets_entrada(self, panel_central):
    #     # Creamos un panel contenedor
    #     panel_nuevo = QWidget()
    #
    #     # Creamos layout
    #     layout = QFormLayout()
    #     layout.setContentsMargins(20, 20, 20, 20)
    #     layout.setSpacing(10)
    #     panel_nuevo.setLayout(layout)
    #
    #     # Label + Edit
    #     label = LabelItem("Entrada")
    #     self.edit_entrada = EditItem()
    #     layout.addRow(label, self.edit_entrada)
    #
    #     # Botón Guardar
    #     boton_guardar = BotonAction("Guardar")
    #     boton_guardar.clicked.connect(self.guardar)
    #     layout.addRow(boton_guardar)
    #
    #     # Añadimos el panel al QStackedWidget
    #     panel_central.addWidget(panel_nuevo)
    #
    #     # Guardamos referencia si queremos acceder después
    #     self.panel_nuevo = panel_nuevo

    def crear_widgets_listado(self, panel_central):
        # Creamos un panel contenedor
        panel_listado = QWidget()

        # Creamos layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        panel_listado.setLayout(layout)

        # Label + Edit
        label = LabelItem("Listado")
        label.setFixedHeight(50)  # 🔹 altura fija 50px
        layout.addWidget(label)

        self.lbl_salida= QLabel(panel_listado)
        self.lbl_salida.setStyleSheet("background-color:#ffff00; padding-left:10px;")
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget( self.lbl_salida)

        # Añadimos el panel al QStackedWidget
        panel_central.addWidget(panel_listado)

        # Guardamos referencia si queremos acceder después
        self.panel_listado = panel_listado

    '''        panel_nuevo = QWidget()
            layout = QGridLayout()
            LabelItem("Entrada")
            layout.addWidget(LabelItem("Entrada"), 0, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(LabelItem("Entrada"), 1, 1, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
            panel_nuevo.setLayout(layout)
            panel_central.addWidget(panel_nuevo)
    def crear_widgets_entradaX(self, panel_central):
        # Layout principal
        panel_nuevo = QWidget()
        layout = QGridLayout(panel_nuevo)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(10)

        # Widgets
        label = LabelItem("Entrada")
        edit = EditItem()
        edit.setMinimumWidth(70)
        edit.setMaximumWidth(150)

        boton_guardar = BotonAction("Guardar")
        boton_guardar.setMinimumWidth(70)
        boton_guardar.setMaximumWidth(150)
        boton_guardar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        boton_guardar.clicked.connect(self.guardar)

        # Añadimos al grid
        layout.addWidget(label, 0, 0)
        layout.addWidget(edit, 0, 1)
        layout.addWidget(boton_guardar, 1, 0, 8, 2)  # Ocupa 2 columnas

        # Stretch para que el grid se expanda y el botón ocupe todo horizontal
        # layout.setColumnStretch(0, 1)
        # layout.setColumnStretch(1, 1)
        # layout.setRowStretch(0, 1)
        # layout.setRowStretch(1, 0)  # fila del botón, altura fija

        panel_central.addWidget(panel_nuevo)
        self.panel_nuevo = panel_nuevo'''


    '''    def crear_widgets_entrada(self, panel_central):
        layout = QFormLayout()
        label = LabelItem("Entrada")
        # label.move(20, 30)
        self.edit_entrada = EditItem()
        # self.edit_entrada.setGeometry(20, 60, 150, 30)
        layout.addRow(label, self.edit_entrada)

        boton_guardar = BotonAction("Guardar")
        # boton_guardar.setGeometry(200, 60, 80, 30)
        layout.addRow(boton_guardar)
        boton_guardar.clicked.connect(self.guardar)

        panel_central.setLayout(layout)'''

    '''def crear_widgets(self):
        self.crear_botones_menu()

        self.panel_datos = QStackedWidget(self)
        self.panel_datos.setGeometry(0, 40, 600, 560)
        self.setStyleSheet("background-color:#E9967A;")

        # Panel opción ueva entrada
        panel_nueva = QWidget(self.panel_datos)
        panel_nueva.setStyleSheet("background-color:#8B0000;")
        label = LabelItem("Entrada", panel_nueva)
        label.move(20, 30)


        self.edit_entrada = EditItem(panel_nueva)
        self.edit_entrada.setGeometry(20, 60, 150, 30)

        boton_guardar = BotonAction("Guardar", panel_nueva)
        boton_guardar.setGeometry(200, 60, 80, 30)

        boton_guardar.clicked.connect(self.guardar)

        panel_listado = QWidget(self.panel_datos)
        panel_listado.setStyleSheet("background-color:#aa00aa;")
        label = LabelItem("Listado", panel_listado)
        label.move(20, 20)

        self.lbl_salida= QLabel(panel_listado)
        self.lbl_salida.setGeometry(20, 50, 570, 400)
        self.lbl_salida.setStyleSheet("background-color:#ffff00; padding-left:10px;")
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)


        self.panel_datos.addWidget(panel_nueva)
        self.panel_datos.addWidget(panel_listado)


    def crear_botones_menu(self):
        panel_botones = QWidget(self)
        panel_botones.setGeometry(0, 0, 600, 40)
        panel_botones.setStyleSheet("background-color:#FF0000;")

        self.boton_nueva = BotonMenu("Nueva", panel_botones)
        self.boton_nueva.setGeometry(0, 0, 80, 30)
        self.boton_nueva.setCheckable(True)
        self.boton_nueva.setChecked(True)
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = BotonMenu("Listado", panel_botones)
        self.boton_listado.setGeometry(100, 0, 80, 30)
        self.boton_listado.setCheckable(True)
        self.boton_listado.setChecked(False)
        self.boton_listado.clicked.connect(self.listado_entradas)

        self.boton_salir = BotonMenu("Salir", panel_botones)
        self.boton_salir.setGeometry(200, 0, 80, 30)
        self.boton_salir.setCheckable(True)
        self.boton_salir.clicked.connect(self.cerrar_app)'''


    def nueva_entrada(self):
        self.panel_central.setCurrentIndex(0)
        self.boton_nueva.setChecked(True)
        self.boton_listado.setChecked(False)

    def listado_entradas(self):
        self.panel_central.setCurrentIndex(1)
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(True)
        self.listar()

    def cerrar_app(self):
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(False)
        self.boton_salir.setChecked(True)
        sys.exit()


    def guardar(self):
        entrada = self.edit_entrada.text()
        self.entradas.append(entrada)
        print(self.entradas)
        self.edit_entrada.clear()

    def listar(self):
        salida = '<span style="color:#ff0000;">Listado de entradas</span><br>'
        for entrada in self.entradas:
           salida += entrada + "<br>"
        self.lbl_salida.setText(salida)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Entradas()
    ventana.show()
    sys.exit(app.exec())