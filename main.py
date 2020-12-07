import Parser
import Img
from hopfield import HopfieldNetwork

vectors = Parser.read_input('SN_projekt3/animals-14x9.csv')
width = 9
height = 14


hn = HopfieldNetwork(height*width, 1)

hn.train(vectors, 2)

Z = hn.Z[0]
print(Z)
Img.vector_to_img(Z, height, width, True)