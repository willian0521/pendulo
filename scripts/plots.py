import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import sys
from os import path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

csv_path = Path("data") / "raw"

real_data_40 = np.loadtxt(
    csv_path / "theta_40.csv",
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
) #guardar datos reales

real_data_15 = np.loadtxt(
    csv_path / "theta_15.csv",
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
) 

data_sim15 = np.load(path.join('data', 'processed', 'datos_15.npz'))
data_sim40 = np.load(path.join('data', 'processed', 'datos_40.npz'))

teorica_data_15 = data_sim15['data_teorica']
approx_data_15 = data_sim15['data_rk4'] #aproximaciones de rk4 para 15°
tiempos_15 = data_sim15['tiempo']


approx_data_40 = data_sim40['data_rk4'] #aproximaciones de rk4 para 40°
tiempos_40 = data_sim40['tiempo']


fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(real_data_40[:, 0], real_data_40[:, 1], c="red", label = "Datos reales")
axs[0, 0].plot(tiempos_40, approx_data_40[:, 0], label = "Datos rk4")

axs[1,0].plot(real_data_15[:, 0], real_data_15[:, 1], c = "red")
axs[1, 0].plot(tiempos_15, approx_data_15[:, 0], c = "skyblue")
axs[1, 0].plot(tiempos_15, teorica_data_15, c = "green")

plt.ylabel("Ángulo")
plt.xlabel("Tiempo")

error_cuadratico_15 = (real_data_15[:492, 1] - teorica_data_15)**2
error_absoluto_15 = np.abs(real_data_15[:492, 1] - teorica_data_15)

error_cuadratico_40 = (real_data_40[:, 1] - approx_data_40[:, 0])**2
error_absoluto_40 = np.abs(real_data_40[:, 1] - approx_data_40[:, 0])

axs[1, 1].plot(tiempos_15, error_cuadratico_15, label = "Error cuadratico", c = "blue")
axs[1, 1].plot(tiempos_15, error_absoluto_15, label = "Error absoluto", c="orange")

axs[0, 1].plot(tiempos_40, error_cuadratico_40, label = "Error cuadratico", c="blue")
axs[0, 1].plot(tiempos_40, error_absoluto_40, label = "Error absoluto", c="orange")

plt.legend()
plt.show()

print(f"Error medio (15°): {np.mean(error_absoluto_15)}. Cota del error: ({np.min(error_absoluto_15)}, {np.max(error_absoluto_15)})")
print(f"Error cuadrático medio (15°): {np.mean(error_cuadratico_15)}. Cota del error: ({np.min(error_cuadratico_15)}, {np.max(error_cuadratico_15)})")

print(f"Error medio (40°): {np.mean(error_absoluto_40)}. Cota del error: ({np.min(error_absoluto_40)}, {np.max(error_absoluto_40)})")
print(f"Error cuadrático medio (40°): {np.mean(error_cuadratico_40)}. Cota del error: ({np.min(error_cuadratico_40)}, {np.max(error_cuadratico_40)})")