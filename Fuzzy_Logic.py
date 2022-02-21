import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import mysql.connector

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
