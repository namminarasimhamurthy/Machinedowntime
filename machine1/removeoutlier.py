import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpl_toolkits

data=pd.read_csv("Machine Downtime.csv")
print(data.head())

plt.title("before removing outlier")
data.boxplot(column='Hydraulic_Pressure(bar)')
plt.show()
upper_limit=data['Hydraulic_Pressure(bar)'].mean() + 3 * data["Hydraulic_Pressure(bar)"].std()
lower_limit=data['Hydraulic_Pressure(bar)'].mean() - 3 * data["Hydraulic_Pressure(bar)"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Hydraulic_Pressure(bar)'] > upper_limit) | (data['Hydraulic_Pressure(bar)']<lower_limit)]
print(a)
newdata = data.loc[(data['Hydraulic_Pressure(bar)'] < upper_limit) | (data['Hydraulic_Pressure(bar)'] > lower_limit)]
print("Before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removing outlier")
sns.boxplot(newdata['Hydraulic_Pressure(bar)'])
plt.show()
plt.savefig("Hydraulic_Pressure(bar).pdf")

plt.title("Before removing outlier")
data.boxplot(column='Coolant_Pressure(bar)')
plt.show()
upper_limit=data['Coolant_Pressure(bar)'].mean() + 3 * data["Coolant_Pressure(bar)"].std()
lower_limit=data['Coolant_Pressure(bar)'].mean() - 3 * data["Coolant_Pressure(bar)"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

b = data.loc[(data['Coolant_Pressure(bar)'] > upper_limit) | (data['Coolant_Pressure(bar)']<lower_limit)]
print(b)
newdata = data.loc[(data['Coolant_Pressure(bar)'] < upper_limit) | (data['Coolant_Pressure(bar)'] > lower_limit)]
print("Before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removing outlier")
sns.boxplot(newdata['Coolant_Pressure(bar)'])
plt.show()

plt.title("Before outlier")
data.boxplot(column='Air_System_Pressure(bar)')
plt.show()
upper_limit=data['Air_System_Pressure(bar)'].mean() + 3 * data["Air_System_Pressure(bar)"].std()
lower_limit=data['Air_System_Pressure(bar)'].mean() - 3 * data["Air_System_Pressure(bar)"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Air_System_Pressure(bar)'] > upper_limit) | (data['Air_System_Pressure(bar)']<lower_limit)]
print(a)
newdata = data.loc[(data['Air_System_Pressure(bar)'] < upper_limit) | (data['Air_System_Pressure(bar)'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After remove outlier")
sns.boxplot(newdata['Air_System_Pressure(bar)'])
plt.show()

plt.title("Before removeoutlier")
data.boxplot(column='Coolant_Temperature')
plt.show()
upper_limit=data['Coolant_Temperature'].mean() + 3 * data["Coolant_Temperature"].std()
lower_limit=data['Coolant_Temperature'].mean() - 3 * data["Coolant_Temperature"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Coolant_Temperature'] > upper_limit) | (data['Coolant_Temperature']<lower_limit)]
print(a)
newdata = data.loc[(data['Coolant_Temperature'] < upper_limit) | (data['Coolant_Temperature'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Coolant_Temperature'])
plt.show()

plt.title("Before removeoutlier")
data.boxplot(column='Hydraulic_Oil_Temperature')
plt.show()
upper_limit=data['Hydraulic_Oil_Temperature'].mean() + 3 * data["Hydraulic_Oil_Temperature"].std()
lower_limit=data['Hydraulic_Oil_Temperature'].mean() - 3 * data["Hydraulic_Oil_Temperature"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Hydraulic_Oil_Temperature'] > upper_limit) | (data['Hydraulic_Oil_Temperature']<lower_limit)]
print(a)
newdata = data.loc[(data['Hydraulic_Oil_Temperature'] < upper_limit) | (data['Hydraulic_Oil_Temperature'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Hydraulic_Oil_Temperature'])
plt.show()






plt.title("Before removeoutlier")
data.boxplot(column='Spindle_Bearing_Temperature')
plt.show()
upper_limit=data['Spindle_Bearing_Temperature'].mean() + 3 * data["Spindle_Bearing_Temperature"].std()
lower_limit=data['Spindle_Bearing_Temperature'].mean() - 3 * data["Spindle_Bearing_Temperature"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Spindle_Bearing_Temperature'] > upper_limit) | (data['Spindle_Bearing_Temperature']<lower_limit)]
print(a)
newdata = data.loc[(data['Spindle_Bearing_Temperature'] < upper_limit) | (data['Spindle_Bearing_Temperature'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Spindle_Bearing_Temperature'])
plt.show()


plt.title("Before removeoutlier")
data.boxplot(column='Spindle_Vibration')
plt.show()
upper_limit=data['Spindle_Vibration'].mean() + 3 * data["Spindle_Vibration"].std()
lower_limit=data['Spindle_Vibration'].mean() - 3 * data["Spindle_Vibration"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Spindle_Vibration'] > upper_limit) | (data['Spindle_Vibration']<lower_limit)]
print(a)
newdata = data.loc[(data['Spindle_Vibration'] < upper_limit) | (data['Spindle_Vibration'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Spindle_Vibration'])
plt.show()

plt.title("Before removeoutlier")
data.boxplot(column='Tool_Vibration')
plt.show()
upper_limit=data['Tool_Vibration'].mean() + 3 * data["Tool_Vibration"].std()
lower_limit=data['Tool_Vibration'].mean() - 3 * data["Tool_Vibration"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Tool_Vibration'] > upper_limit) | (data['Tool_Vibration']<lower_limit)]
print(a)
newdata = data.loc[(data['Tool_Vibration'] < upper_limit) | (data['Tool_Vibration'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Tool_Vibration'])
plt.show()


plt.title("Before removeoutlier")
data.boxplot(column='Spindle_Speed')
plt.show()
upper_limit=data['Spindle_Speed'].mean() + 3 * data["Spindle_Speed"].std()
lower_limit=data['Spindle_Speed'].mean() - 3 * data["Spindle_Speed"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Spindle_Speed'] > upper_limit) | (data['Spindle_Speed']<lower_limit)]
print(a)
newdata = data.loc[(data['Spindle_Speed'] < upper_limit) | (data['Spindle_Speed'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Spindle_Speed'])
plt.show()


plt.title("Before removeoutlier")
data.boxplot(column='Voltage')
plt.show()
upper_limit=data['Voltage'].mean() + 3 * data["Voltage"].std()
lower_limit=data['Voltage'].mean() - 3 * data["Voltage"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Voltage'] > upper_limit) | (data['Voltage']<lower_limit)]
print(a)
newdata = data.loc[(data['Voltage'] < upper_limit) | (data['Voltage'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Voltage'])
plt.show()

plt.title("Before removeoutlier")
data.boxplot(column='Torque')
plt.show()
upper_limit=data['Torque'].mean() + 3 * data["Torque"].std()
lower_limit=data['Torque'].mean() - 3 * data["Torque"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Torque'] > upper_limit) | (data['Torque']<lower_limit)]
print(a)
newdata = data.loc[(data['Torque'] < upper_limit) | (data['Torque'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Torque'])
plt.show()


plt.title("Before removeoutlier")
data.boxplot(column='Cutting(kN)')
plt.show()
upper_limit=data['Cutting(kN)'].mean() + 3 * data["Cutting(kN)"].std()
lower_limit=data['Cutting(kN)'].mean() - 3 * data["Cutting(kN)"].std()
print("upper_limit",upper_limit)
print("lower_limit",lower_limit)

a = data.loc[(data['Cutting(kN)'] > upper_limit) | (data['Cutting(kN)']<lower_limit)]
print(a)
newdata = data.loc[(data['Cutting(kN)'] < upper_limit) | (data['Cutting(kN)'] > lower_limit)]
print("before removing outlier",len(data))
print("after removing outlier",len(newdata))
print("outlier",len(data)-len(newdata))
plt.title("After removeoutlier")
sns.boxplot(newdata['Cutting(kN)'])
plt.show()


