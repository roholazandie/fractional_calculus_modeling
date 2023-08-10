import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def brownian_motion_2D(n, delta_t=1, variance=1):
    # Random angles for uniform directions
    theta = 2 * np.pi * np.random.rand(n)

    r = np.sqrt(variance * delta_t) * np.random.randn(n)

    delta_x = r * np.cos(theta)
    delta_y = r * np.sin(theta)

    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)

    return x, y


num_steps = 1000
num_walks = 5  # Number of random walks

# Store paths for all walks
walks_x = [brownian_motion_2D(num_steps)[0] for _ in range(num_walks)]
walks_y = [brownian_motion_2D(num_steps)[1] for _ in range(num_walks)]

fig, ax = plt.subplots(figsize=(10, 10))

lines = [ax.plot([], [], marker='o', markersize=2, linestyle='-')[0] for _ in range(num_walks)]

xmin, xmax = min([min(w) for w in walks_x]), max([max(w) for w in walks_x])
ymin, ymax = min([min(w) for w in walks_y]), max([max(w) for w in walks_y])

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_title('2D Brownian Motion Animated')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)


def init():
    for line in lines:
        line.set_data([], [])
    return lines


def animate(i):
    for line, walk_x, walk_y in zip(lines, walks_x, walks_y):
        line.set_data(walk_x[:i], walk_y[:i])
    return lines


ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, repeat=False)


# To save the animation to an mp4 file:
ani.save('multiple_brownian_motion_animation.mp4', writer='ffmpeg', fps=30)

# plt.show()
plt.close(fig)  # Close the figure after saving
