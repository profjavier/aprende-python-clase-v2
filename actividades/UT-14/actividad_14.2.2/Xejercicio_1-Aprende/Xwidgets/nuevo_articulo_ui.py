import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QMainWindow, QStatusBar, QScrollArea

from widgets.components_ui import BotonMenu, LabelItem, EditItem, BotonAction
from widgets.form_item import FormItem

class NuevoArticuloUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.config_ui()
        self.crear_widgets()

    def config_ui(self):
        self.layout_panel_nueva = QVBoxLayout(self)
        self.layout_panel_nueva.setContentsMargins(20, 20, 20, 20)
        self.layout_panel_nueva.setSpacing(15)

    def crear_widgets(self):
        #  Stretch superior para centrar verticalmente
        self.layout_panel_nueva.addStretch(1)

        '''# --- Fila centrada (Label + Edit) ---
        layout_fila_entrada = QHBoxLayout()
        layout_fila_entrada.setSpacing(10)

        label = LabelItem("Entrada")
        self.edit_entrada = EditItem()
        self.edit_entrada.setFixedWidth(200)

        # Fila item entrada
        layout_fila_entrada.addStretch(1)
        layout_fila_entrada.addWidget(label)
        layout_fila_entrada.addWidget(self.edit_entrada)
        layout_fila_entrada.addStretch(1)'''

        # layout_fila_entrada = FormItem(self, "Referencia")
        # self.layout_panel_nueva.addLayout(layout_fila_entrada)

        self.form_referencia = FormItem(self, "Referencia")
        self.layout_panel_nueva.addWidget(self.form_referencia)

        #  Stretch inferior para centrar verticalmente
        self.layout_panel_nueva.addStretch(1)

        # --- Botón abajo a la derecha ---
        button_layout = QHBoxLayout()

        boton_guardar = BotonAction("Guardar")
        boton_guardar.setFixedWidth(100)
        boton_guardar.clicked.connect(self.guardar)

        button_layout.addStretch(1)
        button_layout.addWidget(boton_guardar)

        self.layout_panel_nueva.addLayout(button_layout)



    def guardar(self):
        entrada = self.edit_entrada.text()
        self.entradas.append(entrada)
        self.edit_entrada.clear()
        self.statusBar().showMessage(f"Número de entradas: {len(self.entradas)}")
