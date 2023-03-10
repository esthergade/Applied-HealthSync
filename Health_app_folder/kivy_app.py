#kivy app

import kivy
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from datetime import datetime

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


bloodpresure_sys_list = []
bloodpresure_dia_list = []
date_list = []
test_dates5 = ['03/12/22', '01/01/23', '01/05/23', '15/06/23', '1/07/23']

test_dates5 = pd.to_datetime(test_dates5, format="%d/%m/%y")



today = date.today()
today = today.strftime("%d/%m/%y")


class ChildApp(GridLayout): 
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text = 'Enter systolic blood pressure (mm Hg)'))
        self.s_bloodpressure_sys = TextInput()
        self.add_widget(self.s_bloodpressure_sys)

        self.add_widget(Label(text = 'Enter diastolic blood pressure (mm Hg)'))
        self.s_bloodpressure_dia = TextInput()
        self.add_widget(self.s_bloodpressure_dia)

        self.add_widget(Label(text = 'Enter heart rate'))
        self.s_heartrate = TextInput()
        self.add_widget(self.s_heartrate)

        self.press = Button(text= "Report Health data")
        self.press.bind(on_press = self.report)
        self.add_widget(self.press)

        self.press = Button(text= "See Health data")
        self.press.bind(on_press = self.see_health)
        self.add_widget(self.press)


    def report(self, instance):
        print("Your blood presure is "+self.s_bloodpressure_sys.text)
        blood_pressure_sys = int(self.s_bloodpressure_sys.text)
        blood_pressure_dia = int(self.s_bloodpressure_dia.text)

        bloodpresure_sys_list.append(blood_pressure_sys)
        bloodpresure_dia_list.append(blood_pressure_dia)

        date_list.append(today)
        print(bloodpresure_sys_list, bloodpresure_dia_list, test_dates5)
        
        if blood_pressure_sys > 120:
            print("Go to your doctor")
        


    def see_health(self, instance):
        plt.plot(test_dates5, bloodpresure_sys_list, color ='r', label = "systolic")
        plt.plot(test_dates5, bloodpresure_dia_list, color ='g', label = "diastolic")
        plt.legend()
        plt.show()



class ParentApp(App):
    def build(self):
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()

