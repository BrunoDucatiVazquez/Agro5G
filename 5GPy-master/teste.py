import threading
import PySimpleGUI as sg
import simulationFinal

class Agro5G():
    counter = 1
    while counter <=3:
        sg.theme('DarkAmber')   # Add a little color to your windows
        layout = [  [sg.Text('Temperatura'), sg.InputText(simulationFinal.soil_sensor_Temperature.setTemperature)],
                          [sg.Text('Humidade'), sg.InputText(simulationFinal.sensor_Humidity.setHumidity)],
                          [sg.Text('Nivel da Agua'), sg.InputText(simulationFinal.sensor_Water_Level.setWaterLevel)],]
        # Create the Window
        window = sg.Window('Plataforma Agro5G', layout)
        # Event Loop to process "events"
        while True: 
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
        counter+=1

