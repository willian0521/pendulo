import numpy as np
import os

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import src.rk4 as rk4

def pendulum(t, T):
    return np.array([T[1], (-32.97025023) * np.sin(T[0])])

def pendulum_15_teorica(t, A = 1, beta = 0, omega = 1, phi = 0):
    return A * np.exp(-beta * t) * np.cos(omega * t + phi)

approximated_data_40, time_40 = rk4.rk4(0, 14.066666, function = pendulum, initial_value=np.array([0.7345944593392267, 0]), step = 1/30)

approximated_data_15, time_15 = rk4.rk4(0, 16.4, pendulum, np.array([0.2717609501870864, 0]), step = 1/30)

teorica_data_15 = pendulum_15_teorica(time_15, 0.18009588, 0.03834783, 5.81434611, 0.27374829)

np.savez(os.path.join('data', 'processed','datos_40.npz'), tiempo=time_40, data_rk4 = approximated_data_40)
np.savez(os.path.join('data', 'processed','datos_15.npz'), tiempo = time_15, data_rk4 = approximated_data_15, data_teorica = teorica_data_15)