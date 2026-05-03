from classes import *
from ABS_Z_Z import ABS_Z_Z
from GCF_NN_N import GCF_NN_N
from DIV_NN_N import DIV_NN_N
from TRANS_N_Z import TRANS_N_Z
from TRANS_Z_N import TRANS_Z_N

def RED_Q_Q(rational_number):
    numerator_natural = TRANS_Z_N(rational_number.numerator)
    gcd = GCF_NN_N(numerator_natural, rational_number.denominator)
    if gcd.n == 1 and gcd.data[0] == 1:
        return rational_number
    divided_numerator_natural = DIV_NN_N(numerator_natural, gcd)  
    numerator_integer = TRANS_N_Z(divided_numerator_natural)
    numerator_integer.sign = rational_number.numerator.sign
    divided_denominator = DIV_NN_N(rational_number.denominator, gcd) 
    return rational(numerator_integer, divided_denominator)
"""
six = integer(0, natural([6]))
eight = natural([8])
frac = rational(six, eight)
reduced_frac = RED_Q_Q(frac)
print(reduced_frac)  
"""