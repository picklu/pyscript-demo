import matplotlib.pyplot as plt
from data import generate_x_and_y

x, y = generate_x_and_y(1000)
fig, ax = plt.subplots()

ax.scatter(x, y)
fig