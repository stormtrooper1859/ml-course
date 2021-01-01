import math

kx, ky = map(int, input().split())
n = int(input())

X, Y = [], []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

def entropy(X, Y):
    mp = dict()
    n = len(X)

    for i in range(n):
        if mp.get(X[i]) is None:
            mp[X[i]] = []
        mp[X[i]].append(Y[i])

    res = 0

    for k, v in mp.items():
        nc = len(v)

        cm = dict()
        for i in range(nc):
            if cm.get(v[i]) is None:
                cm[v[i]] = 0
            cm[v[i]] += 1

        cr = 0

        for kc, vc in cm.items():
            cr += vc / nc * math.log(vc / nc)

        res += nc / n * cr

    return -res

print(entropy(X, Y))
