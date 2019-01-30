# -*- coding: utf-8 -*-

# L = []
# # n = 1
# # while n<= 99:
# #     L.append(n)
# #     n = n+2
# #
# # print(L)


# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
#
# print(r)
#
# L[0:3]
# print(r)

# L = list(range(100))
# print(L)
# print(L[:10])  #取前十位
# print(L[-10:])  #取后十位
# print(L[:10:2])  #取前十位每隔两个取一个
# print(L[::5])    #取所有书每隔5个取一个
# print(L[:])     #取原列表
#
# a = (0,1,2,3,4,5)
# print(a[:3])
#
# a = '123456'
# print(a[:3])

# def trim(s):
#     n = 1
#     m = 1
#     for i in s:
#         if i == ' ' and i ==s[0]:
#             n +=1
#             s = s[n:]
#             return s
#         elif i == ' 'and i == s[-1]:
#             n +=1
#             s = s[:-n]
#             return s
#         elif i != '':
#             return s





def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])


print(trim('hello'))
print(trim('hello  '))
print(trim('  hello'))
print(trim('   hello   '))
print(trim('    hello  world   '))
print(trim(''))
print(trim('    '))


