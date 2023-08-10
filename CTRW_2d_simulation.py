import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def ctrw_2d(num_steps, jump_distribution, waiting_time_distribution):
    jumps_x, jumps_y = jump_distribution(num_steps)
    waiting_times = waiting_time_distribution(num_steps)

    positions_x = np.cumsum(jumps_x)
    positions_y = np.cumsum(jumps_y)
    times = np.cumsum(waiting_times)

    return times, positions_x, positions_y


def jump_dist(num_steps):
    # Random angles for uniform directions
    theta = 2 * np.pi * np.random.rand(num_steps)

    # Lengths of jumps from normal distribution
    r = np.random.normal(0, 1, num_steps)

    jumps_x = r * np.cos(theta)
    jumps_y = r * np.sin(theta)

    return jumps_x, jumps_y


def waiting_time_dist(num_steps):
    return np.random.exponential(5, num_steps)


num_steps = 200
times, positions_x, positions_y = ctrw_2d(num_steps, jump_dist, waiting_time_dist)

# Scale waiting times for animation purposes
scaled_times = np.int_(times/10)

# Expand the positions based on the waiting times
expanded_positions_x = np.repeat(positions_x, scaled_times)
expanded_positions_y = np.repeat(positions_y, scaled_times)

fig, ax = plt.subplots(figsize=(8, 8))
line, = ax.plot([], [], lw=2, marker='o')
ax.set_xlim(1.1 * np.min(positions_x), 1.1 * np.max(positions_x))
ax.set_ylim(1.1 * np.min(positions_y), 1.1 * np.max(positions_y))
ax.grid(True)


def init():
    line.set_data([], [])
    return line,


def update(frame):
    line.set_data(expanded_positions_x[:frame], expanded_positions_y[:frame])
    return line,


ani = FuncAnimation(fig, update, frames=len(expanded_positions_x), init_func=init, blit=True)

# Save the animation
ani.save('ctrw_animation.mp4', writer='ffmpeg', fps=30)
