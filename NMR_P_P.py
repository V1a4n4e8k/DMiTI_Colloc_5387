"""
P-13
Преобразование многочлена — кратные корни в простые
NMR_P_P
"""

from copy import deepcopy
import classes as cl

from DER_P_P import DER_P_P
from GCF_PP_P import GCF_PP_P
from DIV_PP_P import DIV_PP_P


def NMR_P_P(a_arg: cl.polynom):
    a = deepcopy(a_arg)

    der = DER_P_P(a)
    gcf = GCF_PP_P(a, der)

    return DIV_PP_P(a, gcf)