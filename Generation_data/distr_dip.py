import numpy as np
import matplotlib.pyplot as plt
import pickle

with open("graph_dips_region", "rb") as fp:   # Unpickling
  graph_dips = pickle.load(fp)


dips = np.array(graph_dips).ravel()

plt.hist(dips, density=False, facecolor='g')

