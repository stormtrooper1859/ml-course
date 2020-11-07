n, m, k = map(int, input().split())

ar = list(map(lambda x, i: (int(x), i), input().split(), range(1, n + 1)))

ar.sort()

for i in range(k):
    print(n // k + (1 if i < n % k else 0), end=' ')
    j = i
    while j < n:
        print(ar[j][1], end=' ')
        j += k
    print()
