from PyQt5 import uic,QtWidgets
import plotly
import plotly.graph_objects as go
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
        Visualization.lineEdit_3.setText(str(simulationFinal.sensor_Water_Level.setWaterLevel))
        break
def showGraphic():
    excel_file = 'teste.xlsx'
    df = pd.read_excel(excel_file)
    Temperature = [go.Bar(x=df["Temperatura"], y=df["Duração Da Agua"])]
    Humidity = [go.Bar(x=df["Humidade"], y=df["Duração Da Agua"])]
    WaterLevel = [go.Bar(x=df["NivelAgua"], y=df["Duração Da Agua"])]
    fig = go.Figure(Temperature)
    fig2 = go.Figure(Humidity)
    fig3 = go.Figure(WaterLevel)
    plotly.offline.plot(fig, filename="temperature.html")
    plotly.offline.plot(fig2, filename="Humidity.html")
    plotly.offline.plot(fig3, filename="WaterLevel.html")


app = QtWidgets.QApplication([])

telaInicial = uic.loadUi("TelaInicial.ui")
Visualization = uic.loadUi("Visualization.ui")

telaInicial.pushButton.clicked.connect(executeAlgorithmAndVisualizateData) #execute the irrigation Algorithm
telaInicial.pushButton_2.clicked.connect(openVisualizationFile) # showing the values of sensors
Visualization.pushButton.clicked.connect(backMenu) # back to the main Menu
telaInicial.pushButton_3.clicked.connect(showGraphic) # show graphics 

telaInicial.show()
app.exec()