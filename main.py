import Parser
import Img
from hopfield import HopfieldNetwork
import matplotlib as plt
import matplotlib.pyplot

vectors = Parser.read_input('SN_projekt3/large-25x25.csv')
width = 25
height = 25

countOfPatterns = 6

hn = HopfieldNetwork(height*width, countOfPatterns)

hn.train(vectors, 10)

# Z = hn.Z[0]
# print(Z)
# z0 = Img.vector_to_img(Z, height, width, False)
# z1 = Img.vector_to_img(hn.Z[1], height, width, True)
# z2 = Img.vector_to_img(hn.Z[2], height, width, True)
# z3 = Img.vector_to_img(hn.Z[3], height, width, True)
# z4 = Img.vector_to_img(hn.Z[4], height, width, True)
# z5 = Img.vector_to_img(hn.Z[5], height, width, True)

f, axarr = plt.pyplot.subplots(countOfPatterns, 2)

for i in range(countOfPatterns):
    axarr[i,0].imshow(Img.vector_to_img(vectors[i], height, width, False))
    axarr[i,1].imshow(Img.vector_to_img(hn.Z[i], height, width, False)) 

plt.pyplot.show()