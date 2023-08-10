import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable


def levy_flight_2D_alpha(n, alpha=1.8, beta=0, scale=1):
    # Random angles for uniform directions
    theta = 2 * np.pi * np.random.rand(n)

    # Lengths of jumps from Lévy stable distribution
    r = levy_stable.rvs(alpha, beta, size=n, scale=scale)

    delta_x = r * np.cos(theta)
    delta_y = r * np.sin(theta)

    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)

    return x, y


# Number of steps for the Lévy flight
num_steps = 1000

x, y = levy_flight_2D_alpha(num_steps, alpha=1.4, beta=0)

plt.figure(figsize=(10, 10))
plt.plot(x, y, marker='o', markersize=2, linestyle='-')
plt.title('2D Lévy Flight with α=1.6 and Uniform Direction')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
