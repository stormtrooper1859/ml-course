nn = int(input())

X, Y = [], []

for i in range(nn):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def spearman(P1, P2):
    n = len(P1)

    a1 = sorted(list(range(n)), key=lambda e: P1[e])
    a2 = sorted(list(range(n)), key=lambda e: P2[e])

    ind1 = [0] * n
    ind2 = [0] * n

    for i in range(n):
        ind1[a1[i]] = i
        ind2[a2[i]] = i

    sm = 0.0

    for i in range(n):
        sm += (ind1[i] - ind2[i]) ** 2

    p = 1.0 - 6.0 * sm / (n * (n ** 2 - 1))

    return p


res = spearman(X, Y)

print(res)
