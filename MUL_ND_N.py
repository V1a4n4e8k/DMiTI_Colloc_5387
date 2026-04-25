from copy import deepcopy

def MUL_ND_N(b, n):
    a = deepcopy(b)
    for i in range(len(a)):
        a[i] = a[i] * n
    move = 0
    for i in range(len(a) - 1, -1, -1):
        a[i] += move
        move = a[i] // 10
        a[i] %= 10
    if move:
        a.insert(0, move)
    return a
""" use ex
a = [1,2,3]
n = 9
MUL_NN_N(a,n)
print(a)
"""
