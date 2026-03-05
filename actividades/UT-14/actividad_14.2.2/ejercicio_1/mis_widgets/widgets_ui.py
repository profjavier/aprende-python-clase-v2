from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit


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
                        QPushButton:checked {
                            background-color: #ffebcd;
                            font-weight: bold;
                            border-bottom: 2px solid #000000;
                        }   
                        QPushButton:hover {
                            color: #20b2aa;
                            font-weight: bold;
                            border-color: #20b2aa;
                        }                             
                """)

class LabelItem(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text,parent)
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
                border: 1px solid #20b2aa;
            }

            QLineEdit:focus {
                border: 2px solid #1e90ff;
            }            
        """)

class BotonAction(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.text = text
        self.setStyleSheet("""
                        QPushButton {
                            background-color: #ba55d3;
                            border: 1px solid #444;
                            padding: 5px;
                            border-radius: 5px;
                        }
                        QPushButton:hover {
                            color: #c71585;
                            font-weight: bold;
                            border-color: #c71585;
                        }                             
                """)