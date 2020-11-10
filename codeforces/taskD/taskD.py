import random
import math

loss_function_name = 'linear'
mu = 0.5
a = 0.5

##

loss_functions = {
    'logistic': lambda x: math.log(1 + math.exp(-x)) if -x < 100 else -x,
    'logistic2': lambda x: math.log2(1 + math.exp(-x)) if -x < 100 else -x,
    'linear': lambda x: max(-x, 0),
}

loss_function_derivatives = {
    'logistic': lambda x: -1 / (math.exp(min(x, 300)) + 1),
    'logistic2': lambda x: -1 / (2 ** (min(x, 300)) + 1),
    'linear': lambda x: -1 if x < 0 else 0,
}

loss_function = loss_functions[loss_function_name]
loss_function_derivative = loss_function_derivatives[loss_function_name]


def getInitialValue(n):
    return [(random.random() / n) - 0.5 / n for i in range(n)]


def dotProduct(v1, v2):
    return sum(p * q for p, q in zip(v1, v2))


def solve(X, Y):
    n = len(X)
    for x in X:
        x.append(1)

    m = len(X[0])

    w = getInitialValue(m)
    # w = [0] * m
    # Q = sum([loss_function(dotProduct(w, X[i]) * Y[i]) for i in range(n)])
    Q = sum([loss_function(dotProduct(w, X[i]) * Y[i]) for i in range(n)])
    Qold = math.inf

    cyc = 0
    # while cyc < 10000:
    while abs(Q - Qold) >= 0.00001 and cyc < 10000:
        cyc += 1
        Qold = Q
        i = int(random.random() * n)
        e = loss_function(dotProduct(w, X[i]) * Y[i])
        coeff = mu * loss_function_derivative(dotProduct(w, X[i]) * Y[i]) * Y[i]
        for j in range(m):
            w[j] -= coeff * X[i][j]
        Q = (1 - a) * Q + a * e

    print(Q, cyc)

    return w


def main():
    n, m = map(int, input().split())

    X = [[]] * n
    Y = [0] * n
    for i in range(n):
        ar = list(map(int, input().split()))
        X[i] = ar[:-1]
        Y[i] = ar[-1]

    sol = solve(X, Y)

    print(' '.join(map(str, sol)))

if __name__ == "__main__":
    main()
