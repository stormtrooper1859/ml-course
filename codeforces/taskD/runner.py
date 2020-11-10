from os import listdir
from os.path import isfile, join
from taskD import solve

trainsPath = 'trains'


def getFilesFromDir(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def SMAPE(Y, Yh):
    answ = 0

    for i in range(len(Y)):
        t = abs(Y[i] - Yh[i])
        if t != 0:
            answ += t / (abs(Y[i]) + abs(Yh[i]))

    return answ / len(Y)


def readFileData(path):
    f = open(path, "r")
    m = int(f.readline())
    n_tr = int(f.readline())
    X_tr = [[]] * n_tr
    Y_tr = [0] * n_tr
    for i in range(n_tr):
        ar = list(map(int, f.readline().split()))
        X_tr[i] = ar[:-1]
        Y_tr[i] = ar[-1]
    n_ts = int(f.readline())
    X_ts = [[]] * n_ts
    Y_ts = [0] * n_ts
    for i in range(n_ts):
        ar = list(map(int, f.readline().split()))
        X_ts[i] = ar[:-1]
        Y_ts[i] = ar[-1]
    f.close()
    return n_tr, X_tr, Y_tr, n_ts, X_ts, Y_ts


def runFile(path):
    n, X, Y, nts, Xts, Yts = readFileData(join(trainsPath, path))

    coeff = solve(X, Y)

    Yh = [0] * nts

    for i in range(nts):
        for j in range(len(coeff) - 1):
            Yh[i] += coeff[j] * Xts[i][j]
        Yh[i] += coeff[-1]

    smpS = SMAPE(Yts, Yh)

    smpJ, smpB = map(float, path[:-4].split('_'))

    score = (smpB - smpS) / (smpB - smpJ)

    print('smpS', smpS)
    print('score', score)


allFiles = getFilesFromDir(trainsPath)

runFile(allFiles[0])
