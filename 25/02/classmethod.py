#!python3.6
#encoding: utf-8
# classmethod(function)
# 第一引数としてクラスをとる
class C:
    cls_var = 'cls_var value.'
    @classmethod
    def class_method(cls): print(cls.cls_var)

C.class_method()
