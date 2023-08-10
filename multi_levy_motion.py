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
num_flights = 5  # Number of Lévy flights

# Create a color list for visualization
colors = plt.cm.jet(np.linspace(0, 1, num_flights))

plt.figure(figsize=(10, 10))

for i in range(num_flights):
    x, y = levy_flight_2D_alpha(num_steps, alpha=1.2, beta=0)
    plt.plot(x, y, marker='o', markersize=2, linestyle='-', color=colors[i])

plt.title('2D Lévy Flight with α=1.4 and Uniform Direction')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
