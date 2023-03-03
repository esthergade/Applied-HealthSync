#kivy app

import kivy
import matplotlib.pyplot as plt
import pandas as pd

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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

    def report(self, instance):
        print("Your blood presure is "+self.s_bloodpressure.text)

class ParentApp(App):
    def build(self):
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()

