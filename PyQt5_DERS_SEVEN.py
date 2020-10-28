#KULLANICI GİRİŞİ PROJESİ

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("python 'ı seviyor musunuz ?")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("bana tıkla ")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("Check Box")
        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))
        #burası fonksiyon çağrısı fonksiyon objesi değil burayı bir fonksiyon objesine dönüştürmek gerekiyor
        #bunu ise lambda ile gerçekleştiriyoruz
        self.show()
    def click(self,chekbox,yazi_alani):
        if chekbox :
            yazi_alani.setText("sektördeki geleceğin gözlerinden bile parlak")
        else:
            yazi_alani.setText("Why ? ")
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())