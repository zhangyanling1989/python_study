# -*- coding: utf-8 -*-


def findMinAndMax(L):
    for num in L:
        a = min(L)
        b = max(L)
        return (a,b)






print(findMinAndMax([7]))
print(findMinAndMax([7, 1]))
print(findMinAndMax([7, 1, 3, 9, 5]))
print(findMinAndMax([]))
