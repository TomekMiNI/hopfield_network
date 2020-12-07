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
        self.Z = [[]] * self.M
        for j in range(self.M):
            rr = range(self.N)
            self.Z[j] = [inputs[j][i] for i in range(self.N)]

    #reguła Hebba 
    def updateWeights(self):
        for i in range(self.M):
            for j in range(self.M):
                self.w[i, j] = 1/self.N * self.corelation(self.Z[i], self.Z[j])

                

    #reguła Hebba 
    def updateWeights2(self):
        #foreach pattern
        for m in range(self.M):
            for i in range(self.N):
                for j in range(self.N):
                    self.w[i][j] = 1/self.N * self.Z[m][i] * self.Z[m][j]


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
                    arg += self.w[i][j] * self.Z[n][i]
                newZ[n][i] = self.activFun(arg)
        self.Z = newZ


    def train(self, inputs, iter):
        self.createPatterns2(inputs)
        #while True: #until some eps...
        for _ in range(iter):
            self.updateWeights2()
            self.calculateNewZ()
        
