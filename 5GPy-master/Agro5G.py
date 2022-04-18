from PyQt5 import uic,QtWidgets


def openVisualizationFile():
    telaInicial.close()
    Visualization.show()

def backMenu():
    Visualization.close()
    telaInicial.show()

def executeAlgorithmAndVisualizateData(self):
    import simulationFinal
    temperatureValue = Visualization.lineEdit.setText(str(simulationFinal.soil_sensor_Temperature.setTemperature))
    humididtyValeu = Visualization.lineEdit_2.setText(str(simulationFinal.sensor_Humidity.setHumidity))
    waterLevelValue = Visualization.lineEdit_3.setText(str(simulationFinal.sensor_Water_Level.setWaterLevel))

app = QtWidgets.QApplication([])

telaInicial = uic.loadUi("TelaInicial.ui")
Visualization = uic.loadUi("Visualization.ui")

telaInicial.pushButton.clicked.connect(executeAlgorithmAndVisualizateData) #execute the irrigation Algorithm
telaInicial.pushButton_2.clicked.connect(openVisualizationFile)
Visualization.pushButton.clicked.connect(backMenu) # back to the main Menu

telaInicial.show()
app.exec()