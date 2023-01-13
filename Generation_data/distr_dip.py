import numpy as np
import matplotlib.pyplot as plt
import pickle

with open("graph_dips_region", "rb") as fp:   # Unpickling
  graph_dips = pickle.load(fp)


dips = np.array(graph_dips).ravel()

plt.hist(dips,1000,density=False, facecolor='g')

count = 0
count_i = 0
for i in graph_dips:
  fl = False
  for j in i:
    if j[0] == 110:
      print(i)
      count+=1
      fl = True
  if fl:
    count_i+=1

print(count)
print(count_i)