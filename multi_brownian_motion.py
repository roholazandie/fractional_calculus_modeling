import numpy as np
import matplotlib.pyplot as plt

def brownian_motion_2D(n, delta_t=1, variance=1):
    delta_x = np.sqrt(variance * delta_t) * np.random.randn(n)
    delta_y = np.sqrt(variance * delta_t) * np.random.randn(n)

    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)

    return x, y

# Number of steps for the Brownian motion
num_steps = 1000
num_walks = 5  # Number of random walks

# Create a color list for visualization
colors = plt.cm.jet(np.linspace(0, 1, num_walks))

plt.figure(figsize=(10, 10))

for i in range(num_walks):
    x, y = brownian_motion_2D(num_steps)
    plt.plot(x, y, marker='o', markersize=2, linestyle='-', color=colors[i])

plt.title('2D Brownian Motion')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
