# def fact(n):
#     if n==1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))
#
# def fact(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)
#
# print(fact(5))


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)

print(hanoi(5, 'A', 'B', 'C'))