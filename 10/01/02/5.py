import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
c1 = MyClass()
del c1
time.sleep(2)
c2 = MyClass()
