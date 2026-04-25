# task5 !!!! a>b !!!! a и b  - массивы ЦИФР
def sub(a, b):
    i=len(a)-1
    j = len(b)-1
    while (i >= 0 and j>=0):
        if a[i] >= b[j]:
            a[i] -= b[j]
        else:
            a[i-1] -= 1
            a[i] = a[i]+10- b[j]
        i -= 1
        j-=1
    while (a[0] == 0):
        a.pop(0)

""" ПРИМЕР ИСПОЛЬЗОВАНИЯ
a = [1,2,3,4]
b = [3,4,5]
sub(a,b)

print(print(a))
"""
# task 1 !!!!!! a, b - NUMBERS 0-9 arrays!
def compare_unsig_int(a, b):
    for i in range(len(a)):
        if a[i] > b[i]:
            return 1
        if i >= len(b):
            return 1
    return 0
""" use ex
print(compare_unsig_int([3,2,3,4],[2,3,4]))
"""
def is_zero(a):
    if len(a) == 0 and a[0] == 0:
        return 0
    return 1
""" use ex
print(is_zero([0]))
"""
def add_one(a):
    i = len(a)-1
    while i >= 0:
        if a[i] != 9:
            a[i] += 1
            break
        i -= 1
""" use ex
a = [1][9]
print(add_one(a))
"""