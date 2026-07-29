import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
csv_path = Path("resources") / "theta.csv"
csv_path = Path(__file__).parent / "resources" / "theta.csv"

real_data = np.loadtxt(
    csv_path,
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
) #guardar datos reales
approx_data = np.zeros(10) #aproximaciones de rk4

plt.plot(real_data[:, 0], real_data[:, 1], c="red")

#plt.plot(approx_data[:][0], approx_data[:][1])

plt.ylabel("Ángulo")
plt.xlabel("Tiempo")

plt.show()