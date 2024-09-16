import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

data=pd.read_csv("Machine Downtime.csv")
print(data.head())

print(data.describe())

data['Hydraulic_Pressure(bar)'].value_counts().plot(kind='bar')
plt.title('Hydraulic_Pressure(bar)')
plt.xlabel('hydraulic')
sns.despine 
plt.show()

plt.scatter(data['Coolant_Pressure(bar)'] , data['Air_System_Pressure(bar)'])
plt.title("Coolant_Pressure(bar) vs Air_System_Pressure(bar)")
plt.show()

plt.title('Coolant_Temperature vs Hydraulic_Oil_Temperature vs Spindle_Bearing_Temperature')
plt.scatter((data['Coolant_Temperature']+data['Hydraulic_Oil_Temperature']),data['Spindle_Bearing_Temperature'])
plt.show()
plt.title("Spindle_Vibration")
plt.scatter(data.Spindle_Vibration,data.Tool_Vibration)
plt.show()

plt.title('Torque vs Voltage  vs Cutting(kN)')
plt.scatter((data['Torque']+data['Voltage']),data['Cutting(kN)'])
plt.show()


ax = data.plot(x='Spindle_Speed',kind='bar')
plt.show()

