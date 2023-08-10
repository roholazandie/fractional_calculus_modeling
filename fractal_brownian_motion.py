import numpy as np
import matplotlib.pyplot as plt


def hosking(n, H):
    d = np.arange(1, n) + 1
    cov = 0.5 * (d ** (2 * H) - (d - 1) ** (2 * H))

    w = np.random.normal(0, 1, n)
    v = np.zeros(n)
    x = np.zeros(n)

    for t in range(1, n):
        past_vals = w[:t]
        v[t] = w[t] - np.dot(cov[:t], past_vals[::-1])
        x[t] = x[t - 1] + v[t]

    return x


def fbm_2d(n, H):
    x = hosking(n, H)
    y = hosking(n, H)
    return x, y


n = 1000
H_values = [0.3, 0.5, 0.7]

plt.figure(figsize=(8, 8))

for H in H_values:
    x, y = fbm_2d(n, H)
    plt.plot(x, y, label=f'H={H}')

plt.legend()
plt.title("2D Fractional Brownian Motion using Hosking's Method")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
