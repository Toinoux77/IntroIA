# Configuration file for the WFC model

# This file defines the tile weights, connection rules, and grid size for the Wave Function Collapse (WFC) algorithm.

# The dictionary of tiles and their rules.

TILE_RULES = {
    # Define the connection rules for each tile type
    # TILE : [NORTH, EAST, SOUTH, WEST]
    'SEA_TILE': ['WATER','WATER','WATER','WATER'],
    'SAND_TILE1': ['WATER','WATER_LAND','LAND','WATER_LAND'],
    'SAND_TILE2': ['LAND','LAND_WATER','WATER','LAND_WATER'],
    'SAND_TILE3': ['WATER_LAND','LAND','WATER_LAND','WATER'],
    'SAND_TILE4': ['LAND_WATER','WATER','LAND_WATER','LAND'],
    'SAND_TILE5': ['LAND','LAND_WATER','LAND_WATER','LAND'],
    'SAND_TILE6': ['LAND','LAND','WATER_LAND','LAND_WATER'],
    'SAND_TILE7': ['WATER_LAND','LAND','LAND','WATER_LAND'],
    'SAND_TILE8': ['LAND_WATER','WATER_LAND','LAND','LAND'],
    'LAND_TILE': ['LAND','LAND','LAND','LAND'],
    'PATH_TILE1': ['PATH','LAND','PATH','LAND'],
    'PATH_TILE2': ['LAND','PATH','LAND','PATH'],
    'PATH_TILE3': ['PATH','PATH','LAND','LAND'],
    'PATH_TILE4': ['LAND','LAND','PATH','PATH'],
    'PATH_TILE5': ['PATH','LAND','LAND','PATH'],
    'PATH_TILE6': ['LAND','PATH','PATH','LAND'],
    'PATH_TILE7': ['PATH','LAND','LAND','LAND'],
    'PATH_TILE8': ['LAND','PATH','LAND','LAND'],
    'PATH_TILE9': ['LAND','LAND','PATH','LAND'],
    'PATH_TILE10': ['LAND','LAND','LAND','PATH'],
    'PORT_TILE1': ['PATH','LAND_WATER','WATER','LAND_WATER'],
    'PORT_TILE2': ['WATER_LAND','PATH','WATER_LAND','WATER'],
    'PORT_TILE3': ['WATER','WATER_LAND','PATH','WATER_LAND'],
    'PORT_TILE4': ['LAND_WATER','WATER','LAND_WATER','PATH'],
}

TILE_WEIGHTS = {
    # Define the weights for each tile type
    'SEA_TILE': 50,
    'SAND_TILE1': 5,
    'SAND_TILE2': 5,
    'SAND_TILE3': 5,
    'SAND_TILE4': 5,
    'SAND_TILE5': 5,
    'SAND_TILE6': 5,
    'SAND_TILE7': 5,
    'SAND_TILE8': 5,
    'LAND_TILE': 100,
    'PATH_TILE1': 10,
    'PATH_TILE2': 10,
    'PATH_TILE3': 1,
    'PATH_TILE4': 1,
    'PATH_TILE5': 1,
    'PATH_TILE6': 1,
    'PATH_TILE7': .1,
    'PATH_TILE8': .1,
    'PATH_TILE9': .1,
    'PATH_TILE10': .1,
    'PORT_TILE1': 1,
    'PORT_TILE2': 1,
    'PORT_TILE3': 1,
    'PORT_TILE4': 1,
}