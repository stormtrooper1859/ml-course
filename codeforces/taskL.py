import math

n = int(input())

X, Y = [], []

for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def pirson(P1, P2):
    avg1 = sum(P1) / len(P1)
    avg2 = sum(P2) / len(P2)

    num = 0
    den1 = 0
    den2 = 0

    for i in range(len(P1)):
        num += (P1[i] - avg1) * (P2[i] - avg2)
        den1 += (P1[i] - avg1) ** 2
        den2 += (P2[i] - avg2) ** 2

    if num == 0:
        return 0

    return num / math.sqrt(den1 * den2)


res = pirson(X, Y)

print(res)
