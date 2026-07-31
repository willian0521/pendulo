import numpy as np 
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

csv_path = Path("data") / "raw"

L = 0.26

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

def centradas (T,h):
    dT = np.zeros(len(T))
    dT[0] = (T[1] - T[0]) / h
    dT[1:-1] = (T[2:] - T[:-2]) / (2*h)
    dT[-1] = (T[-1] - T[-2]) / h
    return dT

dTheta_15 = centradas(real_data_15[:, 1], 1/30)
d2Theta_15 = centradas(dTheta_15, 1/30)

dTheta_40 = centradas(real_data_40[:, 1], 1/30)
d2Theta_40 = centradas(dTheta_40, 1/30)

k_15_vec = ((-9.8 / L) * np.sin(real_data_15[:, 1]) - d2Theta_15 ) / dTheta_15

k_40_vec = ((-9.8 / L) * np.sin(real_data_40[:, 1]) - d2Theta_40 ) / dTheta_40

mask_15 = np.abs(dTheta_15) > 0.05
mask_40 = np.abs(dTheta_40) > 0.05

k_15 = np.mean(k_15_vec[mask_15])
k_40 = np.mean(k_40_vec[mask_40])

print(k_15)
print(k_40)