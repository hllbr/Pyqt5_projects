#radioButton kısmında kaldınız

import sys

from PyQt5.QtWidgets import QWidget ,QApplication, QRadioButton, QLabel ,QPushButton , QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.radio_yazizi = QLabel(" hangi dili daha çok seviyorsunuz ? ")
        self.java =QRadioButton("JAVA")
        self.python = QRadioButton("PYTHON")
        self.php = QRadioButton("PHP")

        self.yazi_alani = QLabel("")

        self.buton = QPushButton("Gönder")

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazizi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.buton.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.php.isChecked(),self.yazi_alani))
        self.setWindowTitle("RADİO BUTON")
        self.show()
    def click(self,java,python,php,yazi_alani):
        if python:
            yazi_alani.setText("Python")
        if java:
            yazi_alani.setText("java")
        if php:
            yazi_alani.setText("php")


app = QApplication(sys.argv)
pencere =Pencere()
sys.exit(app.exec_())