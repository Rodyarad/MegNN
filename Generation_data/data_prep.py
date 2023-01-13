import pandas as pd
import math
import random
import numpy as np
import pickle
import matplotlib.pyplot as plt

kol_sensor = 306
target_snr_db = 10
time_m = 1000

with open("graph_dips_region_test", "rb") as fp:   # Unpickling
  graph_dips = pickle.load(fp)


kol_graf = len(graph_dips)
k = 10


def noiser(sig,target_snr_db):
    rez = []
    for i in range(0, kol_sensor):
        watts = []
        for j in range(time_m):
            watts.append(sig[i][j] ** 2)

        sig_avg_watts = np.mean(watts)
        sig_avg_db = 10 * np.log10(sig_avg_watts)

        noise_avg_db = sig_avg_db - target_snr_db
        noise_avg_watts = 10 ** (noise_avg_db / 10)

        mean_noise = 0
        noise_volts = np.random.normal(mean_noise, np.sqrt(noise_avg_watts), len(watts))

        temp = sig[i] + noise_volts
        rez.append(np.mean(temp))
    return rez




rez = []

for i in range(0, kol_graf):
    temp = graph_dips[i]
    temp_rez = []
    for j in range(0, k):
        if len(temp[j]) > 1:
            sig = [[0]]
            for z in temp[j]:
                ad = 'region/snap' + str(z) + '.csv'
                twinks = pd.read_csv(ad, header=None)
                twinks = twinks.to_numpy()
                sig = sig + twinks
        else:
            ad = 'region/snap' + str(temp[j][0]) + '.csv'
            sig = pd.read_csv(ad, header=None)
            sig = sig.to_numpy()

        temp_rez.append([])
        temp_rez[j] = noiser(sig.tolist(),target_snr_db)

    rez.append(temp_rez)
    print(f'Обработана последовательность {i}')

X = np.array(rez)
np.save('X_test', X)
