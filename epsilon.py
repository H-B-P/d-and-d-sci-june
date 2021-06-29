import pandas as pd
import numpy as np


from sklearn.linear_model import LinearRegression


df = pd.read_csv("old_dset.csv")

df=df.drop("Unnamed: 0", axis=1)

def desp(s):
 return s.split(" kCept")[0]

ceptyCols=["Heteropneum Strength", "Pilot Strength (alpha)", "Pilot Strength (beta)", "Pilot Strength (gamma)", "Pilot Strength (delta)", "Pilot Strength (epsilon)", "Pilot Strength (zeta)", "Pilot Strength (eta)"]
for c in ceptyCols:
 df[c] = df[c].apply(desp)

print(df)

pilot="Maria N."

sdf = df[df["Pilot"]==pilot]

sdf = sdf[sdf["Pilot Strength (epsilon)"]!="Unknown"]

print(sdf)

sdf["x1"]=sdf["Heteropneum Strength"].astype(float)
sdf["x2"]=sdf["x1"]*sdf["x1"]
sdf["x3"]=sdf["x1"]*sdf["x2"]

sdf["y"]=sdf["Pilot Strength (epsilon)"].astype(float)

X = sdf[["x1","x2","x3"]]
y = sdf["y"]

reg = LinearRegression().fit(X, y)

print(reg.coef_)

print(reg.intercept_)

def pred(x):
 return reg.predict(np.array([x,x**2, x**3]).reshape(1, -1))[0]

print(3.15, pred(3.15), 3.15/pred(3.15))
print(3.25, pred(3.25), 3.25/pred(3.25))
print("~")
print(0.57, pred(0.57))
print("~")
print(3.15, (0.21/0.1)*pred(3.15))
print(3.15, (0.205/0.105)*pred(3.15))
print(3.25, (0.21/0.1)*pred(3.25))
print(3.25, (0.205/0.105)*pred(3.25))
