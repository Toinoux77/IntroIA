import random
import time

class rubik:

    def __init__(self):
        size = 3
        self.state = [[[i for j in range(size)] for k in range(size)] for i in range(6)]

    #Right rotation of side n
    def rotR(self,n):
        if 0 <= n <= 5:
            #rotation of the side n
            side = self.state[n]
            self.state[n] = [
                [side[2][0],side[1][0],side[0][0]],
                [side[2][1],side[1][1],side[0][1]],
                [side[2][2],side[1][2],side[0][2]]]
            #rotation of the adjacent stickers
            if n == 0:
                aux = [self.state[3][2][2],self.state[3][1][2],self.state[3][0][2]]
                [self.state[3][0][2],self.state[3][1][2],self.state[3][2][2]] = self.state[4][0]
                self.state[4][0] = [self.state[2][2][0],self.state[2][1][0],self.state[2][0][0]]
                [self.state[2][0][0],self.state[2][1][0],self.state[2][2][0]] = self.state[1][2]
                self.state[1][2] = aux
            if n == 1:
                aux = self.state[0][0]
                self.state[0][0] = self.state[2][0]
                self.state[2][0] = self.state[5][2][::-1]
                self.state[5][2] = self.state[3][0][::-1]
                self.state[3][0] = aux
            if n == 2:
                aux = [self.state[0][0][2],self.state[0][1][2],self.state[0][2][2]]
                self.state[0][0][2],self.state[0][1][2],self.state[0][2][2] = self.state[4][0][2],self.state[4][1][2],self.state[4][2][2]
                self.state[4][0][2],self.state[4][1][2],self.state[4][2][2] = self.state[5][0][2],self.state[5][1][2],self.state[5][2][2]
                self.state[5][0][2],self.state[5][1][2],self.state[5][2][2] = self.state[1][0][2],self.state[1][1][2],self.state[1][2][2]
                self.state[1][0][2],self.state[1][1][2],self.state[1][2][2] = aux
            if n == 4:
                aux = self.state[0][2]
                self.state[0][2] = self.state[3][2]
                self.state[3][2] = self.state[5][0][::-1]
                self.state[5][0] = self.state[2][2][::-1]
                self.state[2][2] = aux
            if n == 3:
                aux = [self.state[0][0][0],self.state[0][1][0],self.state[0][2][0]]
                self.state[0][0][0],self.state[0][1][0],self.state[0][2][0] = self.state[1][0][0],self.state[1][1][0],self.state[1][2][0]
                self.state[1][0][0],self.state[1][1][0],self.state[1][2][0] = self.state[5][0][0],self.state[5][1][0],self.state[5][2][0]
                self.state[5][0][0],self.state[5][1][0],self.state[5][2][0] = self.state[4][0][0],self.state[4][1][0],self.state[4][2][0]
                self.state[4][0][0],self.state[4][1][0],self.state[4][2][0] = aux
            if n == 5:
                aux = [self.state[3][0][0],self.state[3][1][0],self.state[3][2][0]]
                [self.state[3][2][0],self.state[3][1][0],self.state[3][0][0]] = self.state[1][0]
                self.state[1][0] = [self.state[2][0][2],self.state[2][1][2],self.state[2][2][2]]
                [self.state[2][2][2],self.state[2][1][2],self.state[2][0][2]] = self.state[4][2]
                self.state[4][2] = aux

        # Left rotation of side n (Counter-clockwise)
    def rotL(self, n):
        if 0 <= n <= 5:
            # 1. Counter-clockwise rotation of the face n itself
            side = self.state[n]
            self.state[n] = [
                [side[0][2], side[1][2], side[2][2]],
                [side[0][1], side[1][1], side[2][1]],
                [side[0][0], side[1][0], side[2][0]]
            ]
            
            # 2. Counter-clockwise rotation of the adjacent stickers
            if n == 0:
                aux = [self.state[3][0][2], self.state[3][1][2], self.state[3][2][2]]
                [self.state[3][2][2], self.state[3][1][2], self.state[3][0][2]] = self.state[1][2]
                self.state[1][2] = [self.state[2][0][0], self.state[2][1][0], self.state[2][2][0]]
                [self.state[2][2][0], self.state[2][1][0], self.state[2][0][0]] = self.state[4][0]
                self.state[4][0] = aux
                
            elif n == 1:
                aux = list(self.state[0][0])
                self.state[0][0] = list(self.state[3][0])
                self.state[3][0] = self.state[5][2][::-1]
                self.state[5][2] = self.state[2][0][::-1]
                self.state[2][0] = aux
                
            elif n == 2:
                aux = [self.state[0][0][2], self.state[0][1][2], self.state[0][2][2]]
                self.state[0][0][2], self.state[0][1][2], self.state[0][2][2] = self.state[1][0][2], self.state[1][1][2], self.state[1][2][2]
                self.state[1][0][2], self.state[1][1][2], self.state[1][2][2] = self.state[5][0][2], self.state[5][1][2], self.state[5][2][2]
                self.state[5][0][2], self.state[5][1][2], self.state[5][2][2] = self.state[4][0][2], self.state[4][1][2], self.state[4][2][2]
                self.state[4][0][2], self.state[4][1][2], self.state[4][2][2] = aux
                
            elif n == 4:
                aux = list(self.state[0][2])
                self.state[0][2] = list(self.state[2][2])
                self.state[2][2] = self.state[5][0][::-1]
                self.state[5][0] = self.state[3][2][::-1]
                self.state[3][2] = aux
                
            elif n == 3:
                aux = [self.state[0][0][0], self.state[0][1][0], self.state[0][2][0]]
                self.state[0][0][0], self.state[0][1][0], self.state[0][2][0] = self.state[4][0][0], self.state[4][1][0], self.state[4][2][0]
                self.state[4][0][0], self.state[4][1][0], self.state[4][2][0] = self.state[5][0][0], self.state[5][1][0], self.state[5][2][0]
                self.state[5][0][0], self.state[5][1][0], self.state[5][2][0] = self.state[1][0][0], self.state[1][1][0], self.state[1][2][0]
                self.state[1][0][0], self.state[1][1][0], self.state[1][2][0] = aux
                
            elif n == 5:
                aux = [self.state[3][2][0], self.state[3][1][0], self.state[3][0][0]]
                [self.state[3][0][0], self.state[3][1][0], self.state[3][2][0]] = self.state[4][2]
                self.state[4][2] = [self.state[2][2][2], self.state[2][1][2], self.state[2][0][2]]
                [self.state[2][0][2], self.state[2][1][2], self.state[2][2][2]] = self.state[1][0]
                self.state[1][0] = aux

    def sides(self):
        return {self.state[0][1][1],self.state[1][1][1],self.state[2][1][1],self.state[3][1][1],self.state[4][1][1],self.state[5][1][1]}
    
    def edges(self):
        return {
            frozenset((self.state[0][0][1],self.state[1][2][1])),frozenset((self.state[0][1][2],self.state[2][1][0])),frozenset((self.state[0][1][0],self.state[3][1][2])),
            frozenset((self.state[0][2][1],self.state[4][0][1])),frozenset((self.state[1][1][2],self.state[2][0][1])),frozenset((self.state[1][1][0],self.state[3][0][1])),
            frozenset((self.state[2][2][1],self.state[4][1][2])),frozenset((self.state[3][2][1],self.state[4][1][0])),frozenset((self.state[1][0][1],self.state[5][2][1])),
            frozenset((self.state[4][2][1],self.state[5][0][1])),frozenset((self.state[3][1][0],self.state[5][1][0])),frozenset((self.state[2][1][2],self.state[5][1][2]))}
    
    def angles(self):
        return {
            frozenset((self.state[0][0][2], self.state[1][2][2], self.state[2][0][0])),
            frozenset((self.state[0][0][0], self.state[1][2][0], self.state[3][0][2])),
            frozenset((self.state[0][2][2], self.state[2][2][0], self.state[4][0][2])),
            frozenset((self.state[0][2][0], self.state[3][2][2], self.state[4][0][0])),
            frozenset((self.state[5][2][0], self.state[1][0][0], self.state[3][0][0])),
            frozenset((self.state[5][2][2], self.state[1][0][2], self.state[2][0][2])),
            frozenset((self.state[5][0][0], self.state[4][2][0], self.state[3][2][0])),
            frozenset((self.state[5][0][2], self.state[4][2][2], self.state[2][2][2]))
        }

    def is_solvable(self):
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

        # 1. Vérification des faces (sides)
        current_sides = self.sides()
        if current_sides != expected_sides:
            print("--- ERREUR : SIDES (Centres/Faces) ---")
            print("En trop :", current_sides.difference(expected_sides))
            print("Manquants :", expected_sides.difference(current_sides))
            return False

        # 2. Vérification des arêtes (edges)
        current_edges = self.edges()
        if current_edges != expected_edges:
            print("--- ERREUR : EDGES (Arêtes) ---")
            print("En trop :", current_edges.difference(expected_edges))
            print("Manquantes :", expected_edges.difference(current_edges))
            return False

        # 3. Vérification des coins (angles)
        current_angles = self.angles()
        if current_angles != expected_angles:
            print("--- ERREUR : ANGLES (Coins) ---")
            print("En trop :", current_angles.difference(expected_angles))
            print("Manquants :", expected_angles.difference(current_angles))
            return False

        return True

    def shuffle(self):
        path = []
        t1 = time.time()
        for i in range(100):
            side = random.randint(0,5)
            dir = random.randint(0,1)
            if dir == 0:
                self.rotR(side)
                if not self.is_solvable():
                    print(i)
                    print("dir=",dir," side=",side)
                    break
                path.append((dir,side))
            else:
                self.rotL(side)
                if not self.is_solvable():
                    print(i)
                    print("dir=",dir," side=",side)
                    break
                path.append((dir,side))
        print(time.time()-t1)