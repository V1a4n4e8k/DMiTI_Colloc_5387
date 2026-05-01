"""
P-7
Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
"""


from copy import deepcopy

import classes as cls

#from ABS_Z_Z import ABS_Z_Z
#from TRANS_Z_N import TRANS_Z_N
from LCM_NN_N import LCM_NN_N
from GCF_NN_N import GCF_NN_N
#from TRANS_N_Z import TRANS_N_Z
#from DIV_ZZ_Z import DIV_ZZ_Z


def FAC_P_Q(a: cls.polynom):
    f = deepcopy(a)

    com_gcf = GCF_NN_N(f.coef[0].denominator, f.coef[1].denominator)

    i = 2
    while i < len(f.coef):
        com_gcf = GCF_NN_N(com_gcf, f.coef[1].denominator)
        i += 1
    
    com_lcm = LCM_NN_N(f.coef[0].numerator.data, f.coef[1].numerator.data)

    i = 2
    while i < len(f.coef):
        com_lcm = LCM_NN_N(com_lcm, f.coef[i].numerator.data)
        i += 1

    output = cls.rational(cls.integer(0, com_lcm), com_gcf)

    return output
    

#Тест

x = cls.rational(cls.integer(0, cls.natural([3,0])), cls.natural([3,0]))
y = cls.rational(cls.integer(0, cls.natural([1,8])), cls.natural([1,8]))
z = cls.rational(cls.integer(0, cls.natural([1,2])), cls.natural([1,2]))

p = cls.polynom([x, y, z])

c = FAC_P_Q(p)

print(c)

#Результат+180/6