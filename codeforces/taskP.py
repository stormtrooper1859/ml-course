k1, k2 = map(int, input().split())
n = int(input())

X, Y = [], []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def xi_square(X, Y):
    mpXY = dict()
    mpX = dict()
    mpY = dict()

    for i in range(len(X)):
        if mpX.get(X[i]) is None:
            mpX[X[i]] = 0
        mpX[X[i]] += 1
        if mpY.get(Y[i]) is None:
            mpY[Y[i]] = 0
        mpY[Y[i]] += 1
        if mpXY.get((X[i], Y[i])) is None:
            mpXY[(X[i], Y[i])] = 0
        mpXY[(X[i], Y[i])] += 1

    res = -1.0

    for k, v in mpXY.items():
        res += v ** 2 / (mpX[k[0]] * mpY[k[1]])

    return len(X) * res

print(xi_square(X, Y))
