m = int(input())
n = 2 ** m

f = [0] * n

for i in range(n):
    f[i] = int(input())

n_true_before = sum(f)
is_reverse = n_true_before > 2 ** (m - 1)
rev_num = -1 if is_reverse else 1

if is_reverse:
    for i in range(n):
        f[i] = 1 - f[i]

n_true = sum(f)


if n_true == 0:
    print(1)
    print(1)
    print(' '.join(list(map(str, ([0] * m) + [-rev_num * 0.5]))))
else:
    print(2)
    print(n_true, 1)

    for i in range(n):
        if f[i] == 1:
            # print answ
            ln = []
            nm = bin(i).count('1')
            for j in range(m):
                if (2 ** j) & i:
                    ln.append(1)
                else:
                    ln.append(min(-nm, -1))
            ln.append(-nm + 0.5)

            print(' '.join(list(map(str, ln))))

    if is_reverse:
        print(' '.join(list(map(str, ([-1] * n_true) + [0.5]))))
    else:
        print(' '.join(list(map(str, ([1] * n_true) + [-0.5]))))
