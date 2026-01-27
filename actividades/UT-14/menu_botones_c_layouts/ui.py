from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit


class BotonMenu(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
                QPushButton {
                    background-color: #cccccc;
                    border: 1px solid #444;
                    padding: 5px;
                    border-radius: 5px;
                }
               QPushButton:checked  {
                    background-color: #ffebcd;
                    font-weight: bold;
                    border-bottom: 2px solid #000000;
                }
        """)
        self.setCheckable(True)
        #self.resize(100,40)

class LabelItem(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("font-weight:bold; color:#ffffff;")


class EditItem(QLineEdit):
    def __init__(self, parent=None, placeholder=""):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #444;
                padding: 5px;
                border-radius: 5px;
            }
            QLineEdit:hover {
                border: 2px solid #20b2aa;
            }
            QLineEdit:focus {
                border: 2px solid #1e90ff;
            }         
        """)

class BotonAction(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
                QPushButton {
                    background-color: #ba55d3;
                    border: 1px solid #444;
                    padding: 5px;
                    border-radius: 5px;
                }
               QPushButton:hover  {
                    background-color: #c71585;
                    font-weight: bold;
                    border-bottom: 2px solid #c71585;
                }
                QPushButton:pressed  {
                    background-color: #ff0000;
                    font-weight: bold;
                    border-bottom: 2px solid #c71585;
                }
        """)
