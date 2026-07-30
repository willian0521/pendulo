import numpy as np

def rk4(start, end, function, initial_value, number_of_dots = None, step = None):
    if number_of_dots is None and step is None:
        raise ValueError("Debe especificarse la cantidad de puntos o el paso")
    elif number_of_dots is None:
        t = np.arange(start, end, step)
    else:
        step = (end - start) / number_of_dots
        t = np.linspace(start, end, number_of_dots + 1)
    w = np.zeros([t.size, initial_value.size])
    w[0, :] = initial_value
    for i in range(t.size - 1):
        k1 = step * function(t[i], w[i, :])
        k2 = step * function(t[i] + step / 2, w[i, :] + k1 / 2)
        k3 = step * function(t[i] + step / 2, w[i, :] + k2 / 2)
        k4 = step * function(t[i+1], w[i, :] + k3)
        w[i+1, :] = w[i, :] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return w, t