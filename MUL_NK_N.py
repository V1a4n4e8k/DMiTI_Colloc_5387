from copy import deepcopy
def MUL_NK_N(a, k):
    res = deepcopy(a)
    for i in range(k):
        res.append(0)
    return res
""" use ex
print(MUL_NK_N([1,2,3], 4))
"""