from COM_NN_D import COM_NN_D
from NZER_N_B import NZER_N_B
from ADD_1N_N import ADD_1N_N
from ADD_NN_N import ADD_NN_N
from SUB_NN_N import SUB_NN_N
from MUL_ND_N import MUL_ND_N
from MUL_Nk_N import MUL_Nk_N
from MUL_NN_N import MUL_NN_N
from SUB_NDN_N import SUB_NDN_N
from DIV_NN_Dk import DIV_NN_Dk
from DIV_NN_N import DIV_NN_N
from MOD_NN_N import MOD_NN_N
from GCF_NN_N import GCF_NN_N
from LCM_NN_N import LCM_NN_N
import classes as cl


"""
N-1
COM_NN_D
Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
"""

def n(lst):
    return cl.natural(lst)


def d(num):
    return num.data


# N-1
def test_com_nn_d():
    assert COM_NN_D(n([1, 2, 3]), n([1, 2, 3])) == 0
    assert COM_NN_D(n([1, 2, 4]), n([1, 2, 3])) == 2
    assert COM_NN_D(n([9]), n([1, 0])) == 1
    assert COM_NN_D(n([1, 0, 0]), n([9, 9])) == 2


# N-2
def test_nzer_n_b():
    assert NZER_N_B(n([0])) == 0
    assert NZER_N_B(n([1])) == 1
    assert NZER_N_B(n([1, 0])) == 1


# N-3
def test_add_1n_n():
    assert d(ADD_1N_N(n([1, 2, 3]))) == [1, 2, 4]
    assert d(ADD_1N_N(n([1, 2, 9]))) == [1, 3, 0]
    assert d(ADD_1N_N(n([9, 9, 9]))) == [1, 0, 0, 0]
    assert d(ADD_1N_N(n([0]))) == [1]


# N-4
def test_add_nn_n():
    assert d(ADD_NN_N(n([1, 2]), n([3, 4]))) == [4, 6]
    assert d(ADD_NN_N(n([9, 9]), n([1]))) == [1, 0, 0]
    assert d(ADD_NN_N(n([0]), n([0]))) == [0]
    assert d(ADD_NN_N(n([5, 5, 5]), n([4, 4, 5]))) == [1, 0, 0, 0]


# N-5
def test_sub_nn_n():
    assert d(SUB_NN_N(n([1, 2, 3]), n([2, 3]))) == [1, 0, 0]
    assert d(SUB_NN_N(n([1, 0, 0, 0]), n([1]))) == [9, 9, 9]
    assert d(SUB_NN_N(n([1, 2, 3]), n([1, 2, 3]))) == [0]
    assert d(SUB_NN_N(n([5, 0, 0]), n([4, 9, 9]))) == [1]


# N-6
def test_mul_nd_n():
    assert d(MUL_ND_N(n([1, 2, 3]), 2)) == [2, 4, 6]
    assert d(MUL_ND_N(n([9, 9]), 9)) == [8, 9, 1]
    assert d(MUL_ND_N(n([1, 2, 3]), 0)) == [0]
    assert d(MUL_ND_N(n([0]), 8)) == [0]


# N-7
def test_mul_nk_n():
    assert d(MUL_Nk_N(n([1, 2, 3]), 0)) == [1, 2, 3]
    assert d(MUL_Nk_N(n([1, 2, 3]), 2)) == [1, 2, 3, 0, 0]
    assert d(MUL_Nk_N(n([0]), 5)) == [0]


# N-8
def test_mul_nn_n():
    assert d(MUL_NN_N(n([1, 2]), n([3]))) == [3, 6]
    assert d(MUL_NN_N(n([1, 2]), n([1, 2]))) == [1, 4, 4]
    assert d(MUL_NN_N(n([1, 2, 3]), n([4, 5]))) == [5, 5, 3, 5]
    assert d(MUL_NN_N(n([0]), n([9, 9]))) == [0]


# N-9
def test_sub_ndn_n():
    # 100 - 12 * 8 = 4
    assert d(SUB_NDN_N(n([1, 0, 0]), n([1, 2]), 8)) == [4]

    # 500 - 99 * 5 = 5
    assert d(SUB_NDN_N(n([5, 0, 0]), n([9, 9]), 5)) == [5]

    # 123 - 10 * 0 = 123
    assert d(SUB_NDN_N(n([1, 2, 3]), n([1, 0]), 0)) == [1, 2, 3]


# N-10
def test_div_nn_dk():
    # 9876 / 123 = 80...
    assert d(DIV_NN_Dk(n([9, 8, 7, 6]), n([1, 2, 3]))) == [8, 0]

    # 999 / 9 = 100...
    assert d(DIV_NN_Dk(n([9, 9, 9]), n([9]))) == [1, 0, 0]

    # 50 / 6 = 8...
    assert d(DIV_NN_Dk(n([5, 0]), n([6]))) == [8]

    # 100 / 20 = 5
    assert d(DIV_NN_Dk(n([1, 0, 0]), n([2, 0]))) == [5]


# N-11
def test_div_nn_n():
    assert d(DIV_NN_N(n([9, 8, 7, 6]), n([1, 2, 3]))) == [8, 0]
    assert d(DIV_NN_N(n([1, 0]), n([2]))) == [5]
    assert d(DIV_NN_N(n([5]), n([1, 0]))) == [0]
    assert d(DIV_NN_N(n([1, 0, 0]), n([2, 0]))) == [5]
    assert d(DIV_NN_N(n([9, 9, 9]), n([9]))) == [1, 1, 1]


# N-12
def test_mod_nn_n():
    assert d(MOD_NN_N(n([9, 8, 7, 6]), n([1, 2, 3]))) == [3, 6]
    assert d(MOD_NN_N(n([1, 0]), n([2]))) == [0]
    assert d(MOD_NN_N(n([5]), n([1, 0]))) == [5]
    assert d(MOD_NN_N(n([1, 0, 0]), n([2, 0]))) == [0]
    assert d(MOD_NN_N(n([9, 9, 9]), n([9]))) == [0]


# N-13
def test_gcf_nn_n():
    assert d(GCF_NN_N(n([4, 8]), n([1, 8]))) == [6]
    assert d(GCF_NN_N(n([1, 2]), n([1, 8]))) == [6]
    assert d(GCF_NN_N(n([1, 0, 0]), n([2, 5]))) == [2, 5]
    assert d(GCF_NN_N(n([1, 7]), n([1, 3]))) == [1]


# N-14
def test_lcm_nn_n():
    assert d(LCM_NN_N(n([1, 2]), n([1, 8]))) == [3, 6]
    assert d(LCM_NN_N(n([4]), n([6]))) == [1, 2]
    assert d(LCM_NN_N(n([1, 0, 0]), n([2, 5]))) == [1, 0, 0]
    assert d(LCM_NN_N(n([1, 7]), n([1, 3]))) == [2, 2, 1]


