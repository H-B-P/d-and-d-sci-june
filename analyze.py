import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("old_dset.csv")

df=df.drop("Unnamed: 0", axis=1)

def desp(s):
 return s.split(" kCept")[0]

ceptyCols=["Heteropneum Strength", "Pilot Strength (alpha)", "Pilot Strength (beta)", "Pilot Strength (gamma)", "Pilot Strength (delta)", "Pilot Strength (epsilon)", "Pilot Strength (zeta)", "Pilot Strength (eta)"]
for c in ceptyCols:
 df[c] = df[c].apply(desp)

print(df)

for pilot in ["Flint S.", "Amir B.", "Corazon V.", "Will C."]:
 print(pilot)
 sdf = df[df["Pilot"]==pilot]
 print(sdf)

for comparator in ["Heteropneum Strength"]:#,"Floorday"]:
 for res in ["Pilot Strength (alpha)", "Pilot Strength (beta)", "Pilot Strength (gamma)", "Pilot Strength (delta)", "Pilot Strength (epsilon)", "Pilot Strength (zeta)", "Pilot Strength (eta)"]:
  for pilot in ["Maria N.", "Janelle K."]:#["Flint S.", "Amir B.", "Corazon V.", "Will C.", "Maria N.", "Janelle K."]:
   sdf = df[df["Pilot"]==pilot]
   #print(pilot, res, len(sdf))
   fig = go.Figure(data=go.Scatter(x=sdf[comparator], y=sdf[res], mode='markers'))
   fig.update_layout(title=pilot, xaxis_title=comparator, yaxis_title=res)
   fig.update_traces(marker={"opacity":0.6})
   #fig.update_layout(xaxis={"range":[0,100]})
   fig.show()

  
  


