import numpy as np
import math

from functools import reduce

from collections import namedtuple
NodeParams = namedtuple("Node", "name additional frm")


def f_rlu(a, x):
    if x >= 0:
        return x
    else:
        return x * (1.0 / a)


func = {
    'var': lambda params, x: x,
    'tnh': lambda params, x: np.array(list(map(lambda z: math.tanh(z), x[0].flatten())), dtype="float64").reshape(x[0].shape),
    'rlu': lambda params, x: np.array(list(map(lambda z: f_rlu(params[0], z), x[0].flatten())), dtype="float64").reshape(x[0].shape),
    'mul': lambda params, x: x[0].dot(x[1]),
    'sum': lambda params, x: reduce(lambda p1, p2: p1 + p2, x),
    'had': lambda params, x: reduce(lambda p1, p2: p1 * p2, x),
}


def tanhder(val):
    return 1 / (math.cosh(val) ** 2)



v = []




class Node:
    def __str__(self) -> str:
        return self.name + \
               " " + " ".join(list(map(str, self.additional))) +  \
               " " + " ".join(list(map(str, self.frm)))

    def __init__(self, node):
        self.name = node.name
        self.additional = node.additional
        self.frm = node.frm
        self.num_to_activate = len(self.frm)
        self.value = None
        self.dv = None
        self.to = []
        self.dactivate_num = 0

    def activate(self):
        # print('activate', self.index)
        if self.value is None:
            args = list(map(lambda x: v[x].value, self.frm))
            # print(args)
            self.value = func[self.name](self.additional, args)
            # print(self.value)
        for _to in self.to:
            v[_to].num_to_activate -= 1
            if v[_to].num_to_activate == 0:
                v[_to].activate()

    def calc_der(self):
        if self.name == 'var':
            return
        res = []

        if self.name == 'mul':
            res = [self.dv.dot(v[self.frm[1]].value.T), v[self.frm[0]].value.T.dot(self.dv)]
        elif self.name == 'sum':
            res = [self.dv] * len(self.frm)
        elif self.name == 'rlu':
            res = np.zeros(self.dv.shape, dtype="float64")

            for i in range(self.dv.shape[0]):
                for j in range(self.dv.shape[1]):
                    res[i][j] = self.dv[i][j]
                    if self.value[i][j] < 0:
                        res[i][j] /= self.additional[0]

            res = [res]
        elif self.name == 'tnh':
            res = np.zeros(self.dv.shape, dtype="float64")

            for ii in range(self.dv.shape[0]):
                for jj in range(self.dv.shape[1]):
                    res[ii][jj] = self.dv[ii][jj] * tanhder(v[self.frm[0]].value[ii][jj])

            res = [res]
        elif self.name == 'had':
            for i in range(len(self.frm)):
                r2 = []
                for j in range(len(self.frm)):
                    if i == j:
                        r2.append(self.dv)
                    else:
                        r2.append(v[self.frm[j]].value)

                res.append(reduce(lambda p1, p2: p1 * p2, r2))

        for i in range(len(self.frm)):
            _f = self.frm[i]
            if v[_f].dv is None:
                v[_f].dv = np.zeros(self.value.shape, dtype="float64")
            v[_f].dv += res[i]
            v[_f].dactivate_num -= 1
            if v[_f].dactivate_num == 0:
                v[_f].calc_der()


n, m, k = map(int, input().split())


def to_int_vertex(ls):
    return list(map(lambda x: int(x) - 1, ls))


# считываем граф функций
for i in range(n):
    s = input().split()
    if s[0] == 'var':
        v.append(Node(NodeParams(
            name='var',
            additional=list(map(int, s[1:])),
            frm=[],
        )))
    elif s[0] == 'tnh':
        v.append(Node(NodeParams(
            name='tnh',
            additional=[],
            frm=to_int_vertex(s[1:]),
        )))
    elif s[0] == 'rlu':
        v.append(Node(NodeParams(
            name='rlu',
            additional=list(map(int, s[1:2])),
            frm=to_int_vertex(s[2:]),
        )))
    elif s[0] == 'mul':
        v.append(Node(NodeParams(
            name='mul',
            additional=[],
            frm=to_int_vertex(s[1:]),
        )))
    elif s[0] == 'sum':
        v.append(Node(NodeParams(
            name='sum',
            additional=[],
            frm=to_int_vertex(s[2:]),
        )))
    elif s[0] == 'had':
        v.append(Node(NodeParams(
            name='had',
            additional=[],
            frm=to_int_vertex(s[2:]),
        )))

# проставляем to
for i in range(n):
    for e in v[i].frm:
        v[e].to.append(i)


for i in range(n):
    v[i].dactivate_num = len(v[i].to)


# считываем входные матрицы
for cyc in range(m):
    a, b = v[cyc].additional

    mtrx = [[0]] * a

    for i in range(a):
        mtrx[i] = list(map(int, input().split()))

    v[cyc].value = np.array(mtrx, dtype="float64")


# activate
for cyc in range(m):
    v[cyc].activate()


# считываем матрицы производных
for cyc in range(n - k, n):
    a, b = v[cyc].value.shape

    mtrx = [[0]] * a

    for i in range(a):
        mtrx[i] = list(map(int, input().split()))

    v[cyc].dv = np.array(mtrx, dtype="float64")

for i in range(n - k):
    v[i].dv = np.zeros(v[i].value.shape, dtype="float64")

# calc derivative
for cyc in range(n - k, n):
    if v[cyc].dactivate_num == 0:
        v[cyc].calc_der()


def print_np_array(ar):
    for _i in range(len(ar)):
        print(" ".join(list(map(lambda v: f'{v:02f}', ar[_i]))))


# print result of activation
for cyc in range(n - k, n):
    print_np_array(v[cyc].value)

# print result of derivative
for cyc in range(m):
    print_np_array(v[cyc].dv)


