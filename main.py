import csv_parser
import Img
from hopfield import HopfieldNetwork
import matplotlib as plt
import matplotlib.pyplot
import numpy as np
import PngReader

def calculateDiff(v1, v2):
    diff = 0 
    length = len(v1)
    for i in range(length):
        if v1[i] != v2[i]:
            diff += 1
    diff /= length
    return diff

countOfPatterns = 2
size = 100
#vectors = csv_parser.read_input('SN_projekt3/animals-14x9.csv')
vectors = PngReader.getSomeBitmaps(countOfPatterns, 'pokemon' + str(size))
width = size
height = size


hn = HopfieldNetwork(height*width, countOfPatterns, False, 0.1, 1)

result = hn.train(vectors)
print("Result: ", result)
f, axarr = plt.pyplot.subplots(countOfPatterns, 2)

for i in range(countOfPatterns):
    axarr[i, 0].imshow(Img.vector_to_img(vectors[i], height, width, False, ))
    axarr[i, 1].imshow(Img.vector_to_img(hn.Z[i], height, width, False))
    diff = calculateDiff(vectors[i], hn.Z[i])
    plt.pyplot.sca(axarr[i, 1])
    plt.pyplot.yticks([1], ["%.2f"%diff])
    plt.pyplot.xticks([1], [""])
    plt.pyplot.sca(axarr[i, 0])
    plt.pyplot.yticks([1], [""])
    plt.pyplot.xticks([1], [""])

plt.pyplot.sca(axarr[countOfPatterns - 1, 0])
plt.pyplot.xticks([1], ["input"])
plt.pyplot.sca(axarr[countOfPatterns - 1, 1])
plt.pyplot.xticks([1], ["output"])
plt.pyplot.show()