import csv_parser
import Img
from hopfield import HopfieldNetwork
import matplotlib as plt
import matplotlib.pyplot
import numpy as np

def calculateDiff(v1, v2):
    diff = 0 
    length = len(v1)
    for i in range(length):
        if v1[i] != v2[i]:
            diff += 1
    diff /= length
    return diff

vectors = csv_parser.read_input('SN_projekt3/large-25x25.csv')
width = 25
height = 25

countOfPatterns = 6

hn = HopfieldNetwork(height*width, countOfPatterns, False, 0.1, 1)

result = hn.train(vectors)
print("Result: ", result)
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
    axarr[i, 0].imshow(Img.vector_to_img(vectors[i], height, width, False, ))
    axarr[i, 1].imshow(Img.vector_to_img(hn.Z[i], height, width, False))
    diff = calculateDiff(vectors[i], hn.Z[i])
    plt.pyplot.sca(axarr[i, 1])
    plt.pyplot.yticks([1], [diff])

plt.pyplot.show()