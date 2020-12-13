import csv
from typing import List
# from IPython.display import display

def read_input(path) -> List[List[int]]:
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        inputs = list()
        for row in reader:
            inp = [0] * len(row)
            for r in range(len(row)):
                if row[r] == '1':
                    inp[r] = 1
                else:
                    inp[r] = -1
            inputs.append(inp)
    return inputs




