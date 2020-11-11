import random
import math

loss_function_name = 'linear'
mu = 0.0001
a = 1 / 5





##

# loss_functions = {
#     'logistic': lambda x: math.log(1 + math.exp(-x)) if -x < 100 else -x,
#     'logistic2': lambda x: math.log2(1 + math.exp(-x)) if -x < 100 else -x,
#     'linear': lambda x: max(-x, 0),
# }
#
# loss_function_derivatives = {
#     'logistic': lambda x: -1 / (math.exp(min(x, 300)) + 1),
#     'logistic2': lambda x: -1 / (2 ** (min(x, 300)) + 1),
#     'linear': lambda x: -1 if x < 0 else 0,
# }
#
# loss_function = loss_functions[loss_function_name]
# loss_function_derivative = loss_function_derivatives[loss_function_name]


def getInitialValue(n):
    return [(random.random() / (n / 6 + 1)) - 0.5 / (n / 6 + 1) for i in range(n)]


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
    # Q = sum([(dotProduct(w, X[i]) - Y[i]) ** 2 for i in range(n)])
    Q = sum([(dotProduct(w, X[i]) - Y[i]) ** 2 for i in range(n)])
    Qold = math.inf

    cyc = 0
    # while cyc < 10000:
    while abs(Q - Qold) >= 0.00001 and cyc < 30000:
        cyc += 1
        Qold = Q
        i = int(random.random() * n)
        e = (dotProduct(w, X[i]) - Y[i]) ** 2
        prodd = dotProduct(w, X[i]) - Y[i]


        xq = 0
        for j in range(m):
            xq += X[i][j] * (2 * X[i][j] * X[i][j] * w[j] + 2 * X[i][j] * (prodd - w[j] * X[i][j]))
        lm = (prodd / (xq) / 2) if xq != 0 else -0.0000001


        # coeff = 1 / (cyc + 2) * (dotProduct(w, X[i]) - Y[i])
        for j in range(m):
            # der = prodd * 2 * mu
            der = (2 * X[i][j] * X[i][j] * w[j] + 2 * X[i][j] * (prodd - w[j] * X[i][j]))
            # der = 2 * X[i][j] * prodd
            # der = (2 * w[j] * w[j] * X[i][j] + 2 * w[j] * (prodd - w[j] * X[i][j]))
            # der = (2 * w[j] * w[j] * (mu) + w[j] * (prodd - w[j] * X[i][j]))
            # w[j] = w[j] - abs(lm) * der
            w[j] = w[j] - lm * der
        Q = (1 - a) * Q + a * e

    # print(Q, cyc)

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
