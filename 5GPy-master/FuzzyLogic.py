
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import network as nt

#Criando as variaveis do problema
UmidadeSolo  = ctrl.Antecedent(np.arange(0,60,1),'UmidadeSolo')
temperaturaSolo  = ctrl.Antecedent(np.arange(0,40,1),'temperaturaSolo')
Ph = ctrl.Antecedent(np.arange(0,14,1),'Ph')
#Como a duração da agua é a saida devemos colocar o metodo Consequent
DuracaoAgua = ctrl.Consequent(np.arange(0,180,1),'DuracaoAgua')

#Criando as funções de pertinencia para a umidade do solo
UmidadeSolo['Molhada'] = fuzz.trapmf(UmidadeSolo.universe, [0,0,10,20])
UmidadeSolo['Normal'] = fuzz.trapmf(UmidadeSolo.universe, [10,20,30,40])
UmidadeSolo['Seca'] = fuzz.trapmf(UmidadeSolo.universe, [30,40,50,60])

#Criando as funções de pertinencia para a temperatura do solo
temperaturaSolo['Gelada'] = fuzz.trapmf(temperaturaSolo.universe, [0,1,15,20])
temperaturaSolo['Amena'] = fuzz.trapmf(temperaturaSolo.universe, [15,20,25,30])
temperaturaSolo['Quente'] = fuzz.trapmf(temperaturaSolo.universe, [25,30,35,40])

#Criando as funções de pertinencia para a o ph
Ph['acido'] = fuzz.trapmf(Ph.universe, [0,0,2,4])
Ph['neutro'] = fuzz.trapmf(Ph.universe, [2,4,6,8])
Ph['alcalino'] = fuzz.trapmf(Ph.universe, [6,8,10,14])

#Criando as funções de pertinencia de saida que é o tempo de duração da agua
DuracaoAgua['Curto'] = fuzz.trapmf(DuracaoAgua.universe, [0,0,40,60])
DuracaoAgua['Medio'] = fuzz.trapmf(DuracaoAgua.universe, [30,60,100,120])
DuracaoAgua['Longo'] = fuzz.trapmf(DuracaoAgua.universe, [90,120,160,180])

#Criando as regras para o tempo de duração da agua
Regra1 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Gelada'] & Ph['acido'],DuracaoAgua['Curto'])
Regra2 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Gelada'] & Ph['neutro'],DuracaoAgua['Curto'])
Regra3 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Gelada'] & Ph['alcalino'],DuracaoAgua['Curto'])
Regra4 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Amena'] & Ph['acido'],DuracaoAgua['Curto'])
Regra5 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Amena'] & Ph['neutro'],DuracaoAgua['Curto'])
Regra6 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Amena'] & Ph['alcalino'],DuracaoAgua['Curto'])
Regra7 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Quente'] & Ph['acido'],DuracaoAgua['Curto'])
Regra8 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Quente'] & Ph['neutro'],DuracaoAgua['Curto'])
Regra9 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Quente'] & Ph['alcalino'],DuracaoAgua['Medio'])
Regra10 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Amena'] & Ph['acido'],DuracaoAgua['Curto'])
Regra11 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Amena'] & Ph['neutro'],DuracaoAgua['Medio'])
Regra12 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Amena'] & Ph['alcalino'],DuracaoAgua['Medio'])
Regra13 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Gelada'] & Ph['acido'],DuracaoAgua['Curto'])
Regra14 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Gelada'] & Ph['neutro'],DuracaoAgua['Medio'])
Regra15 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Gelada'] & Ph['alcalino'],DuracaoAgua['Medio'])
Regra16 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Quente'] & Ph['acido'],DuracaoAgua['Medio'])
Regra17 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Quente'] & Ph['neutro'],DuracaoAgua['Medio'])
Regra18 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Quente'] & Ph['alcalino'],DuracaoAgua['Medio'])
Regra19 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Gelada'] & Ph['acido'],DuracaoAgua['Medio'])
Regra20 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Gelada'] & Ph['neutro'],DuracaoAgua['Medio'])
Regra21 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Gelada'] & Ph['alcalino'],DuracaoAgua['Medio'])
Regra22 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Amena'] & Ph['acido'],DuracaoAgua['Medio'])
Regra23 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Amena'] & Ph['neutro'],DuracaoAgua['Longo'])
Regra24 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Amena'] & Ph['alcalino'],DuracaoAgua['Longo'])
Regra25 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Quente'] & Ph['acido'],DuracaoAgua['Longo'])
Regra26 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Quente'] & Ph['neutro'],DuracaoAgua['Longo'])
Regra27 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Quente'] & Ph['alcalino'],DuracaoAgua['Longo'])
#sistema fuzzy e Simulação
DuracaoAgua_ctrl = ctrl.ControlSystem([Regra1,Regra2,Regra3,Regra4,Regra5,Regra6,Regra7,Regra8,Regra9,Regra10,Regra11,Regra12,Regra13,Regra14,Regra15,Regra16,Regra17,Regra18,Regra19,Regra20,Regra21,Regra22,Regra23,Regra24,Regra25,Regra26,Regra27])
DuracaoAgua_simulador = ctrl.ControlSystemSimulation(DuracaoAgua_ctrl)

#Entrada da temperatura
while True:
  temp = nt.sensor_Temperature.setTemperature
  if temp < 0 or temp > 40:
    print("A temperatura adeve estar no intervalo [0,40]")
    continue
  DuracaoAgua_simulador.input['temperaturaSolo'] = temp
  break


#Entrada da Umidade
while True:
  ur = nt.sensor_Humidity.setHumididty
  if ur < 0 or ur > 60:
    print("A umidade deve estar no intervalo [0,60]")
    continue
  DuracaoAgua_simulador.input['UmidadeSolo'] = ur
  break

#Entrada do ph
while True:
  ph = nt.sensor_Ph.setPh
  if ph < 0 or ph > 14:
    print("A umidade deve estar no intervalo [0,14]")
    continue
  DuracaoAgua_simulador.input['Ph'] = ph
  break

#Computando o resultado (Inferencia fuzzy + Defuzzificação)
DuracaoAgua_simulador.compute()
print(f"A duração da agua calculada foi de {DuracaoAgua_simulador.output['DuracaoAgua']}")

#visualizando as regiões
temperaturaSolo.view(sim=DuracaoAgua_simulador)
UmidadeSolo.view(sim=DuracaoAgua_simulador)
Ph.view(sim=DuracaoAgua_simulador)