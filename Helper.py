def calculateDiff(v1, v2):
    diff = 0 
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            diff += 1