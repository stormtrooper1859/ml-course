import math
from collections import namedtuple
TreeState = namedtuple("TreeState", "vertex depth")

m, k, max_depth = map(int, input().split())
n = int(input())

X = [([], 1)] * n

for i in range(n):
    l = list(map(int, input().split()))
    X[i] = (l[:-1], l[-1] - 1)



special_step = False
if m * n * 2 ** max_depth >= 1.5e6:
    special_step = True

def class_count(U):
    cn = [0] * k
    for (_, c) in U:
        cn[c] += 1
    return cn

def stop_criterion(U, tree_state: TreeState):
    if tree_state.depth == max_depth:
        return True

    cn = class_count(U)
    mcn = max(cn)
    lcn = len(U)
    if mcn >= lcn - 1 and mcn / lcn >= 0.75:
        return True

    return False


def create_leaf(U, tree_state: TreeState):
    cn = class_count(U)
    cl = cn.index(max(cn))
    tree_state.vertex.append((cl,))
    return len(tree_state.vertex) - 1


def gan(U):
    clu = class_count(U)
    lu = len(U)

    rz = 0
    for cl in clu:
        rz += cl * (1 - (cl / lu) ** 2)
    return rz / lu


def gain(U1, U2):
    lu1 = len(U1)
    lu2 = len(U2)
    lu = lu1 + lu2

    g1 = gan(U1)
    g2 = gan(U2)

    rz = (lu1 * g1 + lu2 * g2) / lu

    return -rz


def split_by(U, f):
    (ind, val) = f
    u1 = []
    u2 = []
    for x in U:
        if x[0][ind] < val:
            u1.append(x)
        else:
            u2.append(x)

    return u1, u2


def choose_function(U):
    #calc avg
    av = [0] * m
    mx = [-math.inf] * m
    mn = [math.inf] * m
    for (p, _) in U:
        for i in range(m):
            av[i] += p[i]
            mx[i] = max(mx[i], p[i])
            mn[i] = min(mn[i], p[i])

    lu = len(U)

    for i in range(m):
        av[i] /= lu

    max_index = -1
    max_index_value = -1
    max_index_gain = -math.inf

    gu = gan(U)

    step = 1
    if special_step:
        step = max(math.floor(math.log2(lu + 1) - 1), 1)

    for i in range(m):
        U.sort(key=lambda x: x[0][i])


        # j = (lu - 1) // 2
        for j in range(1, lu - 1, step):
            u1 = U[:j]
            u2 = U[j:]
            gn = gain(u1, u2)
            if gn > max_index_gain:
                max_index = i
                max_index_gain = gn
                max_index_value = (U[j - 1][0][i] + U[j][0][i]) / 2

    # if gu - max_index_gain < 0.01:
    #     return 0, mn[0]

    return max_index, max_index_value


def tree_growing(U, tree_state: TreeState):
    if stop_criterion(U, tree_state):
        return create_leaf(U, tree_state)

    f = choose_function(U)
    (U1, U2) = split_by(U, f)

    if len(U1) == 0:
        return create_leaf(U, tree_state)
    if len(U2) == 0:
        return create_leaf(U, tree_state)

    tree_state.vertex.append((f[0], f[1], -1, -1))
    ind = len(tree_state.vertex) - 1

    nts = TreeState(tree_state.vertex, tree_state.depth + 1)
    v1 = tree_growing(U1, nts)
    v2 = tree_growing(U2, nts)
    # tree_state.depth -= 1
    tree_state.vertex[ind] = (f[0], f[1], v1, v2)

    return ind


treeState = TreeState(vertex=[], depth=0)
tree_growing(X, treeState)


print(len(treeState.vertex))
for v in treeState.vertex:
    if len(v) == 4:
        print(f'Q {v[0] + 1} {v[1]} {v[2] + 1} {v[3] + 1}')
    else:
        print(f'C {v[0] + 1}')


# from sklearn.tree import DecisionTreeClassifier
#
# tree1 = DecisionTreeClassifier()
# X1 = list(map(lambda x: x[0], X))
# Y1 = list(map(lambda x: x[1], X))
# print(X1)
# print(Y1)
# tree1.fit(X1, Y1)
#
# print(tree1.predict([[-1, 7]]))


