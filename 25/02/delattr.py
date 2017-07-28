#!python3.6
#coding:utf-8
#delattr(object, name)
class C:
    def a(): print('A')
c = C()
print('a' in C.__dict__)
delattr(C, 'a')
print('a' in C.__dict__)
