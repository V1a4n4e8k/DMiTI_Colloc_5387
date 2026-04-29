from classes import integer, rational

def TRANS_Q_Z(a: rational):
    if a.denominator == 1:
        res = integer(a.numerator.sign, a.numerator.data)
        return res
    return integer(None, None)
"""
print(TRANS_Q_Z(rational(integer(-1, [1,2,3]), 2)).data)
"""