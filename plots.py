import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

csv_path = Path("resources") / "theta.csv"

real_data_40 = np.loadtxt(
    csv_path,
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
) #guardar datos reales

csv_path = Path("resources") / "theta_2.csv"

real_data_15 = np.loadtxt(
    csv_path,
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
) 

teorica_data_15 = np.load('data_teorica_15.npy')

approx_data_40 = np.load('data_aproximada_40.npy') #aproximaciones de rk4 para 40°
tiempos_40 = np.load('tiempos_40rk4.npy')

approx_data_15 = np.load('data_aproximada_15.npy') #aproximaciones de rk4 para 15°
tiempos_15 = np.load('tiempos_15rk4.npy')

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(real_data_40[:, 0], real_data_40[:, 1], c="red", label = "Datos reales")
ax1.plot(tiempos_40 + 11/30, approx_data_40[:, 0], label = "Datos rk4")

ax2.plot(real_data_15[:, 0], real_data_15[:, 1], c = "red")
ax2.plot(tiempos_15 + 0.5, approx_data_15[:, 0], c = "blue")
ax2.plot(tiempos_15, teorica_data_15, c = "purple")

plt.legend()
plt.ylabel("Ángulo")
plt.xlabel("Tiempo")

plt.show()