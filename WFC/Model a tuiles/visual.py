TILE_VISUALS = {
    # --- MER ---
    'SEA_TILE': [
        "~~~~~~~",
        "~~ 🌊~~",
        "~~~~~~~"
    ],
    
    # --- SABLE (Transitions Eau / Terre) ---
    'SAND_TILE1': [ # N: Water, E: Sand, S: Land, W: Sand
        "~~ ~ ~~",
        "░░ ░ ░░",
        "███████"
    ],
    'SAND_TILE2': [ # N: Land, E: Sand, S: Water, W: Sand
        "███████",
        "░░ ░ ░░",
        "~~ ~ ~~"
    ],
    'SAND_TILE3': [ # N: Sand, E: Land, S: Sand, W: Water
        "~~ ░ ██",
        "~~ ░ ██",
        "~~ ░ ██"
    ],
    'SAND_TILE4': [ # N: Sand, E: Water, S: Sand, W: Land
        "██ ░ ~~",
        "██ ░ ~~",
        "██ ░ ~~"
    ],

    'SAND_TILE5': [
        "███████",
        "██ ░ ░ ",
        "██ ░ ~~"
    ],

        'SAND_TILE6': [
        "███████",
        " ░ ░ ██",
        "~~ ░ ██"
    ],

        'SAND_TILE7': [
        "~~ ░ ██",
        " ░ ░ ██",
        "███████"
    ],
        'SAND_TILE8': [
        "██ ░ ~~",
        "██ ░ ░ ",
        "███████"
    ],
    
    # --- TERRE ---
    'LAND_TILE': [
        "███████",
        "██ █ ██",
        "███████"
    ],
    
    # --- CHEMINS (Lignes droites et Virages) ---
    'PATH_TILE1': [ # N: Path, E: Land, S: Path, W: Land (Ligne verticale)
        "██ ║ ██",
        "██ ║ ██",
        "██ ║ ██"
    ],
    'PATH_TILE2': [ # N: Land, E: Path, S: Land, W: Path (Ligne horizontale)
        "███████",
        "═══════",
        "███████"
    ],
    'PATH_TILE3': [ # N: Path, E: Path, S: Land, W: Land (Virage Haut-Droite)
        "██ ║ ██",
        "██ ╚ ══",
        "███████"
    ],
    'PATH_TILE4': [ # N: Land, E: Land, S: Path, W: Path (Virage Bas-Gauche)
        "███████",
        "══ ╗ ██",
        "██ ║ ██"
    ],
    'PATH_TILE5': [ # N: Path, E: Land, S: Land, W: Path (Virage Haut-Gauche)
        "██ ║ ██",
        "══ ╝ ██",
        "███████"
    ],
    'PATH_TILE6': [ # N: Land, E: Path, S: Path, W: Land (Virage Bas-Droite)
        "███████",
        "██ ╔ ══",
        "██ ║ ██"
    ],
    
    # --- CHEMINS (Impasses / Bouts de chemin) ---
    'PATH_TILE7': [ # N: Path, E: Land, S: Land, W: Land
        "██ ║ ██",
        "██ ╩ ██",
        "███████"
    ],
    'PATH_TILE8': [ # N: Land, E: Path, S: Land, W: Land
        "███████",
        "██ ╠ ══",
        "███████"
    ],
    'PATH_TILE9': [ # N: Land, E: Land, S: Path, W: Land
        "███████",
        "██ ╦ ██",
        "██ ║ ██"
    ],
    'PATH_TILE10': [ # N: Land, E: Land, Land, W: Path
        "███████",
        "══ ╣ ██",
        "███████"
    ],
    
    # --- PORTS (Passage du Chemin à la Mer sur une plage de Sable) ---
    'PORT_TILE1': [ # N: Path, E: Sand, S: Water, W: Sand
        "░░ ║ ░░",
        "░░ ⚓░░",
        "~~ ~ ~~"
    ],
    'PORT_TILE2': [ # N: Sand, E: Path, S: Sand, W: Water
        "~~ ░ ░░",
        "~~ ⚓══",
        "~~ ░ ░░"
    ],
    'PORT_TILE3': [ # N: Water, E: Sand, S: Path, W: Sand
        "~~ ~ ~~",
        "░░ ⚓░░",
        "░░ ║ ░░"
    ],
    'PORT_TILE4': [ # N: Sand, E: Water, S: Sand, W: Path
        "░░ ░ ~~",
        "══ ⚓~~",
        "░░ ░ ~~"
    ]
}

def draw_grid(grid):
    print()
    for y in range(len(grid)):
        # Chaque tuile visuelle fait 3 lignes de haut
        for row_line in range(3):
            line_str = ""
            for x in range(len(grid[y])):
                tile = grid[y][x]
                
                # Cas 1 : La tuile n'est pas encore effondrée
                if tile.entropy != 1:
                    if row_line == 1:
                        # On affiche le nombre de tuiles possibles centré sur 7 caractères
                        nb_possibilites = len(tile.possible_tiles)
                        line_str += f"  ({nb_possibilites})  "[:7].center(7)
                    else:
                        # Lignes du haut et du bas vides pour les tuiles non effondrées
                        line_str += "       "
                        
                # Cas 2 : La tuile est effondrée (entropy == 1)
                elif len(tile.possible_tiles) == 1:
                    tile_name = tile.possible_tiles[0]
                    line_str += TILE_VISUALS[tile_name][row_line]
            print(line_str)
    print()
