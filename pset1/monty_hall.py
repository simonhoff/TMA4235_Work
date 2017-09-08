import numpy as np
import matplotlib as mplot

N_DOORS = 3;

NIT = 500;

for i in range(NIT):
    choices = range(N_DOORS)
    chosen_door = np.random.sample(choices)
    no_prize_door = np.random.sample(choices)

