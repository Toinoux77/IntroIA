import rubik
import visual


cube = rubik.rubik()
visual.display_node(cube.state)
print(cube.is_solvable())
cube.shuffle()
visual.display_node(cube.state)
print(cube.is_solvable())