# http://dackdive.hateblo.jp/entry/2015/08/02/100000
"""
class MyMetaClass(type):
#    def __new__(cls): return type('MyClass', (object,), {'attribute1': 'value'})
    def __new__(cls, name, bases, attrs):
        attrs['meta'] = 'meta'
        return type.__new__(cls, name, bases, attrs)

class MyClass(object):
    __metaclass__ = MyMetaClass
    def bar(self):
        print(self.__dict__)

c = MyClass()
print(dir(c))
print(c.meta)
"""
# http://www.yunabe.jp/docs/python_metaclass.html
"""
def tolower_classname(name, bases, attrs):
  return type(name.lower(), bases, attrs)

class ClassName(object):
  __metaclass__ = tolower_classname

print(ClassName.__name__) # ClassName
"""

# http://qiita.com/podhmo/items/c601050b20f70d27aa07
class MyMetaClass(type): pass
class MyClass(metaclass=MyMetaClass): pass

