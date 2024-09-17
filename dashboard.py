import pandas as pd
import pywedge as pw
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Machine Downtime.csv')

mc = pw.Pywedge_Charts(df, c=None, y="Coolant_Pressure(bar)")
charts = mc.make_charts()

# Render the first chart using matplotlib
plt.imshow(charts[0])
plt.show()
