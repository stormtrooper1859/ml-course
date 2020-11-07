import math

distances = {
    'manhattan': lambda x, y: sum([abs(x[i] - y[i]) for i in range(len(x))]),
    'euclidean': lambda x, y: math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))])),
    'chebyshev': lambda x, y: max([abs(x[i] - y[i]) for i in range(len(x))]),
}

v1 = [1, 2, 3, 4, 5]
v2 = [2, 3, 4, 6, 6]

v3 = [1, 1]
v4 = [4, 5]

for a, b in distances.items():
    print(a, b(v1, v2))
    print(a, b(v3, v4))
