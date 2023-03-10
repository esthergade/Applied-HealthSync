#kivy app

#importing relevant libraries
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

#defining lists that will be used later
bloodpresure_sys_list = []
bloodpresure_dia_list = []
date_list = []
test_dates5 = ['03/12/22', '01/01/23', '01/05/23', '15/06/23', '1/07/23'] #this is a test list

test_dates5 = pd.to_datetime(test_dates5, format="%d/%m/%y") #converting to actual dates instead of text


# defining a function that gives us the day today
today = date.today()
today = today.strftime("%d/%m/%y")

#defining the child app.
class ChildApp(GridLayout): 
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2 #two collumns in the app.

        self.add_widget(Label(text = 'Enter systolic blood pressure (mm Hg)')) #adding a text input for systolic
        self.s_bloodpressure_sys = TextInput() #using the TextIput function earlier imported
        self.add_widget(self.s_bloodpressure_sys) #adding it as a widget

        self.add_widget(Label(text = 'Enter diastolic blood pressure (mm Hg)')) #doing the same for diastolic
        self.s_bloodpressure_dia = TextInput()
        self.add_widget(self.s_bloodpressure_dia)

        self.add_widget(Label(text = 'Enter heart rate')) #doing the same for heartrate
        self.s_heartrate = TextInput()
        self.add_widget(self.s_heartrate)

        self.press = Button(text= "Report Health data") #adding a button for reporting the typed in data
        self.press.bind(on_press = self.report) #we have not defined yet what this button does
        self.add_widget(self.press)

        self.press = Button(text= "See Health data")#adding a button for plotting the reported data
        self.press.bind(on_press = self.see_health) #we have not defined yet what this button does
        self.add_widget(self.press)

    # Here we define what happens when we click on the "Report Health Data button"
    def report(self, instance):
        #just printing to make sure it works
        print("Your blood presure is "+self.s_bloodpressure_sys.text)
        #converting from text to integer
        blood_pressure_sys = int(self.s_bloodpressure_sys.text)
        blood_pressure_dia = int(self.s_bloodpressure_dia.text)
        #appending to the lists so we can make a plot
        bloodpresure_sys_list.append(blood_pressure_sys)
        bloodpresure_dia_list.append(blood_pressure_dia)
        date_list.append(today) #i defined "today" ealier in the code
        #making a datafram so we can save a csv-file.
        df = pd.DataFrame(bloodpresure_sys_list, bloodpresure_dia_list, date_list)

        #printing to see if it works.
        print(bloodpresure_sys_list, bloodpresure_dia_list, test_dates5)
        
        # A lot of if and elif statements
        if blood_pressure_sys > 120:
            print("Go to your doctor")
        

# if you click on the see health data button, then it will show a plot of the reported health data.
    def see_health(self, instance):
        plt.plot(test_dates5, bloodpresure_sys_list, color ='r', label = "systolic")
        plt.plot(test_dates5, bloodpresure_dia_list, color ='g', label = "diastolic")
        plt.legend()
        plt.show()


#defining the parent app
class ParentApp(App):
    def build(self):
        return ChildApp()

#if you run the app then run it?
if __name__ == "__main__":
    ParentApp().run()

