from scipy.optimize import curve_fit
from pathlib import Path
import numpy as np

def pendulum_15_teorica(t, A = 1, beta = 0, omega = 1, phi = 0):
    return A * np.exp(-beta * t) * np.cos(omega * t + phi)

csv_path = Path("resources") / "theta_2.csv"

data_experimental = np.loadtxt(
    csv_path,
    delimiter=",",
    skiprows=1,
    usecols=(0, 1)
)

p0 = np.array([0.27208133034476484, 0.35, 2*np.pi, 0])

param, _ = curve_fit(
    pendulum_15_teorica,
    data_experimental[:, 0],
    data_experimental[:, 1],
    p0
)

print(param)