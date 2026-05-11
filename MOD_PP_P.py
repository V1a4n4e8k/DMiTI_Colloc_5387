"""
P-10
Остаток от деления многочлена на многочлен при делении с остатком
MOD_PP_P
"""

from copy import deepcopy
import classes as cl

from DIV_PP_P import DIV_PP_P
from MUL_PP_P import MUL_PP_P
from SUB_PP_P import SUB_PP_P


def MOD_PP_P(a_arg: cl.polynom, b_arg: cl.polynom):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)

    div = DIV_PP_P(a, b)

    if div is None:
        return None

    pr = MUL_PP_P(b, div)

    rest = SUB_PP_P(a, pr)

    return rest