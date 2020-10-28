import sys
from PyQt5 import QtWidgets,QtGui
def pencere():
    app =QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("pYQt5 DERS 2")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("pypy.png"))
    etiket2.move(100,100)
    etiket1.setText("Burası bir yazıdır")
    etiket1.move(200,30)
    pencere.setGeometry(100,100,500,500)
    #100 100 EKRANDA Kİ KONUM 500 500 PENCERE BOTULARIMIZ
    pencere.show()
    sys.exit(app.exec_())
pencere()