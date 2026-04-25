from copy import deepcopy
def MUL_NK_N(a, k):
    if k == 0:
        return [1]
    res = deepcopy(a)
    for i in range(k):
        res.append(0)
    return res
""" use ex
print(MUL_NK_N([1,2,3], 0))
"""
