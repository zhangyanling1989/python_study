# -*- coding: utf-8 -*-

# A = [36,5,-12,9,-21]
# print(sorted(A))
#
# print(sorted(A,key = abs))
#
#
# B = ['bob', 'about', 'Zoo', 'Credit']
# print(sorted(B))    # 字符串先按字母大小写排序，再按照字母顺序排序
# print(sorted(B, key = str.lower))
# B.sort()
# print(B)
# print(sorted(B,key = str.lower, reverse = True))
#
#
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda x: (x[1], x[0])))