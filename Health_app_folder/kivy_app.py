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


bloodpresure_list = []
date_list = []
test_dates5 = ['03/12/22', '01/01/23', '01/05/23', '15/06/23', '1/07/23']

test_dates5 = pd.to_datetime(test_dates5, format="%d/%m/%y")



today = date.today()
today = today.strftime("%d/%m/%y")


class ChildApp(GridLayout): 
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text = 'Enter blood pressure'))
        self.s_bloodpressure = TextInput()
        self.add_widget(self.s_bloodpressure)

        self.press = Button(text= "Report Health data")
        self.press.bind(on_press = self.report)
        self.add_widget(self.press)

        self.press = Button(text= "See Health data")
        self.press.bind(on_press = self.see_health)
        self.add_widget(self.press)


    def report(self, instance):
        print("Your blood presure is "+self.s_bloodpressure.text)
        blodd_pressure = int(self.s_bloodpressure.text)
        bloodpresure_list.append(blodd_pressure)
        date_list.append(today)
        print(bloodpresure_list, test_dates5)
        
        if blodd_pressure > 120:
            print("Go to your doctor")

    def see_health(self, instance):
        df = pd.DataFrame( bloodpresure_list, test_dates5)
        plt.plot(df)
        plt.show()

    

class ParentApp(App):
    def build(self):
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()

