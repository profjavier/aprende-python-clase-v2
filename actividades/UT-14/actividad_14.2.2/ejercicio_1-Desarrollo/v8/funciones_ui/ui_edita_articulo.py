from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QStackedWidget, QLabel, QLineEdit, QFrame, QTextEdit, QFormLayout, QMessageBox, QHBoxLayout
)

from .ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction
from dao.articulos_dao import ArticulosDao

class UIEditaArticulo(QWidget):
    """

    """

    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        """
        """
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()

    # ----------------------------------------------
    #   CONFIGURACIÓN DE LA INTERFAZ
    # ----------------------------------------------

    def config_ui(self) -> None:
        """
        """
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Stretch arriba para centrar verticalmente
        layout.addStretch(1)

        # Título centrado
        label = LabelTitulo("EDITA ARTÍCULO")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)

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

        # Campos del formulario
        # self.referencia_buscada = EditItem()
        # self.referencia_buscada.setMaximumWidth(100)
        # form_layout.addRow(LabelItem("Referencia:"), self.referencia_buscada)
        self.referencia_buscada_widget(form_layout)

        # Campos del formulario
        self.referencia = EditItem()
        self.referencia.setMaximumWidth(100)
        form_layout.addRow(LabelItem("Referencia:"), self.referencia)

        self.descripcion = EditItem()
        self.descripcion.setMaximumWidth(400)
        form_layout.addRow(LabelItem("Descripción:"), self.descripcion)

        self.precio = EditItem()
        self.precio.setMaximumWidth(70)
        form_layout.addRow(LabelItem("Precio:"), self.precio)

        self.stock = EditItem()
        self.stock.setMaximumWidth(70)
        form_layout.addRow(LabelItem("Stock:"), self.stock)

        # Observaciones en línea separada
        label_obs = LabelItem("Observaciones:")
        form_layout.addRow(label_obs)
        self.observaciones = TextItem()
        self.observaciones.setMaximumWidth(500)
        self.observaciones.setFixedHeight(80)
        form_layout.addRow(self.observaciones)

        # Botón Consultar alineado a la derecha
        boton_guardar = BotonAction("Modificar")
        boton_guardar.setFixedWidth(75)
        boton_guardar.clicked.connect(self.guardar_articulo)

        boton_layout = QVBoxLayout()
        boton_layout.addWidget(boton_guardar, alignment=Qt.AlignmentFlag.AlignRight)
        form_layout.addRow(boton_layout)

        # Añade el formulario al layout principal
        layout.addWidget(widget_form)

        # Stretch abajo para centrar verticalmente
        layout.addStretch(1)

        self.init_form()

    def referencia_buscada_widget(self, form_layout):
        busqueda_frame = QFrame()
        busqueda_frame.setFrameShape(QFrame.Shape.Box)
        busqueda_frame.setStyleSheet("background-color: #eef5ff;")
        busqueda_layout = QHBoxLayout(busqueda_frame)
        busqueda_layout.setContentsMargins(10, 10, 10, 10)

        self.referencia_buscada = EditItem()
        self.referencia_buscada.setMaximumWidth(100)
        busqueda_layout.addWidget(LabelItem("Referencia a buscar:"))

        self.referencia_buscada = EditItem()
        busqueda_layout.addWidget( self.referencia_buscada)

        boton_consultar = BotonAction("Buscar")
        boton_consultar.setFixedWidth(75)
        boton_consultar.clicked.connect(self.consultar_articulo)
        busqueda_layout.addWidget(boton_consultar)


        # Añade el bloque de búsqueda antes del formulario principal
        form_layout.addRow(busqueda_frame)

    # ----------------------------------------------
    #   FUNCIONALIDADES
    # ----------------------------------------------

    def consultar_articulo(self) -> None:
        """
        """
        referencia_buscada = self.referencia_buscada.text()

        articulo = self.articulos_dao.find(referencia_buscada)
        self.init_form()

        if articulo:
            self.referencia.setText(articulo.get("referencia"))
            self.descripcion.setText(articulo.get("descripcion"))
            self.precio.setText( str(articulo.get("precio")) )
            self.stock.setText( str(articulo.get("stock")) )
            self.observaciones.setText(articulo.get("observaciones"))
            self.activa_items_form(True)
        else:
            QMessageBox.warning(self, "Error", "No se ha encontrado la referncia indicada.",
                                QMessageBox.StandardButton.Close)

    def guardar_articulo(self) -> None:
        """
        """
        articulo = {}
        articulo["referencia"] = self.referencia.text()
        articulo["descripcion"] = self.descripcion.text()
        articulo["precio"] = self.precio.text()
        articulo["stock"] = self.stock.text()
        articulo["observaciones"] = self.observaciones.text()


        if self.articulos_dao.update(articulo["referencia"], articulo):
            QMessageBox.information(self, "Actualizacion realizada", f"Se ha actualizado el articulo de referencia: {articulo["referencia"]}.",
                                QMessageBox.StandardButton.Close)
            self.init_form()
        else:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el articulo de referencia: {articulo["referencia"]}.",
                                QMessageBox.StandardButton.Close)

    def init_form(self):
        self.referencia_buscada.clear()
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.setText("")

        self.referencia.setDisabled(True)
        self.activa_items_form(False)

    def activa_items_form(self, activar:bool) -> None:
        self.descripcion.setDisabled(not activar)
        self.precio.setDisabled(not activar)
        self.stock.setDisabled(not activar)
        self.observaciones.setDisabled(not activar)

