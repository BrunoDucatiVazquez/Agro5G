from traceback import print_tb
from PyQt5 import uic,QtWidgets
import Fuzzy_Logic as fz 

app = QtWidgets.QApplication([])
# login = uic.loadUi("view/Login.ui")
visualizar = uic.loadUi("view/visualizar.ui")
# login.pushButton.clicked.connect(verificaUsuario)

visualizar.pushButton.clicked.connect(fz.cadastra_Banco)

temperatura = visualizar.spinBox
Umidade = visualizar.spinBox_2
Nivel_Agua = visualizar.spinBox_3


visualizar.show()
app.exec()