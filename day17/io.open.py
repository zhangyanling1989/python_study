# -*- coding: UTF-8 -*-

import io

f = io.open('abc.txt','wt', encoding='utf-8')
f.write(u'你好， 我现在在学转码')
f.write('\n原来用utf是可以转换语言的')
f.close()

text = io.open('abc.txt',encoding='utf-8').read()
print(text)