import rubik
import visual


cube = rubik.rubik()
print(cube.dist())
visual.display_node(cube.state)
for i in range(8):    
    cube.shuffle(i*10)
    print(cube.dist())
    visual.display_node(cube.state)