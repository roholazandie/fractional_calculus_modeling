import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom

# Parameters
m = 1.0  # particle mass
dt = 0.001  # time step
n_steps = 10000
n_particles = 5
position_range = [0.0, 2.0]  # rectangle limits for position
momentum_range = [0.0, 2.0]  # rectangle limits for momentum


def poisson_bracket(f, g, q, p):
    q_mesh, p_mesh = np.meshgrid(q, p)
    f_values = f(q_mesh, p_mesh)

    if type(g) == np.ndarray:
        g_values = g
    else:
        g_values = g(q_mesh, p_mesh)

    if g_values.shape != f_values.shape:
        #upsample g_values to match f_values
        g_values = zoom(g_values, zoom=f_values.shape[0] / g_values.shape[0])

    dfdq, dfdp = np.gradient(f_values)
    dgdq, dgdp = np.gradient(g_values)

    return dfdq * dgdp - dfdp * dgdq

# Hamiltonian
def H(x, p):
    return p**2 / (2*m) + V(x)

# Potential
def V(x):
    return x ** 6 + 4 * x ** 3 - 5 * x ** 2 - 4 * x

# Force
def F(x):
    return -6 * x ** 5 - 12 * x ** 2 + 10 * x + 4


# Initialize particles in a rectangular region in phase space
positions = np.random.uniform(position_range[0], position_range[1], n_particles)
momenta = np.random.uniform(momentum_range[0], momentum_range[1], n_particles)

# Create a histogram for phase space
n_bins = 100

plt.figure(figsize=(6, 5))

for step in range(n_steps):
    # Hamilton's equations
    dq = momenta / m * dt
    dp = F(positions) * dt

    positions += dq
    momenta += dp


    # Update histogram every 500 steps
    if step % 500 == 0:
        rho_values, _, _ = np.histogram2d(positions, momenta, bins=n_bins,
                                          range=[2 * np.array(position_range), 2 * np.array(momentum_range)])
        plt.clf()


        # Example to compute Poisson bracket of H with itself
        poisson_HH = poisson_bracket(H, H, positions, momenta)
        print(np.sum(poisson_HH)) # should be zero
        rho_values = rho_values / np.sum(rho_values)
        print("sum of rho values: ", np.sum(rho_values))
        poisson_Hrho = poisson_bracket(H, rho_values, positions, momenta)
        print(np.sum(poisson_Hrho))



        plt.imshow(rho_values.T,
                   extent=[2 * position_range[0], 2 * position_range[1], 2 * momentum_range[0], 2 * momentum_range[1]],
                   origin='lower', aspect='auto', interpolation='nearest')
        plt.title(f'Time step: {step}')
        plt.xlabel('Position')
        plt.ylabel('Momentum')
        plt.colorbar()

        plt.pause(0.1)

plt.show()
