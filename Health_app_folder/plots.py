#This is the plotting script

import matplotlib.pyplot as plt
import pandas as pd

date_time = ["2023-01-13","2023-01-29","2023-02-15","2023-02-26","2023-03-01"]
blood_pressure = [120, 110, 100, 120, 90]

date_time = pd.to_datetime(date_time)

df = pd.DataFrame(blood_pressure, date_time)

#plt.plot(df)
#plt.xlabel("Date Time")
#plt.ylabel("Blood Pressure")
#plt.savefig('Health_app_folder/plots/plot.png')

print("l")

