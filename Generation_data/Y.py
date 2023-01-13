import pickle
import numpy as np

with open("graph_dips_region_test", "rb") as fp:   # Unpickling
  graph_dips = pickle.load(fp)

with open("oblast", "rb") as fs:   # Unpickling
  oblast = pickle.load(fs)

#TODO сделать разряженный ground truth
#Y_sparse = []
Y = np.zeros((len(graph_dips),len(graph_dips[0]),len(oblast)))
for sample in range(len(graph_dips)):
       for j in range(len(graph_dips[0])):
           for k in range(len(graph_dips[sample][j])):
               dip = graph_dips[sample][j][k]
               id_dip = oblast.index(dip)
               Y[sample,j,id_dip] = 1

np.save('Y_test',Y)