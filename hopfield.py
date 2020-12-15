import numpy as np
import sys

class HopfieldNetwork:
    Z = [] #patterns
    w = [] #wagi
    M: int #liczba elementow w warstwie posredniej
    N: int #rozmiar wejścia/neuronu
    prevZ = []
    V = []  # Oja
    use_oja: bool
    oji_iters: int
    eta: float

    def __init__(self, n, m, use_oja, eta, oji_iters):
        self.N = n
        self.M = m
        self.w = [[] for _ in range(self.N)]
        self.E = sys.maxsize
        self.use_oja = use_oja
        if self.use_oja:
            self.eta = eta
            self.V = [0 for _ in range(self.N)]
            self.oji_iters = oji_iters

        for i in range(self.N):
            self.w[i] = [0 for _ in range(self.N)]
                
    #input-patterns
    def createPatterns(self, inputs):
        #j patterns
        self.Z = [[]] * self.M
        for j in range(self.M):
            self.Z[j] = [inputs[j][i] for i in range(self.N)]

        self.createWeightsHebb()
        if self.use_oja:
            for j in range(self.N):
                vj = 0
                for i in range(self.N):
                    ksij = 0
                    for m in range(self.M):
                        ksij += self.Z[m][j]
                    vj += self.w[i][j] * ksij
                self.V[j] = vj

            for i in range(self.oji_iters):
                self.updateOjaWeights()

    #reguła Hebba
    def createWeightsHebb(self):
        for i in range(self.N):
            for j in range(self.N):
                self.w[i][j] = 0
                for m in range(self.M):
                    self.w[i][j] += self.Z[m][i] * self.Z[m][j]
                self.w[i][j] /= self.N
            


    def activFun(self, val):
        return self.ownSign(val)

    def ownSign(self, val):
        if val >= 0:
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

        isNewZ = self.isNew(newZ)
        if isNewZ == 0:
            self.prevZ.append(self.Z)
            self.Z = newZ
            return isNewZ
        
        return isNewZ


    def updateOjaWeights(self):
        for i in range(self.N):
            ksii = 0
            for m in range(self.M):
                ksii += self.Z[m][i]

            for j in range(self.N):
                self.w[i][j] += self.eta * self.V[j] * (ksii - self.V[j] * self.w[i][j])

    def isNew(self, newZ):
        #0 means continue calculations
        #1 means stable state
        #-1 means loop  
        if len(self.prevZ) == 0:
            return 0

        for i in reversed(range(len(self.prevZ))):    
            isSame = True
            for m in range(self.M):
                for x in range(self.N):
                    if self.prevZ[i][m][x] != newZ[m][x]:
                        isSame = False
                        break

                if not isSame:
                    break
            if isSame:
                #stable
                if i == len(self.prevZ) - 1:
                    return 1
                #loop
                return -1

        return 0

    def train(self, inputs):
        self.createPatterns(inputs)
        result = 0
        while result == 0:
            result = self.calculateNewZ()  
        return result

    def test(self, input):
        self.M = 1
        self.Z = [input]
        result = 0
        while result == 0:
            result = self.calculateNewZ() 
        return result