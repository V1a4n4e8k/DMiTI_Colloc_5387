import time
import math
from copy import deepcopy
from classes import *
from MUL_NN_N import MUL_NN_N
from COM_NN_D import COM_NN_D
from SUB_NN_N import SUB_NN_N
from DIV_NN_N import DIV_NN_N
from ADD_NN_N import ADD_NN_N
from RED_Q_Q import RED_Q_Q
from TRANS_Z_Q import TRANS_Z_Q
from TRANS_Q_Z import TRANS_Q_Z
from ADD_QQ_Q import ADD_QQ_Q
from DIV_QQ_Q import DIV_QQ_Q
from MUL_QQ_Q import MUL_QQ_Q
from SUB_QQ_Q import SUB_QQ_Q


"""
Программа сравнивает два алгоритма приближённого 
вычисления квадратного корня из натурального числа

Первый алгоритм (цепные дроби) строит периодическую цепную дробь 
для √n методом Лагранжа, затем сворачивает её в рациональное число. 

Второй алгоритм (b1) использует бинарный поиск с экспоненциально убывающим шагом.
На каждой итерации шаг делится пополам, вычисляется середина интервала, 
и если её квадрат меньше n, левая граница сдвигается
"""


def natural_sqrt(n: natural):
    l_n = natural(deepcopy(n.data))
    one = natural([1])
    while COM_NN_D(MUL_NN_N(l_n, l_n), n) > 1:
        l_n = SUB_NN_N(l_n, one)
    return l_n

def natural_to_int(n: natural) -> int:
    if n is None or n.data is None:
        return 0
    return int(''.join(map(str, n.data)))

def int_to_natural(num: int) -> natural:
    if num == 0:
        return natural([0])
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num //= 10
    return natural(digits)

def sqrt_continued_fraction(n: natural):
    a0 = natural_sqrt(n)
    zero = natural([0])
    one = natural([1])
    m, d, a = zero, one, a0
    seen = {}
    coeffs = []
    
    while True:
        key = (tuple(m.data), tuple(d.data))
        
        if key in seen:
            break
        
        seen[key] = len(coeffs)
        
        m_next = SUB_NN_N(MUL_NN_N(d, a), m)
        d_next = DIV_NN_N(SUB_NN_N(n, MUL_NN_N(m_next, m_next)), d)
        a_next = DIV_NN_N(ADD_NN_N(a0, m_next), d_next)
        
        a_val = natural_to_int(a)
        coeffs.append(a_val)
        
        m, d, a = m_next, d_next, a_next
    
    period_start = seen[key]
    periodic_part = coeffs[period_start:]
    
    return [coeffs[0], tuple(periodic_part)]

def continued_fraction_to_rational(cf, periods=1):
    a0 = cf[0]
    period = cf[1]
    
    if not period:
        int_num = integer(0, int_to_natural(a0))
        return TRANS_Z_Q(int_num)
    
    coeffs = [a0]
    for _ in range(periods):
        coeffs.extend(period)
    
    last_int = integer(0, int_to_natural(coeffs[-1]))
    result = TRANS_Z_Q(last_int)
    
    for coeff in reversed(coeffs[:-1]):
        one_int = integer(0, int_to_natural(1))
        one_rat = TRANS_Z_Q(one_int)
        inv_result = DIV_QQ_Q(one_rat, result)
        
        a_int = integer(0, int_to_natural(coeff))
        a_rat = TRANS_Z_Q(a_int)
        
        result = ADD_QQ_Q(a_rat, inv_result)
        result = RED_Q_Q(result)
    
    return result

def find_remainder(a: natural, b: natural):
    ac = deepcopy(a)
    bc = deepcopy(b)
    d = DIV_NN_N(ac, bc)
    if d is None:
        return natural([0])
    res = SUB_NN_N(ac, MUL_NN_N(bc, d))
    if res is None:
        return natural([0])
    return res

def rat_to_aprox_real(r: rational, max_time: float):
    """
    Преобразует рациональное число в десятичную строку
    max_time - максимальное время работы в секундах
    """
    start_time = time.time()
    
    # Получаем числитель и знаменатель
    num = natural(r.numerator.data.data)
    den = natural(r.denominator.data)
    
    # Целая часть
    integer_part = DIV_NN_N(num, den)
    if integer_part is None:
        return 0.0
    remainder = find_remainder(num, den)
    if remainder is None or remainder.data is None:
        remainder = natural([0])
    
    result = str(natural_to_int(integer_part)) + "."
    
    # Дробная часть
    while time.time() - start_time < max_time:
        if remainder is None or remainder.data is None:
            remainder = natural([0])
        remainder.data.append(0)
        digit = DIV_NN_N(remainder, den)
        if digit is None:
            break
        result += str(natural_to_int(digit))
        remainder = find_remainder(remainder, den)
        
        if remainder is not None and natural_to_int(remainder) == 0:
            break
    
    return float(result)

def b1(n: natural, max_time: float):
    """
    Бинарный поиск корня с дроблением шага пополам
    """
    start_time = time.time()
    
    one_nat = natural([1])
    one_int = integer(0, one_nat)
    
    # Находим целую часть корня
    a0 = natural_sqrt(n)
    a0_int = integer(0, a0)
    
    # left = a0 (приближение снизу)
    left = TRANS_Z_Q(a0_int)
    
    # step = 1
    step_num = integer(0, one_nat)
    step_den = natural([1])
    step = rational(step_num, step_den)
    
    iteration = 0
    
    while time.time() - start_time < max_time:
        iteration += 1
        
        # step = step / 2
        two_int = integer(0, natural([2]))
        two_rat = TRANS_Z_Q(two_int)
        step = DIV_QQ_Q(step, two_rat)
        
        # mid = left + step
        mid = ADD_QQ_Q(left, step)
        
        # Вычисляем mid^2
        mid_squared = MUL_QQ_Q(mid, mid)
        
        # n как rational
        n_int = integer(0, n)
        n_rat = TRANS_Z_Q(n_int)
        
        # Сравниваем mid^2 и n
        diff = SUB_QQ_Q(mid_squared, n_rat)
        
        # Если diff отрицательный (mid^2 < n), то left = mid
        if diff.numerator.sign == 1:
            left = mid
    
    return left


"""
есты запускаются на числах 12, 143, 2, 10. Для каждого числа сначала 
выполняется алгоритм цепной дроби, замеряется его полное время. 
Затем алгоритм b1 получает это же время как лимит — так оба алгоритма 
работают одинаковое время. Оба результата переводятся в десятичную строку 
за 0.001 сек и сравниваются с math.sqrt. Выводятся погрешности и их соотношение
"""


# Сравнение алгоритмов
print("="*60)
print("СРАВНЕНИЕ АЛГОРИТМОВ")
print("="*60)

test_numbers = [
    natural([1, 2]),      # 12
    natural([1, 4, 3]),   # 143
    natural([2]),         # 2
    natural([1, 0]),      # 10
]

for n in test_numbers:
    print(f"\nЧисло: {natural_to_int(n)}")
    print("-"*40)
    
    # Первый алгоритм: цепная дробь
    start_cf = time.time()
    res_cf = sqrt_continued_fraction(n)
    time_cf_build = time.time() - start_cf
    
    start_rat = time.time()
    res_rat = continued_fraction_to_rational(res_cf, periods=2)
    time_rat = time.time() - start_rat
    
    total_time_cf = time_cf_build + time_rat
    
    start_approx = time.time()
    approx_cf = rat_to_aprox_real(res_rat, 0.001)
    time_approx = time.time() - start_approx
    
    print(f"Алгоритм цепной дроби:")
    print(f"  Время построения CF: {time_cf_build:.6f} сек")
    print(f"  Приближение: {approx_cf}")
    
    # Второй алгоритм: b1 с таким же временем
    start_b1 = time.time()
    res_b1_rat = b1(n, total_time_cf)
    time_b1 = time.time() - start_b1
    
    start_b1_approx = time.time()
    approx_b1 = rat_to_aprox_real(res_b1_rat, 0.001)
    time_b1_approx = time.time() - start_b1_approx
    
    print(f"Алгоритм b1 (бинарный поиск):")
    print(f"  Время выполнения: {time_b1:.6f} сек")
    print(f"  Приближение: {approx_b1}")
    
    # Эталонное значение
    exact = math.sqrt(natural_to_int(n))
    print(f"Python math.sqrt: {exact}")
    
    # Погрешности
    error_cf = abs(approx_cf - exact)
    error_b1 = abs(approx_b1 - exact)
    
    print(f"Погрешность CF: {error_cf:.10f}")
    print(f"Погрешность b1: {error_b1:.10f}")
    
    if error_cf < error_b1:
        print("✓ Цепная дробь точнее")
    elif error_b1 < error_cf:
        print("✓ Бинарный поиск точнее")
    else:
        print("✓ Точность одинаковая")
    
    if error_cf > 0:
        print(f"Соотношение b1/CF = {error_b1/error_cf:.2f}")