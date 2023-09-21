import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
m = 1.0  # particle mass
dt = 0.001  # time step
n_steps = 1000
n_particles = 10  # Number of particles
position_range = [0.0, 2.0]  # rectangle limits for position
momentum_range = [0.0, 2.0]  # rectangle limits for momentum

# Hamiltonian
def H(x, p):
    return p**2 / (2*m) + V(x)

# Potential
def V(x):
    return x ** 6 + 4 * x ** 3 - 5 * x ** 2 - 4 * x

# Force
def F(x):
    return -6 * x ** 5 - 12 * x ** 2 + 10 * x + 4

# Initialize n_particles at random positions and momenta
positions = np.random.uniform(position_range[0], position_range[1], n_particles)
momenta = np.random.uniform(momentum_range[0], momentum_range[1], n_particles)

fig, ax = plt.subplots(figsize=(8, 6))
lines = [ax.plot([], [])[0] for _ in range(n_particles)]
ax.set_xlim(position_range[0]-3, position_range[1])
ax.set_ylim(momentum_range[0]-3, momentum_range[1])
ax.set_xlabel('Position')
ax.set_ylabel('Momentum')
ax.set_title('Phase Space Evolution')

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(step):
    global positions, momenta
    # Hamilton's equations
    dq = momenta / m * dt
    dp = F(positions) * dt

    positions += dq
    momenta += dp

    for i, line in enumerate(lines):
        x_data, y_data = line.get_data()
        x_data = np.append(x_data, positions[i])
        y_data = np.append(y_data, momenta[i])
        line.set_data(x_data, y_data)

    return lines

ani = FuncAnimation(fig, update, frames=range(n_steps), init_func=init, blit=True)

# Save the animation as an mp4 file
ani.save('phase_space_evolution.mp4', writer='ffmpeg', fps=30)

plt.tight_layout()
plt.show()

