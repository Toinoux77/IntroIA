import random
import tiles
import visual
import time

def initialize_grid(size):
    grid = [[tiles.TILE(x,y) for x in range(size)] for y in range(size)]
    return grid

def run_wfc(grid,watch = False):
    first_tile = minimum_entropy_tile(grid)
    if first_tile is None:
        return grid
        
    first_tile.collapse()
    stack = [first_tile]

    while True:
        # --- PHASE A : PROPAGATION DE L'ONDE ---
        while len(stack) > 0:
            current_tile = stack.pop(0)
            current_tile.set_neighbors(current_tile.x, current_tile.y, grid)
            
            for direction in ['NORTH', 'EAST', 'SOUTH', 'WEST']:
                if current_tile.update_neighbor_possibilities(direction):
                    neighbor = current_tile.neighbors[direction]
            
                    if neighbor not in stack:
                        stack.append(neighbor)
                    
                    # Si le voisin n'a plus qu'un seul choix, on l'effondre
                    if neighbor.entropy == 1:
                        neighbor.collapse()

        if watch:
            time.sleep(.2)
        visual.draw_grid(grid)

        # --- PHASE B : SÉLECTION DE LA PROCHAINE TUILE ---
        # L'onde est stabilisée (stack est vide). On cherche la tuile stricte suivante.
        next_tile = minimum_entropy_tile(grid)
        
        if next_tile is None:
            break
            
        next_tile.collapse()
        stack.append(next_tile)

    return grid


def minimum_entropy_tile(grid):
    minimum_entropy_tiles = []
    minimum_entropy = float('inf')
    size = len(grid)
    for y in range(size):
        for x in range(size):
            tile = grid[y][x]
            if tile.entropy > 1:
                if tile.entropy < minimum_entropy:
                    minimum_entropy = tile.entropy
                    minimum_entropy_tiles = [grid[y][x]]
                elif tile.entropy == minimum_entropy:
                    minimum_entropy_tiles.append(grid[y][x])
    if minimum_entropy_tiles:
        return random.choice(minimum_entropy_tiles)    
    return None