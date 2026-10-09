import rubik
import visual
import time

cube = rubik.rubik()
for i in range(6):
    cube.rotR(i)
visual.display_node(cube.state)