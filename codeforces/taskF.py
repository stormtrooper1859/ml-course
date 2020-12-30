import math

k = int(input())
lam = list(map(int, input().split()))
a = int(input())
n = int(input())

class_count = [0] * k
mWordClass = dict()

for i in range(n):
    s = input().split()
    c = int(s[0]) - 1
    class_count[c] += 1
    l = int(s[1])
    ws = set(s[2:])
    for w in ws:
        if mWordClass.get(w) is None:
            mWordClass[w] = [0] * k
        mWordClass[w][c] += 1


m = int(input())

precalc = [0.0] * k

for i in range(k):
    if class_count[i] != 0:
        precalc[i] = math.log(1.0 * class_count[i] * lam[i] / n)

for w in set(mWordClass.keys()):
    st = mWordClass[w]
    for i in range(k):
        if class_count[i] != 0:
            precalc[i] += math.log(1 - (st[i] + a) / (class_count[i] + 2 * a))

for _cyc in range(m):
    s = input().split()
    l = int(s[0])
    ws = set(s[1:])

    cr = precalc.copy()

    for w in ws:
        for i in range(k):
            if class_count[i] != 0:
                if mWordClass.get(w) is not None:
                    st = mWordClass[w]
                    pr = (st[i] + a) / (class_count[i] + 2 * a)
                    cr[i] += math.log(pr) - math.log(1 - pr)

    mx = max(cr)
    cr = list(map(lambda x: x - mx, cr))

    for i in range(k):
        if class_count[i] != 0:
            cr[i] = math.exp(cr[i])

    sm = sum(cr)
    cr = list(map(lambda x: x / sm, cr))
    print(' '.join(map(str, cr)))

