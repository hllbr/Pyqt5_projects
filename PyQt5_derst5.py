#butonlara fonksiyonel özellikler kazandırmak gibi effektif yapılanmalar üzerinde çalışıyoruz
import sys
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    #burada bir miraz alma işlemi gerçekleştirildi
    #hem normal bir pencere hemde ekxtra özellikler ekleyeceğiz
    def __init__(self):
        super().__init__()
        #burdan sonra ekstradan bir alan özellik ekliyoruz üst kısım standart bir yapı için geçerli
        self.init__uı()
    def init__uı(self):
        self.yazı_alanı = QtWidgets.QLabel("Bana henüz tıklanmadı ")
        self.button =QtWidgets.QPushButton("BANA TIKLA")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.yazı_alanı)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.button.clicked.connect(self.click)
        self.show()
    def click(self):
        self.say+=1
        self.yazı_alanı.setText("bana "+str(self.say)+" kez tıklandı")


app = QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())


