import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0  # particle mass
dt = 0.001  # time step
n_steps = 10000
n_particles = 100  # Number of particles
position_range = [0.0, 1.0]  # rectangle limits for position
momentum_range = [1.0, 2.0]  # rectangle limits for momentum


def poisson_bracket(f, g, q, p):
    dfdq = (f(q + 1e-5, p) - f(q - 1e-5, p)) / (2e-5)
    dgdp = (g(q, p + 1e-5) - g(q, p - 1e-5)) / (2e-5)
    dfdp = (f(q, p + 1e-5) - f(q, p - 1e-5)) / (2e-5)
    dgdq = (g(q + 1e-5, p) - g(q - 1e-5, p)) / (2e-5)

    return dfdq * dgdp - dfdp * dgdq


# Hamiltonian
def H(x, p):
    return p ** 2 / (2 * m) + V(x)


# Potential
def V(x):
    return x ** 6 + 4 * x ** 3 - 5 * x ** 2 - 4 * x


# Force
def F(x):
    return -6 * x ** 5 - 12 * x ** 2 + 10 * x + 4


# Initialize n_particles at random positions and momenta
positions = np.random.uniform(position_range[0], position_range[1], n_particles)
momenta = np.random.uniform(momentum_range[0], momentum_range[1], n_particles)

# Lists to store time evolution of position and momentum
positions_history = [positions.copy()]
momenta_history = [momenta.copy()]

for step in range(n_steps):
    # Hamilton's equations using Poisson brackets for position update
    dq = poisson_bracket(lambda q, p: q, H, positions, momenta)
    dp = F(positions) * dt

    positions += dq * dt
    momenta += dp

    # Store the new values
    positions_history.append(positions.copy())
    momenta_history.append(momenta.copy())

# Plotting the results in phase space
plt.figure(figsize=(8, 6))

for i in range(n_particles):
    plt.plot([pos[i] for pos in positions_history], [mom[i] for mom in momenta_history], color='blue', alpha=0.5)

plt.xlabel('Position')
plt.ylabel('Momentum')
plt.title('Phase Space Evolution')
plt.grid(True)

plt.tight_layout()
plt.show()
