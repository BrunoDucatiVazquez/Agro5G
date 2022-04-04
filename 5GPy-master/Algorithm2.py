import simulationFinal
import threading
from tkinter import *

class Algorithm2:
  def run():
    pass

class IrrigationIoT(Algorithm2,object):
  def run():
    #Entrada da Umidade
        while True:
          ur = simulationFinal.sensor_Humidity.setHumidity
          if  ur > 60 and ur < 100:
            print("A umidade calculada foi de {}%".format(ur))
          else:
            print("A umidade calculada foi de {} %, nao precisa irrigar".format(ur))
          break

global counter
counter = 0
def visualizacao():
  global counter
  if counter < 2:
    janela = Tk()
    janela.title("Testando interface Grafica")
    texto_orientacao = Label(janela, text="Visualização dos dados")
    texto_orientacao.grid(column=0, row=0)
    texto_orientacao2 = Label(janela, text="Leitor de Humidade")
    texto_orientacao2.grid(column=1, row=0)
    text_dados = Label(janela, text=simulationFinal.sensor_Humidity.setHumidity)
    text_dados2 = Label(janela, text=simulationFinal.soil_sensor_Temperature.setTemperature)
    text_dados3 = Label(janela, text=simulationFinal.sensor_Water_Level.setWaterLevel)
  
    text_dados.grid(column=0,row=1)
    text_dados2.grid(column=0,row=2)
    text_dados3.grid(column=0,row=3)
  
    janela.after(400,visualizacao)
    janela.mainloop()
    


threading.Thread(target=visualizacao).start()
threading.Thread(target=IrrigationIoT).start()