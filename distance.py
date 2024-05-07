import math

points = [(2, 9), (5, 8), (8, 5), (9, 3)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 )

distances = []

for i in range(len(points) -1):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

print(min(distances))


