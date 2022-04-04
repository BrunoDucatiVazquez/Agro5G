import threading
import simulationFinal
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

# global counter
# counter = 0
# def visualizacao():
#   global counter
#   if counter < 2:
#     janela = Tk()
#     janela.title("Testando interface Grafica")
#     texto_orientacao = Label(janela, text="Visualização dos dados")
#     texto_orientacao.grid(column=0, row=0)
#     text_dados = Label(janela, text=simulationFinal.sensor_Humidity.setHumidity)
  
#     text_dados.grid(column=0,row=1)
  
#     janela.after(400,visualizacao)
#     janela.mainloop()


threading.Thread(target=visualizacao).start()
threading.Thread(target=simulationFinal.FuzzyLogic).start()
