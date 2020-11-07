import math

kernels = {
    'uniform': lambda x: 0.5 if abs(x) <= 1 else 0,
    'triangular': lambda x: 1 - abs(x) if abs(x) <= 1 else 0,
    'epanechnikov': lambda x: 3 / 4 * (1 - x ** 2) if abs(x) <= 1 else 0,
    'quartic': lambda x: 15 / 16 * (1 - x ** 2) ** 2 if abs(x) <= 1 else 0,
    'triweight': lambda x: 35 / 32 * (1 - x ** 2) ** 3 if abs(x) <= 1 else 0,
    'tricube': lambda x: 70 / 81 * (1 - abs(x) ** 3) ** 3 if abs(x) <= 1 else 0,
    'gaussian': lambda x: 1 / math.sqrt(2 * math.pi) * math.exp(-1 / 2 * x ** 2),
    'cosine': lambda x: math.pi / 4 * math.cos(math.pi / 2 * x) if abs(x) <= 1 else 0,
    'logistic': lambda x: 1 / (math.exp(x) + 2 + math.exp(-x)),
    'sigmoid': lambda x: 2 / math.pi / (math.exp(x) + math.exp(-x)),
}

v1 = [0.1, 0.2, 0.25, 1 / 3, 0.5, 1, 1.5]

for a, b in kernels.items():
    for i in v1:
        print(a, b(i))
