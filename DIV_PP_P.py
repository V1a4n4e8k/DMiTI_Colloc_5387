"""
P-9
Частное от деления многочлена на многочлен при делении с остатком
DIV_PP_P
Зависимости:
DIV_QQ_Q
DEG_P_N
MUL_Pxk_P
SUB_PP_P
ADD_PP_P
"""
from copy import deepcopy
import classes as cl
from SUB_PP_P import SUB_PP_P
from MUL_Pxk_P import MUL_Pxk_P
from ADD_PP_P import ADD_PP_P
from DIV_QQ_Q import DIV_QQ_Q
from DEG_P_N import DEG_P_N

def DIV_PP_P(a_arg : polynom, b_arg : polynom):
    a = deepcopy(a_arg)
    b = deepcopy(b_arg)
    res = cl.polynom([cl.rational(cl.integer(0,cl.natural([0])),cl.natural([1]))])
    k = a.deg - b.deg
    if(k < 0):
        return cl.polynom([cl.rational(cl.integer(0,cl.natural([0])),cl.natural([1]))])
    count = 0
    while(count <= k):
        coef = DIV_QQ_Q(a.coef[count], b.coef[count])

