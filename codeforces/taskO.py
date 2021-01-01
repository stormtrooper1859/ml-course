k = int(input())
n = int(input())

X, Y = [], []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

def dispersion(X, Y):
    mp = dict()

    for i in range(len(X)):
        if mp.get(X[i]) is None:
            mp[X[i]] = []
        mp[X[i]].append(Y[i])

    ts = 0
    tcnt = 0

    for k, v in mp.items():
        tcnt += 1

        v2 = [x * x for x in v]
        v2r = sum(v2) / len(v2)
        vr = sum(v) / len(v)

        ts += (v2r - vr ** 2) * len(v)

    return ts / n

print(dispersion(X, Y))
