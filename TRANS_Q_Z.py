"""
Q-4
Преобразование сокращенного дробного в целое (если знаменатель равен 1)
"""

from classes import integer, rational

def TRANS_Q_Z(a: rational):
    if a.denominator.data == [1] and a.denominator.n == 1:
        res = integer(a.numerator.sign, a.numerator.data)
        return res
    return integer(None, None)