from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFrame, QTableWidget,
    QTableWidgetItem, QPushButton, QStackedWidget, QMessageBox
)

from .ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction
from dao.articulos_dao import ArticulosDao


class UIListadoArticulos(QWidget):
    """
    Panel de la interfaz para mostrar el listado de artículos.

    Muestra una tabla con los campos:
    Referencia | Descripción | Precio | Stock | Observaciones
    """

    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)

        self.articulos_dao = articulos_dao
        self.config_ui()

    # ----------------------------------------------
    #   CONFIGURACIÓN UI
    # ----------------------------------------------

    def config_ui(self) -> None:

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(1)

        # Título
        titulo = LabelTitulo("LISTADO DE ARTÍCULOS")
        layout.addWidget(titulo, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Frame contenedor
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setLineWidth(2)
        frame.setMaximumWidth(800)
        frame.setStyleSheet("background-color: white;")

        frame_layout = QVBoxLayout(frame)

        # Tabla
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(
            ["Referencia", "Descripción", "Precio", "Stock", "Observaciones"]
        )

        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tabla.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        frame_layout.addWidget(self.tabla)

        # # Botón refrescar
        # boton_refrescar = BotonAction("Refrescar")
        # boton_refrescar.clicked.connect(self.cargar_datos)
        # frame_layout.addWidget(boton_refrescar)

        layout.addWidget(frame)

        layout.addStretch(1)

        self.cargar_datos()

    # ----------------------------------------------
    #   FUNCIONALIDAD
    # ----------------------------------------------

    def cargar_datos(self) -> None:
        """
        Carga los artículos en la tabla desde el DAO
        """

        try:
            articulos = self.articulos_dao.find_all()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        self.tabla.setRowCount(0)

        for fila, articulo in enumerate(articulos):
            self.tabla.insertRow(fila)

            self.tabla.setItem(fila, 0, QTableWidgetItem(articulo.get("referencia", "")))
            self.tabla.setItem(fila, 1, QTableWidgetItem(articulo.get("descripcion", "")))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(articulo.get("precio", ""))))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(articulo.get("stock", ""))))
            self.tabla.setItem(fila, 4, QTableWidgetItem(articulo.get("observaciones", "")))

        self.tabla.resizeColumnsToContents()
