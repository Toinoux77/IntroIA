def display_node(cube):
    print()
    for i in range(3):
        print("           ",cube[1][i])
    print()
    for j in range(3):
        print(cube[4][j]," ",cube[0][j]," ",cube[2][j])
    print()
    for k in range(3):
        print("           ",cube[3][k])
    print()
    for l in range(3):
        print("           ",cube[5][l])
