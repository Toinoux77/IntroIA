# WAVE FUNCTION COLLAPSE

# Tiles:

# Rules:
    - sea adjacent to : sea ; beach
    - beach adjacent to : sea ; land - cannot be touching only land
    - land adjacent to : beach ; moutain
    - moutain adjacent to : land

# Algebraically: 

## Facts.

(1,0,0,0) -> (1,1,0,0)
[(1,0,0,0),(1,0,0,0),(1,0,0,0),(1,0,0,0)] -> (1,0,0,0)

(0,1,0,0) -> (1,1,1,0)

(0,0,1,0) -> (0,1,1,1)

(0,0,0,1) -> (0,0,1,1)

when a tile is collapsed to (0,1,0,0)  
## Rule : 

L'erreur : On doit partir d'une tuile collapsee et decider pour celle autours