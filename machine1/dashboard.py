import pandas as pd 
import pywedge as pw
from IPython.display import display
df=pd.read_csv("Machine Downtime.csv")
print(df.head())
print(df.columns)
# Load your dataset
df = pd.read_csv('Machine Downtime.csv')

mc = pw.Pywedge_Charts(df, c=None, y="Coolant_Pressure(bar)")
charts = mc.make_charts()
print(charts)