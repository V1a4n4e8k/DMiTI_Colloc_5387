"""
P-6
Степень многочлена
"""


from copy import deepcopy

import classes as cls


def DEG_P_N(a: cls.polynom):
    f = deepcopy(a)
    
    s = str(f.deg)

    new_data = []

    for x in s:
        new_data.append(int(x))
    
    return cls.natural(new_data)


