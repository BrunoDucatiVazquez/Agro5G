import simulationFinal
import multiprocessing

import kivy  
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
  
# Create the App class
class kivyApplication(App):
      
    def build(self):
        b = BoxLayout(orientation ='vertical')
        # Adding the text input
        t = TextInput(font_size = 50,
                      size_hint_y = None,
                      height = 100)
        f = FloatLayout()
  
        # By this you are able to move the
        # Text on the screen to anywhere you want
        s = Scatter()
        text = Scatter()
        # text = Scatter()
        text_temperature = Label(text = "Valor da Temperatura",font_size = 50,pos = (250,300))
        temperature= Label(text =str(simulationFinal.soil_sensor_Temperature.setTemperature),font_size = 50, pos = (550,300))
        text_Humidity = Label(text = "Valor da umidade",font_size = 50,pos = (250,250))
        Humidity= Label(text =str(simulationFinal.sensor_Humidity.setHumidity),font_size = 50, pos = (550,250))
        text_WaterLevel = Label(text = "Valor do nivel da agua",font_size = 50,pos = (220,200))
        WaterLevel= Label(text =str(simulationFinal.sensor_Water_Level.setWaterLevel),font_size = 50, pos = (550,200))
        f.add_widget(s)
        f.add_widget(text)
        s.add_widget(temperature)
        text.add_widget(text_temperature)
        s.add_widget(Humidity)
        text.add_widget(text_Humidity)
        s.add_widget(WaterLevel)
        text.add_widget(text_WaterLevel)
        
        b.add_widget(f)
  
        #   manager.screen_thermo.ids.TempLabel.text = str(thetemp)
        return b
  


# Run the App
if __name__ == "__main__":
    kivyApplication().run()



