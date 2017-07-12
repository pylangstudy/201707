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
    del c
    print(info)
    time.sleep(2)
print(info)
