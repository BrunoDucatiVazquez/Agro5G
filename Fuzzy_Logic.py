import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import mysql.connector

#contectando com o banco local
banco = mysql.connector.connect(
  host='localhost',
  database='tcc',
  user='root',
  password=''
)


#Criando as variaveis do problema
UmidadeSolo  = ctrl.Antecedent(np.arange(0,60,1),'UmidadeSolo')
temperaturaSolo  = ctrl.Antecedent(np.arange(0,40,1),'temperaturaSolo')
NivelAgua = ctrl.Antecedent(np.arange(0,6,1),'NivelAgua')
#Como a duração da agua é a saida devemos colocar o metodo Consequent
DuracaoAgua = ctrl.Consequent(np.arange(0,180,1),'DuracaoAgua')

#Criando as funções de pertinencia para a umidade do solo
UmidadeSolo['Molhada'] = fuzz.trapmf(UmidadeSolo.universe, [0,0,10,20])
UmidadeSolo['Normal'] = fuzz.trapmf(UmidadeSolo.universe, [10,20,30,40])
UmidadeSolo['Seca'] = fuzz.trapmf(UmidadeSolo.universe, [30,40,50,60])

#Criando as funções de pertinencia para a temperatura do solo
temperaturaSolo['Gelada'] = fuzz.trapmf(temperaturaSolo.universe, [0,0,15,20])
temperaturaSolo['Amena'] = fuzz.trapmf(temperaturaSolo.universe, [15,20,25,30])
temperaturaSolo['Quente'] = fuzz.trapmf(temperaturaSolo.universe, [25,30,35,40])

#Criando as funções de pertinencia para a o Nivel da Agua
NivelAgua['Baixa'] = fuzz.trapmf(NivelAgua.universe, [0,0,2,4])
NivelAgua['Normal'] = fuzz.trapmf(NivelAgua.universe, [2,4,6,8])
NivelAgua['Alta'] = fuzz.trapmf(NivelAgua.universe, [6,8,10,12])

#Criando as funções de pertinencia de saida que é o tempo de duração da aguaaaa
DuracaoAgua['Curto'] = fuzz.trapmf(DuracaoAgua.universe, [0,0,40,60])
DuracaoAgua['Medio'] = fuzz.trapmf(DuracaoAgua.universe, [30,60,100,120])
DuracaoAgua['Longo'] = fuzz.trapmf(DuracaoAgua.universe, [90,120,160,180])
#Criando as regras para o tempo de duração da agua
Regra1 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Gelada'] & NivelAgua['Baixa'],DuracaoAgua['Curto'])
Regra2 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Gelada'] & NivelAgua['Normal'],DuracaoAgua['Curto'])
Regra3 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Gelada'] & NivelAgua['Alta'],DuracaoAgua['Curto'])
Regra4 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Amena'] & NivelAgua['Baixa'],DuracaoAgua['Curto'])
Regra5 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Amena'] & NivelAgua['Normal'],DuracaoAgua['Curto'])
Regra6 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Amena'] & NivelAgua['Alta'],DuracaoAgua['Curto'])
Regra7 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Quente'] & NivelAgua['Baixa'],DuracaoAgua['Curto'])
Regra8 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Quente'] & NivelAgua['Normal'],DuracaoAgua['Curto'])
Regra9 = ctrl.Rule(UmidadeSolo['Molhada'] & temperaturaSolo['Quente'] & NivelAgua['Alta'],DuracaoAgua['Medio'])
Regra10 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Amena'] & NivelAgua['Baixa'],DuracaoAgua['Curto'])
Regra11 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Amena'] & NivelAgua['Normal'],DuracaoAgua['Medio'])
Regra12 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Amena'] & NivelAgua['Alta'],DuracaoAgua['Medio'])
Regra13 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Gelada'] & NivelAgua['Baixa'],DuracaoAgua['Curto'])
Regra14 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Gelada'] & NivelAgua['Normal'],DuracaoAgua['Medio'])
Regra15 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Gelada'] & NivelAgua['Alta'],DuracaoAgua['Medio'])
Regra16 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Quente'] & NivelAgua['Baixa'],DuracaoAgua['Medio'])
Regra17 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Quente'] & NivelAgua['Normal'],DuracaoAgua['Medio'])
Regra18 = ctrl.Rule(UmidadeSolo['Normal'] & temperaturaSolo['Quente'] & NivelAgua['Alta'],DuracaoAgua['Medio'])
Regra19 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Gelada'] & NivelAgua['Baixa'],DuracaoAgua['Medio'])
Regra20 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Gelada'] & NivelAgua['Normal'],DuracaoAgua['Medio'])
Regra21 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Gelada'] & NivelAgua['Alta'],DuracaoAgua['Medio'])
Regra22 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Amena'] & NivelAgua['Baixa'],DuracaoAgua['Medio'])
Regra23 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Amena'] & NivelAgua['Normal'],DuracaoAgua['Longo'])
Regra24 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Amena'] & NivelAgua['Alta'],DuracaoAgua['Longo'])
Regra25 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Quente'] & NivelAgua['Baixa'],DuracaoAgua['Longo'])
Regra26 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Quente'] & NivelAgua['Normal'],DuracaoAgua['Longo'])
Regra27 = ctrl.Rule(UmidadeSolo['Seca'] & temperaturaSolo['Quente'] & NivelAgua['Alta'],DuracaoAgua['Longo'])

#sistema fuzzy e Simulação
DuracaoAgua_ctrl = ctrl.ControlSystem([Regra1,Regra2,Regra3,Regra4,Regra5,Regra6,Regra7,Regra8,Regra9,Regra10,Regra11,Regra12,Regra13,Regra14,Regra15,Regra16,Regra17,Regra18,Regra19,Regra20,Regra21,Regra22,Regra23,Regra24,Regra25,Regra26,Regra27])
DuracaoAgua_simulador = ctrl.ControlSystemSimulation(DuracaoAgua_ctrl)



#Entrada da temperatura
while True:
  temp = float(input("Digite a Temperatura em graus celsius:"))
  if temp < 0 or temp > 40:
    print("A temperatura adeve estar no intervalo [0,40]")
    continue
  DuracaoAgua_simulador.input['temperaturaSolo'] = temp
  break

#Entrada da Umidade
while True:
  ur = float(input("Digite a Umidade em cbar:"))
  if ur < 0 or ur > 60:
    print("A umidade deve estar no intervalo [0,60]")
    continue
  DuracaoAgua_simulador.input['UmidadeSolo'] = ur
  break

#Entrada do nivel da agua
while True:
  na = float(input("Digite o nivel da agua em metros:"))
  if na < 0 or na > 6:
    print("A umidade deve estar no intervalo [0,6]")
    continue
  DuracaoAgua_simulador.input['NivelAgua'] = na
  break

#Colocando os dados no banco
cursor = banco.cursor()
comando_insercao = "INSERT INTO planta (temperatura,umidade,nivel_agua) VALUES (%s,%s,%s)"
dados = (str(temp),str(ur),str(na))
cursor.execute(comando_insercao,dados)
banco.commit()



#Computando o resultado (Inferencia fuzzy + Defuzzificação)
DuracaoAgua_simulador.compute()
print(f"A duração da agua calculada foi de {DuracaoAgua_simulador.output['DuracaoAgua']}")


"""

Tabela da planta que sera utillizada

Create table planta(
  IDPLANTA int not null auto_increment,
  temperatura INT not null,
  umidade INT not null,
  nivel_agua INT not null,
  primary key (IDPLANTA)
);
"""