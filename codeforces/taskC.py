import math

n, m = map(int, input().split())

X = [[]] * n
Y = [0] * n
for i in range(n):
    ar = list(map(int, input().split()))
    X[i] = ar[:-1]
    Y[i] = ar[-1]

q = list(map(int, input().split()))

distType = input()
kernelType = input()
windowType = input()

H = int(input())

distances = {
    'manhattan': lambda x, y: sum([abs(x[i] - y[i]) for i in range(len(x))]),
    'euclidean': lambda x, y: math.sqrt(sum([(x[i] - y[i]) ** 2 for i in range(len(x))])),
    'chebyshev': lambda x, y: max([abs(x[i] - y[i]) for i in range(len(x))]),
}

kernels = {
    'uniform': lambda x: 0.5 if abs(x) < 1 else 0,
    'triangular': lambda x: 1 - abs(x) if abs(x) < 1 else 0,
    'epanechnikov': lambda x: 3 / 4 * (1 - x ** 2) if abs(x) < 1 else 0,
    'quartic': lambda x: 15 / 16 * (1 - x ** 2) ** 2 if abs(x) < 1 else 0,
    'triweight': lambda x: 35 / 32 * (1 - x ** 2) ** 3 if abs(x) < 1 else 0,
    'tricube': lambda x: 70 / 81 * (1 - abs(x) ** 3) ** 3 if abs(x) < 1 else 0,
    'gaussian': lambda x: 1 / math.sqrt(2 * math.pi) * math.exp(-1 / 2 * x ** 2),
    'cosine': lambda x: math.pi / 4 * math.cos(math.pi / 2 * x) if abs(x) < 1 else 0,
    'logistic': lambda x: 1 / (math.exp(x) + 2 + math.exp(-x)),
    'sigmoid': lambda x: 2 / math.pi / (math.exp(x) + math.exp(-x)),
}

distance = distances[distType]
kernel = kernels[kernelType]

sortedX = sorted([distance(x, q) for x in X])

if windowType == 'variable':
    H = sortedX[H]

resY = 0
res = 0
for i in range(n):
    d = distance(X[i], q)
    t = 0
    if H == 0:
        if d == 0:
            t = 1
    else:
        t = kernel(d / H)
    res += t
    resY += t * Y[i]

if res == 0:
    for i in range(n):
        resY += Y[i]
        res += 1

result = resY / res

print(result)
