import sys
from PyQt5.QtWidgets import QWidget, QApplication , QLabel ,QPushButton, QVBoxLayout, QTextEdit
class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yazialani = QTextEdit()
        self.temizle = QPushButton("TEMİZLE")
        v_box =QVBoxLayout()
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazialani)
        self.setWindowTitle("Yazı Alanı ")

        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)

        self.show()
    def click(self):
        self.yazialani.clear()
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())