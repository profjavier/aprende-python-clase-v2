from PyQt6.QtWidgets import QWidget, QVBoxLayout, \
    QHBoxLayout, QLabel, QGroupBox

from mis_widgets.form_items import  FormItem
from mis_widgets.widgets_ui import BotonAction

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

        '''self.form_referencia_buscar = FormItem(self, "Referencia")
        self.layout_panel_nueva.addWidget(self.form_referencia_buscar)

        self.form_referencia = FormItem(self, "Referencia")
        self.layout_panel_nueva.addWidget(self.form_referencia)
        self.form_descripcion = FormItem(self, "Descpción")
        self.layout_panel_nueva.addWidget(self.form_descripcion)
        self.form_precio = FormItem(self, "Precio")
        self.layout_panel_nueva.addWidget(self.form_precio)
        self.form_stock = FormItem(self, "Stock")
        self.layout_panel_nueva.addWidget(self.form_stock)
        self.form_observaciones = FormItem(self, "Observaciones")
        self.layout_panel_nueva.addWidget(self.form_observaciones)'''

        # ---- GRUPO BUSCAR ----
        grupo_buscar = QGroupBox("Buscar")
        grupo_buscar.setStyleSheet("background-color: #F27B63")
        layout_buscar = QVBoxLayout()

        self.form_referencia_buscar = FormItem(self, "Referencia")
        layout_buscar.addWidget(self.form_referencia_buscar)

        grupo_buscar.setLayout(layout_buscar)

        self.layout_panel_nueva.addWidget(grupo_buscar)

        # ---- GRUPO NUEVO ----
        grupo_nuevo = QGroupBox("Nuevo")
        grupo_nuevo.setStyleSheet("background-color: #F54927")
        layout_nuevo = QVBoxLayout()

        self.form_referencia = FormItem(self, "Referencia")
        layout_nuevo.addWidget(self.form_referencia)

        self.form_descripcion = FormItem(self, "Descripción")
        layout_nuevo.addWidget(self.form_descripcion)

        self.form_precio = FormItem(self, "Precio")
        layout_nuevo.addWidget(self.form_precio)

        self.form_stock = FormItem(self, "Stock")
        layout_nuevo.addWidget(self.form_stock)

        self.form_observaciones = FormItem(self, "Observaciones")
        layout_nuevo.addWidget(self.form_observaciones)

        grupo_nuevo.setLayout(layout_nuevo)

        self.layout_panel_nueva.addWidget(grupo_nuevo)

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



    def activa_items(self, estado):
        if estado:
            self.form_referencia.item.self.setStyleSheet("backgorund-color:#ffff00")
            self.layout_panel_nueva.addWidget(self.form_referencia)
            self.form_referencia = FormItem(self, "Descpción")
            self.layout_panel_nueva.addWidget(self.form_descripcion)
            self.form_precio = FormItem(self, "Precio")
            self.layout_panel_nueva.addWidget(self.form_precio)
            self.form_stock = FormItem(self, "Stock")
            self.layout_panel_nueva.addWidget(self.form_stock)
            self.form_observaciones = FormItem(self, "Observaciones")
            self.layout_panel_nueva.addWidget(self.form_observaciones)


    def guardar(self):
        entrada = self.edit_entrada.text()
        self.entradas.append(entrada)
        self.edit_entrada.clear()
        self.statusBar().showMessage(f"Número de entradas: {len(self.entradas)}")
