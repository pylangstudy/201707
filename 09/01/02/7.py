import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__')
    def method(self): raise Exception()
c = MyClass()
info = None
try: c.method()
except:
    info = sys.exc_info()[2]
    del info
    del c
    time.sleep(2)
