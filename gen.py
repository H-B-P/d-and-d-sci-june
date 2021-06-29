import numpy as np
import pandas as pd
import random
import math

def gen_heteropneum():
 amt = 142*np.random.poisson(np.random.poisson(np.random.poisson(14.9)))
 if amt>0:
  return amt
 else:
  return gen_heteropneum()




def pick_pilot(enemyStr):
 detected = round(enemyStr, -2)
 if detected>=2500:
  return "Maria N."
 if detected>=1200:
  return random.choice(["Maria N.", "Janelle K."])
 return random.choice(["Flint S.", "Amir B.", "Corazon V.", "Will C.", "Maria N.", "Maria N.", "Janelle K.", "Janelle K.", "Janelle K.", "Janelle K."])




def gen_addl_floordays():
 return 1+np.random.poisson(np.random.poisson(2.1))




def gen_alpha_res(days, enemyStr, teeming):
 return 3444.4 + (days>502)*511.1 + 28.5*np.random.poisson(10.2)

def gen_beta_res(days, enemyStr, teeming):
 return 2401.1 + 103.4*np.random.poisson(3.9)

def gen_gamma_res(days, enemyStr, teeming):
 return 662.6 + enemyStr*0.66*np.random.poisson(1.1)

def gen_delta_res(days, enemyStr, teeming):
 return enemyStr*0.32 + 3253.0 + 88.2*np.random.poisson(19.2)

def gen_epsilon_res(days, enemyStr, teeming):
 simpl = enemyStr/1000.0
 amt = 0.46 - simpl*1.12 + simpl*simpl*0.93 - simpl*simpl*simpl*0.14
 return amt*1000.0

def gen_zeta_res(days, enemyStr, teeming):
 if random.random()<0.78:
  if teeming:
   return 7531.1
  else:
   return 2157.1
 else:
  return 0

def gen_eta_res(days, enemyStr, teeming):
 return 943.4+(days>256)*481.5+(days>303)*703.3+(days>502)*890.8-(days>748)*608.1




resFuncLookup={
"alpha":gen_alpha_res,
"beta":gen_beta_res,
"gamma":gen_gamma_res,
"delta":gen_delta_res,
"epsilon":gen_epsilon_res,
"zeta":gen_zeta_res,
"eta":gen_eta_res}

resOfChoice={
"Maria N.":"delta",
"Janelle K.":"beta",
"Flint S.":"alpha",
"Amir B.":"alpha",
"Corazon V.":"alpha",
"Will C.":"beta"}

multipliers={
"Maria N.":{"alpha":1.0,"beta":1.0,"gamma":1.0,"delta":1.0,"epsilon":1.0, "zeta":1.0, "eta":1.0},
"Janelle K.":{"alpha":0.48, "beta":0.98, "gamma":1.34, "delta":0.24, "epsilon":0.79, "zeta":0.43, "eta":0.45},
"Flint S.":{"alpha":0.42, "beta":0.32, "gamma":0.36, "delta":0.32, "epsilon":1.23, "zeta":0.39, "eta":1.08},
"Amir B.":{"alpha":0.50, "beta":0.72, "gamma":0.42, "delta":0.34, "epsilon":0.78, "zeta":0.41, "eta":0.23},
"Corazon V.":{"alpha":0.59, "beta":0.11, "gamma":0.58, "delta":0.16, "epsilon":0.35, "zeta":0.92, "eta":0.12},
"Will C.":{"alpha":0.23, "beta":0.55, "gamma":0.14, "delta":0.21, "epsilon":2.11, "zeta":0.12, "eta":0.95},
}

def convert_to_kCept(cept, decis):
 return str(round(cept, -decis)/1000)+" kCept"

dictForDf = {"Floorday":[],"Heteropneum Strength":[], "Pilot":[], "Pilot Strength (alpha)":[], "Pilot Strength (beta)":[], "Pilot Strength (gamma)":[], "Pilot Strength (delta)":[], "Pilot Strength (epsilon)":[], "Pilot Strength (zeta)":[],"Pilot Strength (eta)":[]}

df = pd.DataFrame(dictForDf)

df = df[["Floorday","Heteropneum Strength", "Pilot", "Pilot Strength (alpha)", "Pilot Strength (beta)", "Pilot Strength (gamma)", "Pilot Strength (delta)", "Pilot Strength (epsilon)", "Pilot Strength (zeta)", "Pilot Strength (eta)"]]

floorday=0
floordays=[]

random.seed(2) #I admit it: I fiddled with the seeds until no pilots died and it gave me a puzzle I considered solvable.
np.random.seed(2)

def add_new_stuff_to_df(df, floorday, eStr, teeming):
 pilot = pick_pilot(eStr)
 primaryRes = resOfChoice[pilot]
 primaryResFunc = resFuncLookup[primaryRes]
 pilotStr = multipliers[pilot][primaryRes]*primaryResFunc(floorday, eStr, teeming)
 if pilotStr<eStr:
  print(pilot+ " DIED! (floorday " + str(floorday)+")")
  assert(False)
 if pilotStr>(eStr*2):
  newRow = {"Floorday": int(floorday), "Heteropneum Strength":convert_to_kCept(eStr, 1), "Pilot":pilot}
  for res in resFuncLookup:
   newRow["Pilot Strength ("+res+")"] = convert_to_kCept(multipliers[pilot][res]*resFuncLookup[res](floorday, eStr, teeming), 1)
  newRow["Pilot Strength ("+primaryRes+")"] = convert_to_kCept(pilotStr, 1)
 else:
  newRow = {"Floorday": int(floorday), "Heteropneum Strength":convert_to_kCept(eStr, 2), "Pilot":pilot}
  for res in resFuncLookup:
   newRow["Pilot Strength ("+res+")"] = "Unknown"
  newRow["Pilot Strength ("+primaryRes+")"] = convert_to_kCept(pilotStr, 2)
 df=df.append(newRow, ignore_index=True)
 return df

for i in range(262):
 floorday += gen_addl_floordays()
 floordays.append(floorday)
 eStr = gen_heteropneum()
 df = add_new_stuff_to_df(df, floorday, eStr, False)

for floorday, eStr in [[107,2441],[150,3300], [212,301],[213,1188],[323, 205],[380,4922], [389,3245], [463,1387],[464,1402], [520,5109], [529,4546], [630, 504], [680, 790], [771,1890],[772,53],[800,2232], [803,2944], [813,5504], [814,3141]]:
 while floorday in floordays:
  floorday+=1
 floordays.append(floorday)
 df = add_new_stuff_to_df(df, floorday, eStr, True)

print(df)

df = df.sort_values(by='Floorday')

#print(df)

df.to_csv("dset.csv")
