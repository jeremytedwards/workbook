# coding=utf-8

# N for neighbors, the following is a WEIGHTED GRAPH where each edge has a value attached
# representing the weight of that path
#

a, b, c, d, e, f, g, h = range(8)

Nwg = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
    {c: 4, e: 3},                    # b
    {d: 8},                          # c
    {e: 7},                          # d
    {f: 5},                          # e
    {c: 2, g: 2, h: 2},              # f
    {f: 1, h: 6},                    # g
    {f: 9, g: 8}                     # h
]


# Dictionary with ADJACENCY SETS
#

Nas = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

# ADJACENCY MATRICES
# ( assumes nodes are numbered a=1, b=2, ...)
# - implemented with nested lists
# - 1 for true and 0 for false where node is neighbor of.

#    a, b, c, d, e, f, g, h

Nam = [
    [0, 1, 1, 1, 1, 1, 0, 0],  # a
    [0, 0, 1, 0, 1, 0, 0, 0],  # b
    [0, 0, 0, 1, 0, 0, 0, 0],  # c
    [0, 0, 0, 0, 1, 0, 0, 0],  # d
    [0, 0, 0, 0, 0, 1, 0, 0],  # e
    [0, 0, 1, 0, 0, 0, 1, 1],  # f
    [0, 0, 0, 0, 0, 1, 0, 1],  # g
    [0, 0, 0, 0, 0, 1, 1, 0]   # h
]

# WEIGHTED ADJACENCY MATRICES
# sys.maxint is not guaranteed to be the greatest possible value so we
# use infinity = float('inf')
#
# -1 could be used if your weights are non-negative
# or None which would be a 'illegal weight'
# 0 is used for self, since link to self has 0 weight
#
# >>> W[a][b] < inf
# True
# >>> W[c][e] < inf
# False
# >>> sum(1 for w in W[a] if w < inf) - 1
# 5

inf = float('inf')

W = [
    [0, 2, 1, 3, 9, 4, inf, inf],          # a
    [inf, 0, 4, inf, 3, inf, inf, inf],    # b
    [inf, inf, 0, 8, inf, inf, inf, inf],  # c
    [inf, inf, inf, 0, 7, inf, inf, inf],  # d
    [inf, inf, inf, inf, 0, 5, inf, inf],  # e
    [inf, inf, 2, inf, inf, 0, 2, 2],      # f
    [inf, inf, inf, inf, inf, 1, 0, 6],    # g
    [inf, inf, inf, inf, inf, 9, 8, 0]     # h
]


# empty NumPy array, 10 x 10 of zeros

# import numpy as np
# N = np.zeros([10,10])

Nnp = [[0]*10 for i in range(10)]
