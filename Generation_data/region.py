import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import pickle

d = np.genfromtxt('Vert.csv', delimiter = ',')
d = d[1:]

R = 7
n = 15002
n_neigh = 0
Neigh = []
dist = []
dip = 300

"""
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Выбранный диполь')

ax1.scatter(d[:,0]*1000, d[:,1]*1000, s = 1, marker = '.')
ax1.scatter(d[dip,0]*1000, d[dip,1]*1000, color='orange', s=40, marker='o')

ax2.scatter(d[:,0]*1000, d[:,2]*1000, s = 1, marker = '.')
ax2.scatter(d[dip,0]*1000, d[dip,2]*1000, color='orange', s=40, marker='o')
"""



for view_dipol in range(n):
    if view_dipol == dip:
        continue
    R1 = math.sqrt((d[dip][0] * 1000 - d[view_dipol][0] * 1000) ** 2 + (
                d[dip][1] * 1000 - d[view_dipol][1] * 1000) ** 2 + (
                               d[dip][2] * 1000 - d[view_dipol][2] * 1000) ** 2)
    if R1 < R:
        dist.append(R1)
        n_neigh = n_neigh + 1
        Neigh.append(view_dipol)


Neigh.append(dip)

print(f'Количество диполей, попавших в область = {len(Neigh)}')

d_dip = []
for view_dipol in Neigh:
    temp = []
    for j in range(len(Neigh)):
        if Neigh[j] == view_dipol:
            continue
        R1 = math.sqrt((d[Neigh[j]][0] * 1000 - d[view_dipol][0] * 1000) ** 2 + (
                d[Neigh[j]][1] * 1000 - d[view_dipol][1] * 1000) ** 2 + (
                               d[Neigh[j]][2] * 1000 - d[view_dipol][2] * 1000) ** 2)
        temp.append(R1)
    d_dip.append(temp)

#with open("oblast", "wb") as fp:  # Pickling
  #pickle.dump(Neigh, fp)