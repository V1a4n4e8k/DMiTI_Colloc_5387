import classes as cl

from ADD_PP_P import ADD_PP_P
from SUB_PP_P import SUB_PP_P
from MUL_PQ_P import MUL_PQ_P
from MUL_Pxk_P import MUL_Pxk_P
from LED_P_Q import LED_P_Q
from DEG_P_N import DEG_P_N
from FAC_P_Q import FAC_P_Q
# from MUL_PP_P import MUL_PP_P
# from DIV_PP_P import DIV_PP_P
# from MOD_PP_P import MOD_PP_P
# from GCF_PP_P import GCF_PP_P
# from DER_P_P import DER_P_P
# from NMR_P_P import NMR_P_P


def q(sign, num, den):
    return cl.rational(
        cl.integer(sign, cl.natural(num)),
        cl.natural(den)
    )


def p(coefs):
    return cl.polynom(coefs)


def qeq(x, sign, num, den):
    assert x.numerator.sign == sign
    assert x.numerator.data.data == num
    assert x.denominator.data == den


def peq(poly, expected):
    assert poly.deg == len(expected) - 1

    for i, (sign, num, den) in enumerate(expected):
        qeq(poly.coef[i], sign, num, den)


# P-1
def test_add_pp_p():
    # (x + 1) + (x + 2) = 2x + 3
    r = ADD_PP_P(
        p([q(0, [1], [1]), q(0, [1], [1])]),
        p([q(0, [1], [1]), q(0, [2], [1])])
    )

    peq(r, [
        (0, [2], [1]),
        (0, [3], [1]),
    ])


# P-2
def test_sub_pp_p():
    # (2x + 5) - (x + 3) = x + 2
    r = SUB_PP_P(
        p([q(0, [2], [1]), q(0, [5], [1])]),
        p([q(0, [1], [1]), q(0, [3], [1])])
    )

    peq(r, [
        (0, [1], [1]),
        (0, [2], [1]),
    ])
    
    # (2x + 5) - (6x^2 + x + 3) = -6x^2 + x + 2
    r = SUB_PP_P(
        p([q(0, [2], [1]), q(0, [5], [1])]),
        p([q(0, [6], [1]), q(0, [1], [1]), q(0, [3], [1])])
    )

    peq(r, [
        (1, [6], [1]),
        (0, [1], [1]),
        (0, [2], [1]),
    ])


# P-3
def test_mul_pq_p():
    # (x + 2) * 1/2 = 1/2 x + 1
    r = MUL_PQ_P(
        p([q(0, [1], [1]), q(0, [2], [1])]),
        q(0, [1], [2])
    )

    peq(r, [
        (0, [1], [2]),
        (0, [1], [1]),
    ])


# P-4
def test_mul_pxk_p():
    # (x + 1) * x^2 = x^3 + x^2
    r = MUL_Pxk_P(
        p([q(0, [1], [1]), q(0, [1], [1])]),
        2
    )

    peq(r, [
        (0, [1], [1]),
        (0, [1], [1]),
        (0, [0], [1]),
        (0, [0], [1]),
    ])


# P-5
def test_led_p_q():
    poly = p([
        q(1, [3], [4]),
        q(0, [2], [1]),
        q(0, [5], [1]),
    ])

    r = LED_P_Q(poly)

    qeq(r, 1, [3], [4])


# P-6
def test_deg_p_n():
    poly = p([
        q(0, [1], [1]),
        q(0, [2], [1]),
        q(0, [3], [1]),
        q(0, [4], [1]),
    ])

    r = DEG_P_N(poly)

    assert r.data == [3]


# P-7
def test_fac_p_q():
    # коэффициенты: 2/3, 4/5
    # НОД числителей = 2
    # НОК знаменателей = 15
    # FAC = 2/15
    poly = p([
        q(0, [2], [3]),
        q(0, [4], [5]),
    ])

    r = FAC_P_Q(poly)

    qeq(r, 0, [2], [1, 5])


# P-8
def test_mul_pp_p():
    # (x + 1)(x + 2) = x^2 + 3x + 2
    r = MUL_PP_P(
        p([q(0, [1], [1]), q(0, [1], [1])]),
        p([q(0, [1], [1]), q(0, [2], [1])])
    )

    peq(r, [
        (0, [1], [1]),
        (0, [3], [1]),
        (0, [2], [1]),
    ])


# P-9
def test_div_pp_p():
    # (x^2 + 3x + 2) / (x + 1) = x + 2
    r = DIV_PP_P(
        p([
            q(0, [1], [1]),
            q(0, [3], [1]),
            q(0, [2], [1]),
        ]),
        p([
            q(0, [1], [1]),
            q(0, [1], [1]),
        ])
    )

    peq(r, [
        (0, [1], [1]),
        (0, [2], [1]),
    ])


# P-10
def test_mod_pp_p():
    # (x^2 + 1) mod (x + 1) = 2
    r = MOD_PP_P(
        p([
            q(0, [1], [1]),
            q(0, [0], [1]),
            q(0, [1], [1]),
        ]),
        p([
            q(0, [1], [1]),
            q(0, [1], [1]),
        ])
    )

    peq(r, [
        (0, [2], [1]),
    ])


# P-11
def test_gcf_pp_p():
    # GCF(x^2 + 3x + 2, x^2 + 4x + 3) = x + 1
    r = GCF_PP_P(
        p([
            q(0, [1], [1]),
            q(0, [3], [1]),
            q(0, [2], [1]),
        ]),
        p([
            q(0, [1], [1]),
            q(0, [4], [1]),
            q(0, [3], [1]),
        ])
    )

    peq(r, [
        (0, [1], [1]),
        (0, [1], [1]),
    ])


# P-12
def test_der_p_p():
    # derivative of 3x^3 + 2x^2 + x + 5 = 9x^2 + 4x + 1
    r = DER_P_P(
        p([
            q(0, [3], [1]),
            q(0, [2], [1]),
            q(0, [1], [1]),
            q(0, [5], [1]),
        ])
    )

    peq(r, [
        (0, [9], [1]),
        (0, [4], [1]),
        (0, [1], [1]),
    ])


# P-13
def test_nmr_p_p():
    # P = (x - 1)^2(x + 2) = x^3 - 3x + 2
    # NMR(P) = (x - 1)(x + 2) = x^2 + x - 2
    r = NMR_P_P(
        p([
            q(0, [1], [1]),
            q(0, [0], [1]),
            q(1, [3], [1]),
            q(0, [2], [1]),
        ])
    )

    peq(r, [
        (0, [1], [1]),
        (0, [1], [1]),
        (1, [2], [1]),
    ])
