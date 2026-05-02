import classes as cl

# from RED_Q_Q import RED_Q_Q
from INT_Q_B import INT_Q_B
from TRANS_Z_Q import TRANS_Z_Q
from TRANS_Q_Z import TRANS_Q_Z
# from ADD_QQ_Q import ADD_QQ_Q
# from SUB_QQ_Q import SUB_QQ_Q
# from MUL_QQ_Q import MUL_QQ_Q
# from DIV_QQ_Q import DIV_QQ_Q


def n(digits):
    return cl.natural(digits)


def z(sign, digits):
    return cl.integer(sign, cl.natural(digits))


def q(sign, num_digits, den_digits):
    return cl.rational(
        cl.integer(sign, cl.natural(num_digits)),
        cl.natural(den_digits)
    )


def q_num_digits(x):
    return x.numerator.data.data


def q_num_sign(x):
    return x.numerator.sign


def q_den_digits(x):
    return x.denominator.data


def assert_q(x, sign, num_digits, den_digits):
    assert q_num_sign(x) == sign
    assert q_num_digits(x) == num_digits
    assert q_den_digits(x) == den_digits


# Q-1
def test_red_q_q():
    assert_q(RED_Q_Q(q(0, [2], [4])), 0, [1], [2])
    assert_q(RED_Q_Q(q(1, [6], [8])), 1, [3], [4])
    assert_q(RED_Q_Q(q(0, [1, 0], [5])), 0, [2], [1])
    assert_q(RED_Q_Q(q(0, [0], [5])), 0, [0], [1])


# Q-2
def test_int_q_b():
    assert INT_Q_B(q(0, [4], [2])) == 1
    assert INT_Q_B(q(1, [9], [3])) == 1
    assert INT_Q_B(q(0, [3], [2])) == 0
    assert INT_Q_B(q(0, [0], [5])) == 1


# Q-3
def test_trans_z_q():
    assert_q(TRANS_Z_Q(z(0, [1, 2])), 0, [1, 2], [1])
    assert_q(TRANS_Z_Q(z(1, [5])), 1, [5], [1])
    assert_q(TRANS_Z_Q(z(0, [0])), 0, [0], [1])


# Q-4
def test_trans_q_z():
    x = TRANS_Q_Z(q(0, [1, 2], [1]))
    assert x.sign == 0
    assert x.data.data == [1, 2]

    x = TRANS_Q_Z(q(1, [5], [1]))
    assert x.sign == 1
    assert x.data.data == [5]

    x = TRANS_Q_Z(q(0, [0], [1]))
    assert x.sign == 0
    assert x.data.data == [0]


# Q-5
def test_add_qq_q():
    # 1/2 + 1/3 = 5/6
    assert_q(ADD_QQ_Q(q(0, [1], [2]), q(0, [1], [3])), 0, [5], [6])

    # -1/2 + 1/3 = -1/6
    assert_q(ADD_QQ_Q(q(1, [1], [2]), q(0, [1], [3])), 1, [1], [6])

    # 2/3 + 4/3 = 2/1
    assert_q(ADD_QQ_Q(q(0, [2], [3]), q(0, [4], [3])), 0, [2], [1])


# Q-6
def test_sub_qq_q():
    # 1/2 - 1/3 = 1/6
    assert_q(SUB_QQ_Q(q(0, [1], [2]), q(0, [1], [3])), 0, [1], [6])

    # 1/3 - 1/2 = -1/6
    assert_q(SUB_QQ_Q(q(0, [1], [3]), q(0, [1], [2])), 1, [1], [6])

    # -1/2 - 1/3 = -5/6
    assert_q(SUB_QQ_Q(q(1, [1], [2]), q(0, [1], [3])), 1, [5], [6])


# Q-7
def test_mul_qq_q():
    # 2/3 * 3/4 = 1/2
    assert_q(MUL_QQ_Q(q(0, [2], [3]), q(0, [3], [4])), 0, [1], [2])

    # -2/3 * 3/4 = -1/2
    assert_q(MUL_QQ_Q(q(1, [2], [3]), q(0, [3], [4])), 1, [1], [2])

    # 0 * 5/7 = 0
    assert_q(MUL_QQ_Q(q(0, [0], [1]), q(0, [5], [7])), 0, [0], [1])


# Q-8
def test_div_qq_q():
    # 1/2 / 3/4 = 2/3
    assert_q(DIV_QQ_Q(q(0, [1], [2]), q(0, [3], [4])), 0, [2], [3])

    # -1/2 / 3/4 = -2/3
    assert_q(DIV_QQ_Q(q(1, [1], [2]), q(0, [3], [4])), 1, [2], [3])

    # 2/3 / -4/5 = -5/6
    assert_q(DIV_QQ_Q(q(0, [2], [3]), q(1, [4], [5])), 1, [5], [6])