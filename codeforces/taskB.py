k = int(input())

ar = [[]] * k
for i in range(k):
    ar[i] = list(map(int, input().split()))

# print(ar)
# k = 3
# ar = [[3, 1, 1], [3, 1, 1], [1, 3, 1]]


def calc_f(tp, fn, fp, tn):
    p = tp + fn
    n = fp + tn
    rec = tp
    pr = tp
    if rec != 0:
        rec = tp / p
    if rec != 0:
        pr = tp / (tp + fp)
    if pr * rec == 0:
        return 0
    # f = 2 * (pr * rec) / (pr + rec)
    beta = 1
    f = (1 + beta * beta) * (pr * rec) / (beta * beta * pr + rec)
    return f

some = []

def calc(x):
    tp, fn, fp, tn = 0, 0, 0, 0
    for i in range(k):
        for j in range(k):
            if i == x and j == x:
                tp += ar[i][j]
            elif i == x and j != x:
                fn += ar[i][j]
            elif i != x and j == x:
                fp += ar[i][j]
            else:
                tn += ar[i][j]

    some.append((tp, fn, fp, tn))
    return calc_f(tp, fn, fp, tn)


ar2 = list(map(sum, ar))
ar3 = sum(ar2)

r2 = 0
for i in range(k):
    t = calc(i)
    r2 += t * ar2[i]
    # print(t)

# micro f score ^



arr = []
for i in range(k):
    ttt2 = 0
    for j in range(k):
        ttt2 += ar[j][i]
    arr.append(ttt2)

ttt = 0
ttt1 = 0
for i in range(k):
    if ar[i][i] * ar2[i] != 0:
        ttt += ar[i][i] * ar2[i] / arr[i]
    ttt1 += ar[i][i]

ttt /= ar3
ttt1 /= ar3

tt4 = 2 * (ttt * ttt1)
if tt4 != 0:
    tt4 = 2 * (ttt * ttt1) / (ttt + ttt1)

print(tt4)
print(r2 / ar3)

# TP FN
# FP TN
#
# 3 2
# 4 6


# tp = 3
# fn = 2
# fp = 4
# tn = 6
#
# p = tp + fn
# n = fp + tn
#
# rec = tp / p
#
# pr = tp / (tp + fp)
#
# f = 2 * (pr * rec) / (pr + rec)

# print(f)
