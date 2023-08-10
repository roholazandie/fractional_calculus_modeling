import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable
from matplotlib.animation import FuncAnimation

def levy_flight_2D_alpha(n, alpha=1.3, beta=0, scale=2):
    # Random angles for uniform directions
    theta = 2 * np.pi * np.random.rand(n)

    # Lengths of jumps from Lévy stable distribution
    r = levy_stable.rvs(alpha, beta, size=n, scale=scale)

    delta_x = r * np.cos(theta)
    delta_y = r * np.sin(theta)

    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)

    return x, y

num_steps = 1000
x, y = levy_flight_2D_alpha(num_steps)

fig, ax = plt.subplots(figsize=(10, 10))
line, = ax.plot([], [], marker='o', markersize=2, linestyle='-')
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.grid(True)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, repeat=False)

# Save the animation
ani.save('levy_flight_animation.mp4', writer='ffmpeg', fps=30)

plt.close(fig)  # Close the figure after saving
