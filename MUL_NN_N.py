from copy import deepcopy
from COM_NN_D import COM_NN_D
from ADD_NN_N import ADD_NN_N
from MUL_ND_N import MUL_ND_N
from MUL_NK_N import MUL_NK_N

def MUL_NN_N(a, b):
    long = []
    short = []
    if COM_NN_D(a, b) == 2:
        long = deepcopy(a)
        short = deepcopy(b)
    else:
        long = deepcopy(b)
        short = deepcopy(a)
    
    result = [0]
    
    for i in range(len(short)-1, -1, -1):
        digit = short[i]
        mul_by_digit = MUL_ND_N(long, digit)
        mul_by_pow10 = MUL_NK_N(mul_by_digit, len(short)-1-i)
        result = ADD_NN_N(result, mul_by_pow10)
    
    return result
""" use ex
print(MUL_NN_N([9,9], [9,9,9]))
"""