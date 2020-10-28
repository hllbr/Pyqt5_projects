import sys
from PyQt5 import QtWidgets,QtGui
def pencere():
    app =QtWidgets.QApplication(sys.argv)


    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("pYQt5 DERS 3")
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Burası bir butondur.")
    etiket1=QtWidgets.QLabel(pencere)
    etiket1.setText("MERHABA YOLCU ")
    etiket1.move(200,30)
    buton.move(190,80)
    pencere.setGeometry(100,100,500,500)
    #100 100 EKRANDA Kİ KONUM 500 500 PENCERE BOTULARIMIZ
    pencere.show()
    sys.exit(app.exec_())
pencere()