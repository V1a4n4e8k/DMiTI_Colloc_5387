"""
Q-2
Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
"""

from classes import *
from MOD_NN_N import MOD_NN_N
from NZER_N_B import NZER_N_B

def INT_Q_B(a : rational):
    ost = MOD_NN_N(a.numerator.data, a.denominator)
    if NZER_N_B(ost) == 0:
        return 1
    return 0
