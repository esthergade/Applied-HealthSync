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
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


#defining lists that will be used later
bloodpresure_sys_list = []
bloodpresure_dia_list = []
heartrate_list = []
date_list = []


try:
    df = pd.read_csv('Health_app_folder/csv_data/health_data.csv')
except FileNotFoundError:
    df = pd.DataFrame({'systolic': bloodpresure_sys_list, 'diastolic': bloodpresure_dia_list, 'Heartrate': heartrate_list, 'date': date_list})




# defining a function that gives us the day today
today = date.today()
today = today.strftime("%d/%m/%y")

class MyPopup(Popup):
    def __init__(self, **kwargs):
        super(MyPopup, self).__init__(**kwargs)
        self.title = 'Blood pressure status'
        self.size_hint = (None, None)
        self.size = (400, 200)

        df4 = pd.read_csv('Health_app_folder/csv_data/health_data.csv')
        #take the last row from the dataframe
        df4 = df4.tail(1)
        #defining the variables blood_pressure_sys and blood_pressure_dia
        blood_pressure_sys = df4['systolic'].values[0]
        blood_pressure_dia = df4['diastolic'].values[0]


        #defining the content of the popup
        if blood_pressure_sys <= 120 and blood_pressure_dia <= 80:
            self.content = Label(text='Blood pressure is optimal')
        elif blood_pressure_sys > 129 or blood_pressure_dia > 89:
            if blood_pressure_sys >= 180 or blood_pressure_dia >= 120:
                self.content = Label(text="Blood pressure in hypertensive emergency - seek medical care immediately")
                self.size = (550, 200)
            elif blood_pressure_sys >= 140 or blood_pressure_dia >= 90:
                self.content = Label(text='Stage 2 hypertension')
            elif blood_pressure_sys >= 130 or blood_pressure_dia >= 80:
                self.content = Label(text='Stage 1 hypertension')
        else:
            self.content = Label(text='Blood pressure is elevated') 

            


#defining the child app.
class ChildApp(GridLayout): 
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text = 'Enter systolic \nblood pressure (mm Hg)')) #adding a text input for systolic
        self.s_bloodpressure_sys = TextInput() #using the TextIput function earlier imported
        self.add_widget(self.s_bloodpressure_sys) #adding it as a widget

        self.add_widget(Label(text = 'Enter diastolic \nblood pressure (mm Hg)')) #doing the same for diastolic
        self.s_bloodpressure_dia = TextInput()
        self.add_widget(self.s_bloodpressure_dia)

        self.add_widget(Label(text = 'Enter heart rate')) #doing the same for heartrate
        self.s_heartrate = TextInput()
        self.add_widget(self.s_heartrate)

        self.press = Button(text= "", background_normal='Buttons/buttons_report.png') #adding a button for reporting the typed in data
        self.press.bind(on_press = self.report) #we have not defined yet what this button does
        self.add_widget(self.press)

        self.press = Button(text= "", background_normal='Buttons/buttons_graph.png')#adding a button for plotting the reported data
        self.press.bind(on_press = self.see_health) #we have not defined yet what this button does
        self.add_widget(self.press)

    # Here we define what happens when we click on the "Report Health Data button"
    def report(self, instance):
        #just printing to make sure it works
        print("Your blood presure is "+self.s_bloodpressure_sys.text)
        #converting from text to integer
        blood_pressure_sys = int(self.s_bloodpressure_sys.text)
        blood_pressure_dia = int(self.s_bloodpressure_dia.text)
        heartrate = int(self.s_heartrate.text)
        #appending to the lists so we can make a plot

        bloodpresure_sys_list.append(blood_pressure_sys)
        bloodpresure_dia_list.append(blood_pressure_dia)
        heartrate_list.append(heartrate)
        date_list.append(today) #i defined "today" ealier in the code


        dict2 = {'systolic': bloodpresure_sys_list, 'diastolic': bloodpresure_dia_list, 'Heartrate': heartrate_list, 'date': date_list}
        df2 = pd.DataFrame(dict2)
        df3 = pd.concat([df, df2])
        print(df3)


        # creating conditionals for pop ups
        if blood_pressure_sys <= 120 and blood_pressure_dia <= 80:
            print("optimal blood pressure")
        elif blood_pressure_sys > 120 and blood_pressure_sys <= 129 and blood_pressure_dia >= 80:
            print("elevated blood pressure")
        elif blood_pressure_sys >= 140 or blood_pressure_dia >= 90:
            print ("stage 2 hypertension")
        elif blood_pressure_sys > 130 and blood_pressure_sys <= 139 or blood_pressure_dia > 80 and blood_pressure_dia <= 89:
            print("stage 1 hypertension")
        elif blood_pressure_sys >= 180 or blood_pressure_dia >= 120:
            print("blood pressure in hypertensive emergency - seek medical care immediately")
        #saving a csv
        df3.to_csv('Health_app_folder/csv_data/health_data.csv')

        #opening the popup
        popup = MyPopup()
        popup.open()

# if you click on the see health data button, then it will show a plot of the reported health data.
    def see_health(self, instance):
        df3 = pd.read_csv('Health_app_folder/csv_data/health_data.csv')
        plt.plot(df3['date'], df3['systolic'], color ='r', label = "systolic")
        plt.plot(df3['date'], df3['diastolic'], color ='g', label = "diastolic")
        plt.legend()
        plt.show()



#defining the parent app
class ParentApp(App):
    def build(self):
        return ChildApp()

#if you run the app then run it?
if __name__ == "__main__":
    ParentApp().run()