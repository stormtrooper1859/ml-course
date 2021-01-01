k = int(input())
n = int(input())

X, Y = [], []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

def dist(v):
    a = sorted(v)
    n = len(v)
    res = 0
    for i in range(n - 1):
        res += (a[i + 1] - a[i]) * (i + 1) * (n - i - 1)
    return res

def class_dist(X, Y):
    mp = dict()

    for i in range(len(Y)):
        if mp.get(Y[i]) is None:
            mp[Y[i]] = []
        mp[Y[i]].append(X[i])
    
    res_in = 0
    res_out = dist(X)

    for k, v in mp.items():
        res_in += dist(v)

    return res_in * 2, (res_out - res_in) * 2


class_in, class_out = class_dist(X, Y)

print(class_in)
print(class_out)
