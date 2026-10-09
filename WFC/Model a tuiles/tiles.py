import random
import config

class TILE:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.possible_tiles = list(config.TILE_RULES.keys())
        self.entropy = len(self.possible_tiles)
        self.neighbors = dict()

    def collapse(self):
        if self.entropy > 1:
            if not self.possible_tiles:
                print("No possible tiles left to collapse.")
                return False
                
            # 1. Récupération des poids
            weights = [config.TILE_WEIGHTS[tile] for tile in self.possible_tiles]
            
            # 2. Tirage (renvoie une liste à 1 élément, ex: ['LAND_TILE'])
            chosen_list = random.choices(self.possible_tiles, weights=weights, k=1)
            
            # 3. Extraction de la chaîne de caractères (ex: 'LAND_TILE')
            self.possible_tiles = [chosen_list[0]]  # <-- CORRECTION ICI
            self.entropy = 1
            return True
        return False

    def pre_collapse(self,TILE):
        self.possible_tiles = [TILE]
        self.entropy = 2


    def set_neighbors(self, x, y, grid):
        neighbors = {}
        if x > 0:
            neighbors['WEST'] = grid[y][x-1]
        if x < len(grid[0]) - 1:
            neighbors['EAST'] = grid[y][x+1]
        if y > 0:
            neighbors['NORTH'] = grid[y-1][x]
        if y < len(grid) - 1:
            neighbors['SOUTH'] = grid[y+1][x]
        self.neighbors = neighbors

    def get_neighbor_possibilities(self, direction):
        if direction in self.neighbors and self.neighbors[direction] is not None:
            return self.neighbors[direction].get_possible_tiles()
        else:
            print(f"No neighbor in direction {direction} for tile at position ({self.x}, {self.y})")
            return []

    # Returns True if the neighbor's possibilities were updated, False otherwise
    def update_neighbor_possibilities(self, direction):
        if direction in self.neighbors and self.neighbors[direction] is not None and self.neighbors[direction].entropy > 1:
            neighbor = self.neighbors[direction]
            neighbor_possibilities = neighbor.possible_tiles
            valid_neighbor_tiles = []
            
            # On cherche quelles tuiles du VOISIN sont compatibles avec la tuile actuelle
            for possible_tile in neighbor_possibilities:
                is_valid = False
                
                for tile in self.possible_tiles:
                    if direction == 'NORTH':
                        # Le NORD de ma tuile actuelle doit correspondre au SUD du voisin du dessus
                        if config.TILE_RULES[tile][0] == config.TILE_RULES[possible_tile][2]:
                            is_valid = True
                            break
                    elif direction == 'EAST':
                        # L'EST de ma tuile actuelle doit correspondre à l'OUEST du voisin de droite
                        if config.TILE_RULES[tile][1] == config.TILE_RULES[possible_tile][3]:
                            is_valid = True
                            break               
                    elif direction == 'SOUTH':
                        # Le SUD de ma tuile actuelle doit correspondre au NORD du voisin du dessous
                        if config.TILE_RULES[tile][2] == config.TILE_RULES[possible_tile][0]:
                            is_valid = True
                            break
                    elif direction == 'WEST':
                        # L'OUEST de ma tuile actuelle doit correspondre à l'EST du voisin de gauche
                        if config.TILE_RULES[tile][3] == config.TILE_RULES[possible_tile][1]:
                            is_valid = True
                            break
                
                if is_valid:
                    valid_neighbor_tiles.append(possible_tile)
            
            # On enregistre l'ancienne entropie pour voir s'il y a eu un changement
            old_entropy = neighbor.entropy
            
            # Mise à jour du voisin
            neighbor.possible_tiles = valid_neighbor_tiles
            neighbor.entropy = len(valid_neighbor_tiles)
            
            # Renvoie True si le nombre de possibilités du voisin a diminué
            return neighbor.entropy < old_entropy
            
        return False
