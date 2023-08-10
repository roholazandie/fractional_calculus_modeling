import numpy as np
import matplotlib.pyplot as plt


def ctrw(num_steps, jump_distribution, waiting_time_distribution):
    # Generate jump lengths and waiting times
    jumps = jump_distribution(num_steps)
    waiting_times = waiting_time_distribution(num_steps)

    # Cumulative sum of jumps gives the position
    positions = np.cumsum(jumps)

    # Cumulative sum of waiting times gives the time of each jump
    times = np.cumsum(waiting_times)

    return times, positions


# Example distributions for jump lengths and waiting times
def jump_dist(num_steps):
    # Gaussian distribution for jump lengths with mean 0 and standard deviation 1
    return np.random.normal(0, 1, num_steps)


def waiting_time_dist(num_steps):
    # Exponential distribution for waiting times with mean 1
    return np.random.exponential(1, num_steps)


num_steps = 1000
times, positions = ctrw(num_steps, jump_dist, waiting_time_dist)

plt.plot(times, positions)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Continuous Time Random Walk (CTRW)')
plt.grid(True)
plt.show()
