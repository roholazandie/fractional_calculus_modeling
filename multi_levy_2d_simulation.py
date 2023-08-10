import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable
from matplotlib.animation import FuncAnimation

def levy_flight_2D_alpha(n, alpha=1.2, beta=0, scale=2):
    # Random angles for uniform directions
    theta = 2 * np.pi * np.random.rand(n)

    # Lengths of jumps from Lévy stable distribution
    r = levy_stable.rvs(alpha, beta, size=n, scale=scale)

    delta_x = r * np.cos(theta)
    delta_y = r * np.sin(theta)

    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)

    return x, y

num_steps = 2000
num_flights = 6  # Number of Lévy flights

coords = [levy_flight_2D_alpha(num_steps) for _ in range(num_flights)]

# Get combined x and y for setting axis limits
all_x = np.hstack([c[0] for c in coords])
all_y = np.hstack([c[1] for c in coords])

fig, ax = plt.subplots(figsize=(10, 10))
colors = plt.cm.jet(np.linspace(0, 1, num_flights))
lines = [ax.plot([], [], marker='o', markersize=2, linestyle='-', color=colors[i])[0] for i in range(num_flights)]
ax.set_xlim(min(all_x), max(all_x))
ax.set_ylim(min(all_y), max(all_y))
ax.grid(True)

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    for coord, line in zip(coords, lines):
        x, y = coord
        line.set_data(x[:i], y[:i])
    return lines

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, repeat=False)

# Save the animation
ani.save('multiple_levy_flights_animation.mp4', writer='ffmpeg', fps=30)

plt.close(fig)  # Close the figure after saving
