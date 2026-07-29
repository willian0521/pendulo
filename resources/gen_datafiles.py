import numpy as np
import rk4

def pendulum(t, T):
    return np.array([T[1], (-9.81 / 0.26) * np.sin(T[0])])

approximated_data, time = rk4.rk4(0, 14.066666, 1000, pendulum, np.array([np.deg2rad(40), 0]))

np.save("data_aproximadark4", approximated_data)
np.save("tiempos_rk4", time)