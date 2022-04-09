# 5GPy

Dependencies:

5GPy runs with Python 3.6.9.

5GPy uses Networkx Python module to implement graphs. Install it using the following command:

-pip install networkx

All simulation configurations must be put at:

-configurations.xml

The initialization of a simulation is done at:

-simulation.py

To run a simulation, execute:

-python3 simulation.py

The classes representing the network topology elements are within:

-network.py

Utility methods can be found and must be placed at:

-utiliy.py

Please, when using 5GPy in your paper, thesis or dissertation, it is mandatory to cite the following reference:

@article{tinini20195gpy,
title={5GPy: A SimPy-based simulator for performance evaluations in 5G hybrid Cloud-Fog RAN architectures},
author={Tinini, Rodrigo Izidoro and dos Santos, Matias Rom{\'a}rio Pinheiro and Figueiredo, Gustavo Bittencourt and Batista, Daniel Mac{\^e}do},
journal={Simulation Modelling Practice and Theory},
pages={102030},
year={2019},
publisher={Elsevier}
}

If you have any questions, please contact me at: tinini at fei dot edu dot br

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
