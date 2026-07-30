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



fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(real_data_40[:, 0], real_data_40[:, 1], c="red", label = "Datos reales")
ax1.plot(tiempos_40, approx_data_40[:, 0], label = "Datos rk4")

ax2.plot(real_data_15[:, 0], real_data_15[:, 1], c = "red")
ax2.plot(tiempos_15, approx_data_15[:, 0], c = "skyblue")
ax2.plot(tiempos_15, teorica_data_15, c = "green")

plt.legend()
plt.ylabel("Ángulo")
plt.xlabel("Tiempo")

plt.show()

print(teorica_data_15.shape)
print(real_data_15.shape)
plt.plot(tiempos_15[1:173], (real_data_15[1:173, 1] - teorica_data_15[1:173])**2, label = "Error cuadratico")
plt.legend()
plt.show()