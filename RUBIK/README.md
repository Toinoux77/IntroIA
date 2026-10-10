# RUBIK'S CUBE SOLVING WITH A*

# FIRST
## We need a CUBE (6 sides, 9 tiles) - this is a flattened cube
            Top
            [1, 1, 1]
            [1, 1, 1]
            [1, 1, 1]
Left        Front       Right
[3, 3, 3]   [0, 0, 0]   [2, 2, 2]
[3, 3, 3]   [0, 0, 0]   [2, 2, 2]
[3, 3, 3]   [0, 0, 0]   [2, 2, 2]
            Bottom
            [4, 4, 4]
            [4, 4, 4]
            [4, 4, 4]
            Back
            [5, 5, 5]
            [5, 5, 5]
            [5, 5, 5]
Each side can turn clockwise or anti-clockwise (that's 12 vertex per node)

## We also need to make sure our CUBE IS SOLVABLE which only takes some rules
It's physically impossible for a cube to change it's angles, centers and edges so we just need to verify their presence

        expected_sides = {0, 1, 2, 3, 4, 5}

        expected_edges = {
            frozenset((0,1)), frozenset((0,2)), frozenset((0,3)), frozenset((0,4)),
            frozenset((1,2)), frozenset((1,3)), frozenset((2,4)), frozenset((3,4)),
            frozenset((1,5)), frozenset((4,5)), frozenset((3,5)), frozenset((2,5))
        }

        expected_angles = {
            frozenset((0,1,2)), frozenset((0,1,3)), frozenset((0,2,4)), frozenset((0,3,4)),
            frozenset((5,1,3)), frozenset((5,1,2)), frozenset((5,4,3)), frozenset((5,4,2))
        }

## Now we can generate a shuffled cube by randomly making moves
            [3, 0, 0]
            [5, 1, 4]
            [5, 5, 2]

[1, 1, 4]   [3, 4, 4]   [5, 0, 4]
[2, 3, 4]   [2, 0, 1]   [0, 2, 0]
[2, 1, 2]   [0, 4, 3]   [5, 3, 0]

            [1, 3, 1]
            [2, 4, 1]
            [1, 5, 3]

            [5, 3, 4]
            [5, 5, 3]
            [0, 2, 2]
True #This cube is solvable.

# To implement A* we need a HEURISTIC that can be the "entropy" of the cube state or the distance from the solved cube
## A solvable cube can always be solved in less than 20 moves

Before searching for the best solution with A* we need to know the solution, so we are taking and reducing the random path to get the shortest path