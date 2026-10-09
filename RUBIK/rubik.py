class rubik:

    def __init__(self):
        size = 3
        self.state = [[[i for j in range(size)] for k in range(size)] for i in range(6)]

    #Right rotation of side n
    def rotR(self,n):
        if 0 <= n <= 5:
            #rotation of the side n
            side = self.state[n]
            self.state[n] = [[side[2][0],side[1][0],side[0][0]],[side[2][1],side[1][1],side[0][1]],[side[2][2],side[1][2],side[0][2]]]
            #rotation of the rest
            if n == 0:
                aux = [self.state[4][0][2],self.state[4][1][2],self.state[4][2][2]]
                [self.state[4][0][2],self.state[4][1][2],self.state[4][2][2]] = self.state[3][0]
                self.state[3][0] = [self.state[2][2][0],self.state[2][1][0],self.state[2][0][0]]
                [self.state[2][0][0],self.state[2][1][0],self.state[2][2][0]] = self.state[1][2]
                self.state[1][2] = aux
            if n == 1:
                aux = self.state[0][0]
                self.state[0][0] = self.state[2][0]
                self.state[2][0] = self.state[5][2][::-1]
                self.state[5][2] = self.state[4][0][::-1]
                self.state[4][0] = aux
            if n == 2:
                aux = [self.state[0][0][2],self.state[0][1][2],self.state[0][2][2]]
                self.state[0][0][2],self.state[0][1][2],self.state[0][2][2] = self.state[3][0][2],self.state[3][1][2],self.state[3][2][2]
                self.state[3][0][2],self.state[3][1][2],self.state[3][2][2] = self.state[5][0][2],self.state[5][1][2],self.state[5][2][2]
                self.state[5][0][2],self.state[5][1][2],self.state[5][2][2] = self.state[1][0][2],self.state[1][1][2],self.state[1][2][2]
                self.state[1][0][2],self.state[1][1][2],self.state[1][2][2] = aux
            if n == 3:
                aux = self.state[0][2]
                self.state[0][2] = self.state[4][2]
                self.state[4][2] = self.state[5][0][::-1]
                self.state[5][0] = self.state[2][2][::-1]
                self.state[2][2] = aux
            if n == 4:
                aux = [self.state[0][0][0],self.state[0][1][0],self.state[0][2][0]]
                self.state[0][0][0],self.state[0][1][0],self.state[0][2][0] = self.state[1][0][0],self.state[1][1][0],self.state[1][2][0]
                self.state[1][0][0],self.state[1][1][0],self.state[1][2][0] = self.state[5][0][0],self.state[5][1][0],self.state[5][2][0]
                self.state[5][0][0],self.state[5][1][0],self.state[5][2][0] = self.state[3][0][0],self.state[3][1][0],self.state[3][2][0]
                self.state[3][0][0],self.state[3][1][0],self.state[3][2][0] = aux
            if n == 5:
                aux = [self.state[4][0][0],self.state[4][1][0],self.state[4][2][0]]
                [self.state[4][2][0],self.state[4][1][0],self.state[4][0][0]] = self.state[1][0]
                self.state[1][0] = [self.state[2][0][2],self.state[2][1][2],self.state[2][2][2]]
                [self.state[2][2][2],self.state[2][1][2],self.state[2][0][2]] = self.state[3][2]
                self.state[3][2] = aux