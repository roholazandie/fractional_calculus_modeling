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
x, y = brownian_motion_2D(num_steps)

fig, ax = plt.subplots(figsize=(10, 10))
line, = ax.plot([], [], marker='o', markersize=2, linestyle='-')
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_title('2D Brownian Motion Animated')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True, repeat=False)


# To save the animation to an mp4 file:
ani.save('brownian_motion_animation.mp4', writer='ffmpeg', fps=30)

# plt.show()
plt.close(fig)  # Close the figure after saving