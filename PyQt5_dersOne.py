import sys
from PyQt5 import QtWidgets
def pencere():
    app =QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("pYQt5 DERS 1 ")
    pencere.show()
    sys.exit(app.exec_())
pencere()