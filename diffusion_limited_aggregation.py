import numpy as np
import random
import matplotlib.pyplot as plt

width, height = 200, 200
grid = np.zeros((width, height))

# Define the initial seed at the center of the grid
grid[width // 2][height // 2] = 1


def is_adjacent_to_aggregate(x, y, grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and grid[nx][ny] == 1:
            return True
    return False


def perform_random_walk(x, y, grid):
    while True:
        direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x += direction[0]
        y += direction[1]

        # Check boundaries
        if x < 0 or x >= width or y < 0 or y >= height:
            return None, None

        # Check if particle can stick
        if is_adjacent_to_aggregate(x, y, grid):
            return x, y


def dla_step(grid):
    # Introduce a new particle from a random position on the boundary
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        x, y = 0, random.randint(0, height - 1)
    elif side == "bottom":
        x, y = width - 1, random.randint(0, height - 1)
    elif side == "left":
        x, y = random.randint(0, width - 1), 0
    else:
        x, y = random.randint(0, width - 1), height - 1

    x, y = perform_random_walk(x, y, grid)
    if x is not None and y is not None:
        grid[x][y] = 1


num_particles = 1000000
for _ in range(num_particles):
    dla_step(grid)

# Display the aggregate
plt.imshow(grid, cmap="gray")
plt.show()
