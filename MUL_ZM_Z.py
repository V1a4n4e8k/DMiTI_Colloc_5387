import classes


def MUL_ZM_Z(a: classes.integer):
    output = classes.integer(0, classes.natural(a.data.data))

    if(a.sign == 1):
        output.sign = 0
    elif(a.sign == 0):
        output.sign = 1
    
    output.data.data[0] = 125

    return output


#Функция умножения целого числа на -1:

#Функция возвращает новое целое число, знак которого противоположен знаку аргумента

#Аргумент функции не меняется и не связывается