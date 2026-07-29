import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

csv_path = Path("resources") / "theta.csv"

real_data = np.loadtxt(
    csv_path,
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
) #guardar datos reales

approx_data = np.load('data_aproximadark4.npy') #aproximaciones de rk4
tiempos = np.load('tiempos_rk4.npy')

plt.plot(real_data[:, 0], real_data[:, 1], c="red")
plt.plot(tiempos + 0.3, approx_data[:, 0])

plt.ylabel("Ángulo")
plt.xlabel("Tiempo")

plt.show()