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
