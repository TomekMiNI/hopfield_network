def HopfieldNetwork:
    Z = [] #patterns
    w = [] #wagi
    M :int #liczba elementow w warstwie posredniej
    N :int #rozmiar wejścia/neuronu

    def __init__(self, n, m)
        self.N = n
        self.M = m
        

    def corelation(x, y):
        val = 0
        for i in range(len(x)):
            val += x[i] * y[i]
        return val

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
        Z = [] * self.M
        for j in range(self.M):
            Z[j] = [inputs[j][i] for i in range(self.N)]

    #reguła Hebba 
    def updateWeights(self):
        for i in range(self.M):
            for j in range(self.M):
                w[i, j] = 1/self.N * self.corelation(Z[i], Z[j])

                

    #reguła Hebba 
    def updateWeights2(self):
        #foreach pattern
        for m in range(self.M):
            for i in range(self.N):
                for j in range(self.N):
                    w[i, j] = 1/self.N * Z[m][i] * Z[m][j]

    def updateWeights_mod1(self):
        #100???
        for u in range(100):


    def activFun(self, val):
        return self.ownSign(val)

    def ownSign(self, val):
        if val >= 0:
            return 1
        return -1

    def calculateNewZ(self):
        newZ = [] * self.M
        #foreach pattern
        for n in range(self.M):
            newZ = [] * self.N
            #foreach elem in pattern
            for i in range(self.N):
                arg = 0
                for j in range(self.N):
                    arg += w[i, j] * Z[n][i]
                newZ[n][i] = self.activFun(arg)
        Z = newZ
                

    def calculateOutput(self):
        for j in range(self.M):
            newZ = [] * self.N
            for i in range(self.N):
                


    def train(self, inputs):
        self.createPatterns2(inputs)
        #while True: #until some eps...
        for _ in range(1000):
            self.updateWeights2()
            self.calculateNewZ()
        
