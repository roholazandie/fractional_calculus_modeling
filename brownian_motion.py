import numpy as np
import matplotlib.pyplot as plt


def brownian_motion_2D(n, delta_t=1, variance=1):
    delta_x = np.sqrt(variance * delta_t) * np.random.randn(n)
    delta_y = np.sqrt(variance * delta_t) * np.random.randn(n)

    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)

    return x, y


# Number of steps for the Brownian motion
num_steps = 100000
#
x, y = brownian_motion_2D(num_steps)
#
plt.figure(figsize=(10, 10))
plt.plot(x, y, marker='o', markersize=2, linestyle='-')
plt.title('2D Brownian Motion')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()



# Compute the time correlation of the x and y coordinates
# def compute_normalized_time_correlation(x, max_lag):
#     mean_x = np.mean(x)
#     var_x = np.var(x)
#     correlation = [(np.mean(x[i:] * x[:len(x)-i]) - mean_x**2) / var_x for i in range(max_lag)]
#     return correlation
#
# max_lag = 100
# correlation_x = compute_normalized_time_correlation(x, max_lag)
# correlation_y = compute_normalized_time_correlation(y, max_lag)
#
# plt.figure(figsize=(10, 5))
# plt.plot(correlation_x, label='Correlation of X')
# plt.plot(correlation_y, label='Correlation of Y')
# plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# plt.title('Time Correlation of X and Y Coordinates')
# plt.xlabel('Lag')
# plt.ylabel('Correlation')
# plt.legend()
# plt.grid(True)
# plt.show()