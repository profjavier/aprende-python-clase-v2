from PyQt6.QtWidgets import QHBoxLayout, QWidget
from mis_widgets.widgets_ui import LabelItem, EditItem

class FormItem(QWidget):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title = title
        self.config_ui()
        self.crear_widgets()

    def config_ui(self):
        self.layout_fila= QHBoxLayout()
        self.layout_fila.setSpacing(10)

    def crear_widgets(self):
        label = LabelItem(self.title)
        label.setFixedWidth(100)
        self.item = EditItem()
        self.item.setFixedWidth(200)

        # Fila item entrada
        self.layout_fila.addStretch(1)
        self.layout_fila.addWidget(label)
        self.layout_fila.addWidget(self.item)
        self.layout_fila.addStretch(1)

        self.setLayout(self.layout_fila)