import classes as cl

from ABS_Z_Z import ABS_Z_Z
from SGN_Z_D import SGN_Z_D
from MUL_ZM_Z import MUL_ZM_Z
from TRANS_N_Z import TRANS_N_Z
from TRANS_Z_N import TRANS_Z_N
from ADD_ZZ_Z import ADD_ZZ_Z
from SUB_ZZ_Z import SUB_ZZ_Z
from MUL_ZZ_Z import MUL_ZZ_Z
from DIV_ZZ_Z import DIV_ZZ_Z
from MOD_ZZ_Z import MOD_ZZ_Z


def n(digits):
    return cl.natural(digits)


def z(sign, digits):
    return cl.integer(sign, cl.natural(digits))


def zdigits(num):
    return num.data.data


def zsign(num):
    return num.sign


def assert_z(num, sign, digits):
    assert zsign(num) == sign
    assert zdigits(num) == digits


# Z-1
def test_abs_z_z():
    assert_z(ABS_Z_Z(z(0, [1, 2, 3])), 0, [1, 2, 3])
    assert_z(ABS_Z_Z(z(1, [1, 2, 3])), 0, [1, 2, 3])
    assert_z(ABS_Z_Z(z(0, [0])), 0, [0])
    assert_z(ABS_Z_Z(z(1, [0])), 0, [0])


# Z-2
def test_sgn_z_d():
    assert SGN_Z_D(z(0, [1, 2, 3])) == 1
    assert SGN_Z_D(z(1, [1, 2, 3])) == -1
    assert SGN_Z_D(z(0, [0])) == 0
    assert SGN_Z_D(z(1, [0])) == 0


# Z-3
def test_mul_zm_z():
    assert_z(MUL_ZM_Z(z(0, [1, 2, 3])), 1, [1, 2, 3])
    assert_z(MUL_ZM_Z(z(1, [1, 2, 3])), 0, [1, 2, 3])
    assert_z(MUL_ZM_Z(z(0, [0])), 0, [0])


# Z-4
def test_trans_n_z():
    assert_z(TRANS_N_Z(n([1, 2, 3])), 0, [1, 2, 3])
    assert_z(TRANS_N_Z(n([0])), 0, [0])


# Z-5
def test_trans_z_n():
    assert TRANS_Z_N(z(0, [1, 2, 3])).data == [1, 2, 3]
    assert TRANS_Z_N(z(0, [0])).data == [0]


# Z-6
def test_add_zz_z():
    assert_z(ADD_ZZ_Z(z(0, [1, 2]), z(0, [3])), 0, [1, 5])
    assert_z(ADD_ZZ_Z(z(1, [1, 2]), z(1, [3])), 1, [1, 5])
    assert_z(ADD_ZZ_Z(z(0, [1, 2]), z(1, [3])), 0, [9])
    assert_z(ADD_ZZ_Z(z(1, [1, 2]), z(0, [3])), 1, [9])
    assert_z(ADD_ZZ_Z(z(0, [5]), z(1, [5])), 0, [0])


# Z-7
def test_sub_zz_z():
    assert_z(SUB_ZZ_Z(z(0, [1, 2]), z(0, [3])), 0, [9])
    assert_z(SUB_ZZ_Z(z(0, [3]), z(0, [1, 2])), 1, [9])
    assert_z(SUB_ZZ_Z(z(1, [1, 2]), z(1, [3])), 1, [9])
    assert_z(SUB_ZZ_Z(z(0, [1, 2]), z(1, [3])), 0, [1, 5])
    assert_z(SUB_ZZ_Z(z(1, [1, 2]), z(0, [3])), 1, [1, 5])
    assert_z(SUB_ZZ_Z(z(0, [5]), z(0, [5])), 0, [0])


# Z-8
def test_mul_zz_z():
    assert_z(MUL_ZZ_Z(z(0, [1, 2]), z(0, [3])), 0, [3, 6])
    assert_z(MUL_ZZ_Z(z(1, [1, 2]), z(0, [3])), 1, [3, 6])
    assert_z(MUL_ZZ_Z(z(0, [1, 2]), z(1, [3])), 1, [3, 6])
    assert_z(MUL_ZZ_Z(z(1, [1, 2]), z(1, [3])), 0, [3, 6])
    assert_z(MUL_ZZ_Z(z(1, [1, 2]), z(0, [0])), 0, [0])


# Z-9
def test_div_zz_z():
    assert_z(DIV_ZZ_Z(z(0, [1, 0]), z(0, [2])), 0, [5])
    assert_z(DIV_ZZ_Z(z(1, [1, 0]), z(0, [2])), 1, [5])
    assert_z(DIV_ZZ_Z(z(0, [1, 0]), z(1, [2])), 1, [5])
    assert_z(DIV_ZZ_Z(z(1, [1, 0]), z(1, [2])), 0, [5])

    assert_z(DIV_ZZ_Z(z(0, [7]), z(0, [3])), 0, [2])
    assert_z(DIV_ZZ_Z(z(1, [7]), z(0, [3])), 1, [3])


# Z-10
def test_mod_zz_z():
    assert_z(MOD_ZZ_Z(z(0, [1, 0]), z(0, [3])), 0, [1])
    assert_z(MOD_ZZ_Z(z(1, [1, 0]), z(0, [3])), 0, [2])
    assert_z(MOD_ZZ_Z(z(0, [1, 0]), z(1, [3])), 1, [2])
    assert_z(MOD_ZZ_Z(z(1, [1, 0]), z(1, [3])), 1, [1])
    assert_z(MOD_ZZ_Z(z(0, [1, 0]), z(0, [5])), 0, [0])