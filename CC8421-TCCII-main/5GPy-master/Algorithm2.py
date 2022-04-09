
import simulationFinal
from tkinter import *

class Algorithm2:
  def run():
    pass

class IrrigationIoT(Algorithm2,object):
  def run():
    #Entrada da Umidade
        while True:
          threshouldValue = 100 # value of amount irrigation in ms
          ur = simulationFinal.sensor_Humidity.setHumidity
          if  ur > 60 and ur < 100:
            print("The humidity was{}% , and the amount of irrigation is {} ".format(ur,threshouldValue))
          else:
            print("The humidity was{}%, and don't need the irrigation".format(ur))
          break


    



