from COM_NN_D import COM_NN_D
from copy import deepcopy

def ADD_NN_N(a, b):
    num1 = deepcopy(a)
    num2 = deepcopy(b)
    
    while len(num1) < len(num2):
        num1.insert(0, 0)
    while len(num2) < len(num1):
        num2.insert(0, 0)
    
    num1.insert(0, 0)
    
    for i in range(len(num1)-1, 0, -1):
        num1[i] += num2[i-1]
        
        if num1[i] >= 10:
            num1[i] -= 10
            num1[i-1] += 1
    
    while len(num1) > 1 and num1[0] == 0:
        num1.pop(0)
    
    return num1
""" use ex
print(ADD_NN_N([1,9], [9,1,9]))
"""