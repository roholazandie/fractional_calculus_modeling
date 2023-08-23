import numpy as np
import matplotlib.pyplot as plt


def simulate_wiener_process(n, dt):
    """
    Simulate a Wiener process.
    :param n: Number of steps.
    :param dt: Time step.
    :return: A numpy array representing the Wiener process.
    """
    # Generate normally distributed random increments with mean=0 and variance=dt
    increments = np.random.normal(loc=0, scale=np.sqrt(dt), size=n)

    # Compute the cumulative sum of these increments to obtain the process values
    return np.insert(np.cumsum(increments), 0, 0)


# Parameters
n = 1000  # number of steps
dt = 0.01  # time step
num_paths = 50  # number of Wiener processes to simulate
t = np.linspace(0, n * dt, n + 1)  # time vector

plt.figure(figsize=(10, 6))

# Simulate and plot each path
for i in range(num_paths):
    W = simulate_wiener_process(n, dt)
    plt.plot(t, W, label=f"Path {i + 1}")

plt.title("Multiple Wiener Process Simulations")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
