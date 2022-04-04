import threading
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import simulationFinal
from tkinter import *

class FuzzyLogic(object):
    def run():
        #Criando as variaveis do problema
        Soil_Moisture  = ctrl.Antecedent(np.arange(0,60,1),'Soil_Moisture')
        Soil_Temperature  = ctrl.Antecedent(np.arange(0,40,1),'Soil_Temperature')
        Water_Level = ctrl.Antecedent(np.arange(0,12,1),'Water_Level')
        #Como a duração da agua é a saida devemos colocar o metodo Consequent
        DuracaoAgua = ctrl.Consequent(np.arange(0,180,1),'DuracaoAgua')
        #Criando as funções de pertinencia para a umidade do solo
        Soil_Moisture['Molhada'] = fuzz.trapmf(Soil_Moisture.universe, [0,0,10,20])
        Soil_Moisture['Normal'] = fuzz.trapmf(Soil_Moisture.universe, [10,20,30,40])
        Soil_Moisture['Seca'] = fuzz.trapmf(Soil_Moisture.universe, [30,40,50,60])
        #Criando as funções de pertinencia para a temperatura do solo
        Soil_Temperature['Gelada'] = fuzz.trapmf(Soil_Temperature.universe, [0,1,15,20])
        Soil_Temperature['Amena'] = fuzz.trapmf(Soil_Temperature.universe, [15,20,25,30])
        Soil_Temperature['Quente'] = fuzz.trapmf(Soil_Temperature.universe, [25,30,35,40])
        #Criando as funções de pertinencia para a o Water_Level
        Water_Level['baixo'] = fuzz.trapmf(Water_Level.universe, [0,0,2,4])
        Water_Level['neutro'] = fuzz.trapmf(Water_Level.universe, [2,4,6,8])
        Water_Level['alto'] = fuzz.trapmf(Water_Level.universe, [6,8,10,14])
        #Criando as funções de pertinencia de saida que é o tempo de duração da agua
        DuracaoAgua['Curto'] = fuzz.trapmf(DuracaoAgua.universe, [0,0,40,60])
        DuracaoAgua['Medio'] = fuzz.trapmf(DuracaoAgua.universe, [30,60,100,120])
        DuracaoAgua['Longo'] = fuzz.trapmf(DuracaoAgua.universe, [90,120,160,180])
        #Criando as regras para o tempo de duração da agua
        Regra1 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Gelada'] & Water_Level['baixo'],DuracaoAgua['Curto'])
        Regra2 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Gelada'] & Water_Level['neutro'],DuracaoAgua['Curto'])
        Regra3 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Gelada'] & Water_Level['alto'],DuracaoAgua['Curto'])
        Regra4 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Amena'] & Water_Level['baixo'],DuracaoAgua['Curto'])
        Regra5 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Amena'] & Water_Level['neutro'],DuracaoAgua['Curto'])
        Regra6 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Amena'] & Water_Level['alto'],DuracaoAgua['Curto'])
        Regra7 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Quente'] & Water_Level['baixo'],DuracaoAgua['Curto'])
        Regra8 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Quente'] & Water_Level['neutro'],DuracaoAgua['Curto'])
        Regra9 = ctrl.Rule(Soil_Moisture['Molhada'] & Soil_Temperature['Quente'] & Water_Level['alto'],DuracaoAgua['Medio'])
        Regra10 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Amena'] & Water_Level['baixo'],DuracaoAgua['Curto'])
        Regra11 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Amena'] & Water_Level['neutro'],DuracaoAgua['Medio'])
        Regra12 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Amena'] & Water_Level['alto'],DuracaoAgua['Medio'])
        Regra13 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Gelada'] & Water_Level['baixo'],DuracaoAgua['Curto'])
        Regra14 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Gelada'] & Water_Level['neutro'],DuracaoAgua['Medio'])
        Regra15 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Gelada'] & Water_Level['alto'],DuracaoAgua['Medio'])
        Regra16 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Quente'] & Water_Level['baixo'],DuracaoAgua['Medio'])
        Regra17 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Quente'] & Water_Level['neutro'],DuracaoAgua['Medio'])
        Regra18 = ctrl.Rule(Soil_Moisture['Normal'] & Soil_Temperature['Quente'] & Water_Level['alto'],DuracaoAgua['Medio'])
        Regra19 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Gelada'] & Water_Level['baixo'],DuracaoAgua['Medio'])
        Regra20 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Gelada'] & Water_Level['neutro'],DuracaoAgua['Medio'])
        Regra21 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Gelada'] & Water_Level['alto'],DuracaoAgua['Medio'])
        Regra22 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Amena'] & Water_Level['baixo'],DuracaoAgua['Medio'])
        Regra23 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Amena'] & Water_Level['neutro'],DuracaoAgua['Longo'])
        Regra24 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Amena'] & Water_Level['alto'],DuracaoAgua['Longo'])
        Regra25 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Quente'] & Water_Level['baixo'],DuracaoAgua['Longo'])
        Regra26 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Quente'] & Water_Level['neutro'],DuracaoAgua['Longo'])
        Regra27 = ctrl.Rule(Soil_Moisture['Seca'] & Soil_Temperature['Quente'] & Water_Level['alto'],DuracaoAgua['Longo'])
        #sistema fuzzy e Simulação
        DuracaoAgua_ctrl = ctrl.ControlSystem([Regra1,Regra2,Regra3,Regra4,Regra5,Regra6,Regra7,Regra8,Regra9,Regra10,Regra11,Regra12,Regra13,Regra14,Regra15,Regra16,Regra17,Regra18,Regra19,Regra20,Regra21,Regra22,Regra23,Regra24,Regra25,Regra26,Regra27])
        DuracaoAgua_simulador = ctrl.ControlSystemSimulation(DuracaoAgua_ctrl)
    
        #Entrada da temperatura
        while True:
          temp = simulationFinal.soil_sensor_Temperature.setTemperature
          # temp = simulationFinal.soil_sensor_Temperature1.setTemperature
          if temp < 0 or temp > 40:
            print("A temperatura adeve estar no intervalo [0,40]")
            continue
          DuracaoAgua_simulador.input['Soil_Temperature'] = temp
          break
        
        #Entrada da Umidade
        while True:
          ur = simulationFinal.sensor_Humidity.setHumidity
          # ur = simulationFinal.sensor_Humidity1.setHumidity
          if ur < 0 or ur > 60:
            print("A umidade deve estar no intervalo [0,60]")
            continue
          DuracaoAgua_simulador.input['Soil_Moisture'] = ur
          break
        
        #Entrada do Water_Level
        while True:
          Water_Level = simulationFinal.sensor_Water_Level.setWaterLevel
          # Water_Level = simulationFinal.sensor_Water_Level1.setWaterLevel
          if Water_Level < 0 or Water_Level > 14:
            print("A umidade deve estar no intervalo [0,14]")
            continue
          DuracaoAgua_simulador.input['Water_Level'] = Water_Level
          break

        while True:
          #Computando o resultado (Inferencia fuzzy + Defuzzificação)
          DuracaoAgua_simulador.compute()
          print(f"A duração da agua calculada foi de {DuracaoAgua_simulador.output['DuracaoAgua']}")
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
    text_dados = Label(janela, text=simulationFinal.sensor_Humidity.setHumidity)
    text_dados2 = Label(janela, text=simulationFinal.soil_sensor_Temperature.setTemperature)
    text_dados3 = Label(janela, text=simulationFinal.sensor_Water_Level.setWaterLevel)
  
    text_dados.grid(column=0,row=1)
    text_dados2.grid(column=0,row=2)
    text_dados3.grid(column=0,row=3)
  
    janela.after(400,visualizacao)
    janela.mainloop()


threading.Thread(target=visualizacao).start()
threading.Thread(target=FuzzyLogic).start()