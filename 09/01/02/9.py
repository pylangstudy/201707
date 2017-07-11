import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
try: c.method()
except: print('except')
finally: del c
time.sleep(2);
