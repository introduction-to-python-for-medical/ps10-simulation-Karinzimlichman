import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                # Check neighbors, ensuring we stay within bounds
                neighbors = []
                if i > 0:  # Top neighbor
                    neighbors.append(grid[i - 1][j])
                if i < grid_size - 1:  # Bottom neighbor
                    neighbors.append(grid[i + 1][j])
                if j > 0:  # Left neighbor
                    neighbors.append(grid[i][j - 1])
                if j < grid_size - 1:  # Right neighbor
                    neighbors.append(grid[i][j + 1])
                
                # If any neighbor is on fire, set this tree on fire
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid

