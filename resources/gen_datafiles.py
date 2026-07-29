import numpy as np
import rk4

def pendulum(t, T):
    return np.array([T[1], (-9.81 / 0.26) * np.sin(T[0])])

handtaken_data = np.array([
    [0, 40],
    [5, 26],
    [10, 20],
    [15, 14],
    [20, 5],
    [25, 3]
], dtype=float)

handtaken_data = np.deg2rad(handtaken_data)

approximated_data = rk4.rk4(0, 20, 1000, pendulum, (np.deg2rad(40), 0))

np.save("data_manual", handtaken_data)
np.save("data_aproximadark4", approximated_data)
