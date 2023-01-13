# -*- coding: utf-8 -*-

import pandas as pd
import math
import random
import numpy as np
import pickle
import random

koordinata = np.genfromtxt('Vert.csv', delimiter = ',')
koordinata = koordinata[1:]

with open("oblast", "rb") as fp:   # Unpickling
  idx = pickle.load(fp)

#koordinata = koordinata[idx,:]


max_k = 10
results = []
kol_chains = 250

"""Функция создания ветви возбуждаемых диполей"""

def childs(k, dip, j):

  results[j][k].append(dip)

  if  k == max_k-1:
    return
  else:
    k = k+1


  p_child = random.randint(0, 100)
  if p_child <= 50:
    child = 1
  else:
    child = 1

  for m in range(child):

    R = 10
    n = len(idx)
    n_neigh = 0
    Neigh = []
    ps = 0
    p =[]
    dist = []

    for id in range(n):
      view_dipol = idx[id]
      if view_dipol == dip or view_dipol in results[j][k]:
        continue
      R1 = math.sqrt((koordinata[dip][0]*1000 - koordinata[view_dipol][0]*1000)**2 + (koordinata[dip][1]*1000 - koordinata[view_dipol][1]*1000)**2 + (koordinata[dip][2]*1000 - koordinata[view_dipol][2]*1000)**2)
      if R1 < R:
        #R1 = sqrt((koordinata[dip,1]*100 - koordinata[z,1]*100).^2 + (koordinata[dip,2]*100 - koordinata[z,2]*100).^2 + (koordinata[dip,3]*100 - koordinata[z,3]*100).^2)
        dist.append(R1)
        n_neigh = n_neigh + 1
        Neigh.append(view_dipol)

    alpha = np.var(dist, ddof = 1)

    #fprintf('alpha %d\n',alpha)
    for i in range(n_neigh):
      temp = (-(dist[i])**2)/alpha
      temp = math.exp(temp)
      p.append(temp)
      ps = ps + p[-1]


    for i in range(n_neigh):
      p[i] = p[i]/ps


    r = np.random.uniform(0.0, 1.0)
    p.insert(0, 0)
    p = np.cumsum(p)
    for h in range(len(p)):
      if r >= p[h]:
        p[h] = 1
      else:
        p[h] = 0
    i_neigh = sum(p)

    childs(k, Neigh[int(i_neigh-1)], j)

for j in range(kol_chains):
  results.append([])
  for n in range(max_k):
    results[j].append([])
  dip = random.randint(0, len(idx)-1)
  childs(0, idx[dip], j)
  #print(results[j])


"""
j = 0
for dip in idx:
  for i in range(70):
    results.append([])
    for n in range(max_k):
      results[j].append([])
    childs(0,dip,j)
    j+=1
"""


with open("graph_dips_region_test", "wb") as fp:  # Pickling
 pickle.dump(results, fp)


#with open("test", "rb") as fp:   # Unpickling
#  b = pickle.load(fp)

