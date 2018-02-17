import math
import numpy as np
def eudis(v1, v2):
    dist = [(a - b)**2 for a, b in zip(v1, v2)]
    dist = math.sqrt(sum(dist))
    return dist

number_of_cases = int(input())

points = []
for i in range(0,number_of_cases):
    point_input = input().split()
    points.append((int(point_input[0]),int(point_input[1])))
longest = 0
for i in range(0, number_of_cases):
    for j in range(0, number_of_cases):
        dist = eudis(points[i], points[j])
        if dist > longest:
            longest = dist
print(longest)
