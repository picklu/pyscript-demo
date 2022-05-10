import numpy as np


def generate_x_and_y(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    return (x, y)
