import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QMainWindow, QStatusBar, QScrollArea

from widgets.components_ui import BotonMenu, LabelItem, EditItem, BotonAction


class ListadoArticulosUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.config_ui()
        self.crear_widgets()

    def config_ui(self):
        self.layout_panel_listado = QVBoxLayout(self)
        self.layout_panel_listado.setContentsMargins(20, 20, 20, 20)
        self.layout_panel_listado.setSpacing(10)
    def crear_widgets(self):
        # Label + Edit
        label = LabelItem("Listado")
        label.setFixedHeight(25)
        label.setStyleSheet("color:#ffffff;font-size: 20px;")
        self.layout_panel_listado.addWidget(label)

        # Sin scroll
        '''self.lbl_salida= QLabel(panel_listado)
        self.lbl_salida.setStyleSheet("background-color:#F5F5DC; padding:5 10 5 10;;font-size: 16px;")
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_panel_listado.addWidget( self.lbl_salida)'''
        # Con scroll
        self.lbl_salida = QLabel(self)
        self.lbl_salida.setStyleSheet("background-color:#F5F5DC; padding:5 10 5 10;;font-size: 16px;")
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_salida = QScrollArea()
        scroll_salida.setWidgetResizable(True)
        scroll_salida.setWidget(self.lbl_salida)
        # Cambiar colores del scroll vertical
        '''scroll_salida.setStyleSheet("""
        QScrollBar:vertical {
            background: #f0f0f0;          /* color del track */
            width: 15px;                   /* ancho del scroll */
            margin: 0px 0px 0px 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            background: #c71585;           /* color de la “manija” */
            min-height: 20px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        """)'''
        self.layout_panel_listado.addWidget(scroll_salida)

    def listar(self):
        salida = '<span style="color:#ff0000;">Listado de entradas</span><br>'
        # for entrada in self.entradas:
        #     salida += entrada + "<br>"
        self.lbl_salida.setText(salida)




