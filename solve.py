import numpy as np
import pandas as pd
import random
import math

def gen_alpha_res(days, enemyStr, teeming):
 return 3444.4 + (days>502)*511.1 + 28.5*np.random.poisson(10.2)

def gen_beta_res(days, enemyStr, teeming):
 return 2401.1 + 103.4*np.random.poisson(3.9)#average of 2.8kCept approx

def gen_gamma_res(days, enemyStr, teeming):
 return 662.6 + enemyStr*0.66*np.random.poisson(1.1)


def gen_delta_res(days, enemyStr, teeming):
 return enemyStr*0.32 + 3253.0 + 88.2*np.random.poisson(19.2) #Essentially, you win, if you're Maria; and if not, you lose.

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

Earwax=3194#3151#3194

def give_me_prob(lamb, n):
 return math.pow(lamb ,n)*math.exp(-lamb)/math.factorial(n)


def alpha_res(mult, target):
 problose=0
 probsurv=0
 i=0
 while i<100:
  amt = (3444.4 + 511.1 + 28.5*i)*mult
  if amt>(2*target):
   return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)
  if amt>target:
   probsurv+=give_me_prob(10.2, i)
  else:
   problose+=give_me_prob(10.2, i)
  i+=1
 return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)

def beta_res(mult, target):
 problose=0
 probsurv=0
 i=0
 while i<100:
  amt = (2401.1 + 103.4*i)*mult
  if amt>(2*target):
   return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)
  if amt>target:
   probsurv+=give_me_prob(3.9, i)
  else:
   problose+=give_me_prob(3.9, i)
  i+=1
 return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)

def gamma_res(mult, target):
 problose=0
 probsurv=0
 i=0
 while i<100:
  amt = (662.6 + target*0.66*i)*mult
  if amt>(2*target):
   return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)
  if amt>target:
   probsurv+=give_me_prob(1.1, i)
  else:
   problose+=give_me_prob(1.1, i)
  i+=1
 return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)

def delta_res(mult, target):
 problose=0
 probsurv=0
 i=0
 while i<100:
  amt = (target*0.32 + 3253.0 + 88.2*i)*mult
  if amt>(2*target):
   return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)
  if amt>target:
   probsurv+=give_me_prob(19.2, i)
  else:
   problose+=give_me_prob(19.2, i)
  i+=1
 return (round(problose,4)*100, round(probsurv,4)*100, round(1-(problose+probsurv),4)*100)

def epsilon_res(mult, target):
 amt = (gen_epsilon_res(9999, target, True))*mult
 if amt>(2*target):
  return (0,0,100)
 if amt>target:
  return (0,100,0)
 else:
  return (100,0,0)

def zeta_res(mult, target):
 if (7531.1*mult)>(target*2):
  return(22,0,78)
 if (7531.1*mult)>target:
  return(22,78,0)
 else:
  return(100,0,0)

def eta_res(mult, target):
 amt = (gen_eta_res(9999, target, True))*mult
 if amt>(2*target):
  return (0,0,100)
 if amt>target:
  return (0,100,0)
 else:
  return (100,0,0)

resFuncLookup={
"alpha":alpha_res,
"beta":beta_res,
"gamma":gamma_res,
"delta":delta_res,
"epsilon":epsilon_res,
"zeta":zeta_res,
"eta":eta_res}

multipliers={
"Maria N.":{"alpha":1.0,"beta":1.0,"gamma":1.0,"delta":1.0,"epsilon":1.0, "zeta":1.0, "eta":1.0},
"Janelle K.":{"alpha":0.48, "beta":0.98, "gamma":1.34, "delta":0.24, "epsilon":0.79, "zeta":0.43, "eta":0.45},#good at beta, *can* win with gamma
"Flint S.":{"alpha":0.42, "beta":0.32, "gamma":0.36, "delta":0.32, "epsilon":1.23, "zeta":0.39, "eta":1.08},
"Amir B.":{"alpha":0.50, "beta":0.72, "gamma":0.42, "delta":0.34, "epsilon":0.78, "zeta":0.41, "eta":0.23},
"Corazon V.":{"alpha":0.59, "beta":0.11, "gamma":0.58, "delta":0.16, "epsilon":0.35, "zeta":0.92, "eta":0.12},#matches on zeta
"Will C.":{"alpha":0.23, "beta":0.55, "gamma":0.14, "delta":0.21, "epsilon":2.11, "zeta":0.12, "eta":0.95}, #outdoes on epsilon
}

viablePilots=["Janelle K.","Amir B.","Corazon V.","Flint S.","Will C."]
viableReses = ["alpha","beta","gamma","delta","epsilon", "zeta","eta"]



print(epsilon_res(2.05, 3150))
print(epsilon_res(2.15, 3150))
print(epsilon_res(2.05, 3250))
print(epsilon_res(2.15, 3250))

print(epsilon_res(2.05, 3150))
print(epsilon_res(2.15, 3150))
print(epsilon_res(2.05, 3250))
print(epsilon_res(2.15, 3250))

print(viableReses)

for pil in viablePilots:
 print(pil)
 lyst=[]
 for res in viableReses:
  lyst.append(resFuncLookup[res](multipliers[pil][res], Earwax))
 print(lyst)
