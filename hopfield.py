import numpy as np

class HopfieldNetwork:
    Z = [] #patterns
    w = [] #wagi
    M :int #liczba elementow w warstwie posredniej
    N :int #rozmiar wejścia/neuronu

    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.w = [[]] * self.N
        for i in range(self.N):
            self.w[i] = [0] * self.N
        
    #macukow
    #input-patterns
    def createPatterns(self, inputs):
        #j patterns
        Z = [] * self.M
        for j in range(self.M):
            Z[j] = [] * self.N
            divider = inputs[j].sum()
            for i in range(self.N):
                Z[j][i] = inputs[j][i] / divider #0 or 1/divider

                
    #input-patterns
    def createPatterns2(self, inputs):
        #j patterns
        self.Z = [[]] * self.M
        for j in range(self.M):
            self.Z[j] = [inputs[j][i] for i in range(self.N)]


    #reguła Hebba 
    def updateWeights2(self):
        for i in range(self.N):
            for j in range(self.N):
                self.w[i][j] = 0
                for m in range(self.M):
                    self.w[i][j] += self.Z[m][i] * self.Z[m][j]
                self.w[i][j] /= 2
            


    def activFun(self, val):
        return self.ownSign(val)

    def ownSign(self, val):
        if val > 0:
            return 1
        return -1

    def calculateNewZ(self):
        newZ = [[]] * self.M
        #foreach pattern
        for n in range(self.M):
            newZ[n] = [0] * self.N
            #foreach elem in pattern
            for i in range(self.N):
                arg = 0
                for j in range(self.N):
                    arg += self.w[i][j] * self.Z[n][j]
                newZ[n][i] = self.activFun(arg)
        if self.Z == newZ:
            return False
        self.Z = newZ
        return True

    def calculateNewIndexZ(self):
        change = False
        newZ = [0] * self.M
        i = np.random.randint(self.N)
        #foreach pattern
        for n in range(self.M):
            #foreach elem in pattern
            arg = 0
            for j in range(self.N):
                arg += self.w[i][j] * self.Z[n][j]
            newZ[n] = self.activFun(arg)
        for k in range(self.M):
            if self.Z[k][i] != newZ[k]:
                change = True
            self.Z[k][i] = newZ[k]
        return change

    def calculateRandomZ(self):
        change = False
        newZ = [0] * self.N
        n = np.random.randint(self.M)
        #foreach elem in pattern
        for i in range(self.N):
            arg = 0
            #j can be equal i... omit or create newZ
            for j in range(self.N):
                arg += self.w[i][j] * self.Z[n][j]
            newZ[i] = self.activFun(arg)
        for k in range(self.N):
            if self.Z[n][k] != newZ[k]:
                change = True
            self.Z[n][k] = newZ[k]
        return change
        


    def updateZ(self):
        change = False
        newZ = [[]] * self.M
        for n in range(self.M):
            newZ[n] = [0] * self.N
            for i in range(self.N):
                noise = 0
                for j in range(self.N):
                    argM = 0
                    for m in range(self.M):
                        if m != n:
                            argM += self.Z[m][i] * self.Z[m][j] 
                noise = argM * self.Z[n][j]
                noise /= self.N
                if np.abs(noise) >= 1:
                    change = True
                    newZ[n][i] = self.activFun(self.Z[n][i] + noise)
        self.Z = newZ
        return change

    def updateIndexZ(self):
        change = False
        i = np.random.randint(self.N)
        newZ = [self.Z[p][i] for p in range(self.M)]
        for n in range(self.M):
            noise = 0
            for j in range(self.N):
                argM = 0
                for m in range(self.M):
                    if m != n:
                        argM += self.Z[m][i] * self.Z[m][j] 
                noise += argM * self.Z[n][j]
            noise /= 2
            if np.abs(noise) >= 1:
                change = True
                newZ[n] = self.activFun(self.Z[n][i] + noise)
        n=0
        for n in range(self.M):
            self.Z[n][i] = newZ[n]
        return change

    def updateRandomZ(self):
        change = False
        n = np.random.randint(self.M)
        newZ = [self.Z[n][i] for i in range(self.N)]
        for i in range(self.N):
            noise = 0
            for j in range(self.N):
                argM = 0
                for m in range(self.M):
                    if m != n:
                        argM += self.Z[m][i] * self.Z[m][j] 
                noise += argM * self.Z[n][j]
            noise /= 2
            if np.abs(noise) >= 1:
                change = True
                newZ[i] = self.activFun(self.Z[n][i] + noise)
        for k in range(self.N):
            self.Z[n][k] = newZ[k]
        return change

    def train(self, inputs, iter):
        self.createPatterns2(inputs)
        #while True: #until some eps...
        for _ in range(iter):
            #sign(val) = 1 if val > 0 
            self.updateWeights2()
            #choice of concrete index and change in every pattern
            #if not self.calculateNewIndexZ():
            #choice of concrete pattern and change every bit in this pattern
            #if not self.calculateRandomZ():
            if not self.calculateNewZ():
                return

            #sign(val) = 1 if val >= 0 
            #if not self.updateIndexZ():
            #if not self.updateZ():
            #if not self.updateRandomZ():
            #   print("finish")
            #       return