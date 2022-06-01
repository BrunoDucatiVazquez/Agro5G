from PyQt5 import uic,QtWidgets
import plotly
import plotly.express as px
import pandas as pd

def openVisualizationFile():
    telaInicial.close()
    Visualization.show()

def backMenu():
    Visualization.close()
    telaInicial.show()

def executeAlgorithmAndVisualizateData(self):
    while True:
        import simulationFinal
        Visualization.lineEdit.setText(str(simulationFinal.soil_sensor_Temperature.setTemperature))
        Visualization.lineEdit_2.setText(str(simulationFinal.sensor_Humidity.setHumidity))
        Visualization.lineEdit_3.setText(str(simulationFinal.sensor_Ph.setPh))
        break
    
def showGraphic():
    excel_file = 'teste.xlsx'
    df = pd.read_excel(excel_file)
    fig = px.bar(df, x="Temperatura", y="Duração Da Agua", barmode="group")
    fig2 = px.bar(df, x="Humidade", y="Duração Da Agua", barmode="group")
    fig3 = px.bar(df, x="Ph", y="Duração Da Agua", barmode="group")
    plotly.offline.plot(fig, filename="temperature.html")
    plotly.offline.plot(fig2, filename="Humidade.html")
    plotly.offline.plot(fig3, filename="Ph.html")


app = QtWidgets.QApplication([])

telaInicial = uic.loadUi("TelaInicial.ui")
Visualization = uic.loadUi("Visualization.ui")

telaInicial.pushButton.clicked.connect(executeAlgorithmAndVisualizateData) #execute the irrigation Algorithm
telaInicial.pushButton_2.clicked.connect(openVisualizationFile) # showing the values of sensors
Visualization.pushButton.clicked.connect(backMenu) # back to the main Menu
telaInicial.pushButton_3.clicked.connect(showGraphic) # show graphics 

telaInicial.show()
app.exec()
