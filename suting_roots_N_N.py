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

# вычисление корня натурального числа
def natural_sqrt(n: natural):
    l_n = natural(deepcopy(n.data))
    one = natural([1])
    while COM_NN_D(MUL_NN_N(l_n, l_n), n) > 1:
        l_n = SUB_NN_N(l_n, one)
    return l_n
# перевод натурального числа к стандартному пайтоновскому инту 
# (нужно только для вводы/вывода не используется в логике программы
# а по сему не нарушает концепции длинного числа)
def natural_to_int(n: natural) -> int:
    return int(''.join(map(str, n.data)))
# обратная предыдущей
def int_to_natural(num: int) -> natural:
    if num == 0:
        return natural([0])
    digits = []
    while num > 0:
        digits.insert(0, num % 10)
        num //= 10
    return natural(digits)
# функция для представления квадратного корня натурального числа в виде циклической дроби
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
## функция для преобразования цепной дроби, cf которая повторяется periods раз к 
# типу rational
def continued_fraction_to_rational(cf, periods=1):
    a0 = cf[0]
    period = cf[1]
    
    if not period:
        # Целое число -> преобразуем в дробное
        int_num = integer(0, int_to_natural(a0))
        return TRANS_Z_Q(int_num)
    
    # Строим коэффициенты
    coeffs = [a0]
    for _ in range(periods):
        coeffs.extend(period)
    
    # Начинаем с последнего коэффициента как дроби
    # a_n / 1
    last_int = integer(0, int_to_natural(coeffs[-1]))
    result = TRANS_Z_Q(last_int)
    
    # Идём с конца к началу: result = a_i + 1/result
    for coeff in reversed(coeffs[:-1]):
        # 1/result
        one_int = integer(0, int_to_natural(1))
        one_rat = TRANS_Z_Q(one_int)
        inv_result = DIV_QQ_Q(one_rat, result)  # 1 / result
        
        # a_i
        a_int = integer(0, int_to_natural(coeff))
        a_rat = TRANS_Z_Q(a_int)
        
        # a_i + 1/result
        result = ADD_QQ_Q(a_rat, inv_result)
        
        # Сокращаем дробь
        result = RED_Q_Q(result)
    
    return result

# Пример использования
n = natural([1, 4, 3])
print(f"Число: {natural_to_int(n)}")

res_cf = sqrt_continued_fraction(n)
print(f"√{natural_to_int(n)} = [{res_cf[0]}; ({', '.join(map(str, res_cf[1]))})]")

# Получаем рациональное приближение
res_rat = continued_fraction_to_rational(res_cf, periods=1)
print(f"Сокращённая дробь: {res_rat}")

# Проверяем, является ли целым
from INT_Q_B import INT_Q_B
is_int = INT_Q_B(res_rat)
print(f"Является целым? {'Да' if is_int else 'Нет'}")

# Преобразуем в целое если возможно
if is_int:
    as_int = TRANS_Q_Z(res_rat)
    print(f"Целое значение: {as_int}")