import numpy as np
import rk4

def pendulum(t, T):
    return np.array([T[1], (-32.97025023) * np.sin(T[0])])

def pendulum_15_teorica(t, A = 1, beta = 0, omega = 1, phi = 0):
    return A * np.exp(-beta * t) * np.cos(omega * t + phi)

approximated_data_40, time_40 = rk4.rk4(0, 14.066666, function = pendulum, initial_value=np.array([0.7345944593392267, 0]), step = 1/30)

approximated_data_15, time_15 = rk4.rk4(0, 16.9, pendulum, np.array([0.2717609501870864, 0]), step = 1/30)

teorica_data_15 = pendulum_15_teorica(time_15, -0.18005327,  0.0406344,   5.78504738,  0.81667062)

np.save("data_aproximada_40", approximated_data_40)
np.save("tiempos_40rk4", time_40)
np.save("data_aproximada_15", approximated_data_15)
np.save("tiempos_15rk4", time_15)
np.save("data_teorica_15", teorica_data_15)