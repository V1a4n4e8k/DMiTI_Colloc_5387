import classes


def SGN_Z_D(a: classes.integer):
    if a.data.n == 1 and a.data.data[0] == 0:
        return 0 

    if a.data.n == 0:
        return 0
    
    if a.sign == 1:
        return 1
    
    return 2

#Функция определения положительности числа, возвращает:
# 2 - если число положительное
# 1 - если число отрицательное
# 0 - если число равно 0
#
# Функция возвращает 0, если размер массива цифр равен 0