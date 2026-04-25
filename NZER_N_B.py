"""
N-2
Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
"""

def NZER_N_B(a):
    if len(a) == 1 and a[0] == 0:
        return 0
    return 1

""" use ex
print(NZER_N_B([0]))
"""