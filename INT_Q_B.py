from classes import *
from COM_NN_D import *

def INT_Q_B(a : rational):
    if COM_NN_D(a.denominator.data, natural([1])) == 0:
        return 1
    return 0