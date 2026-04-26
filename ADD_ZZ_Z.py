import classes
import SGN_Z_D
#import ABS_Z_Z
import COM_NN_D
import ADD_NN_N
import SUB_NN_N
#import MUL_ZM_Z


def ADD_ZZ_Z(a: classes.integer, b: classes.integer):
    a_sign = SGN_Z_D.SGN_Z_D(a)
    b_sign = SGN_Z_D.SGN_Z_D(b)

    com_nn_d = COM_NN_D.COM_NN_D(a.data.data, b.data.data)

    if com_nn_d == 2:
        big_val = a
        sml_val = b
    elif com_nn_d == 1:
        big_val = b
        sml_val = a
    elif com_nn_d == 0:
        #Без разницы, что больше
        big_val = a
        sml_val = b

    if a_sign == b_sign:
        new_data = ADD_NN_N.ADD_NN_N(a.data.data, b.data.data)
        new_sign = a.sign
    else:
        new_data = SUB_NN_N.SUB_NN_N(big_val.data.data, sml_val.data.data)
        new_sign = big_val.sign

    output = classes.integer(new_sign, classes.natural(new_data))

    return output


#Функция сложения целых чисел

#Функция возвращает новое целое число

#Аргументы функции не меняются и не связываются

#Функция не использует ABS_ZZ_Z и MUL_ZM_Z, но в задании указано, что функция должна ссылатся на эти модули

#Также функция использует SGN_Z_D, в котором нет необходимости