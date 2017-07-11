import sys
import time
class MyClass:
    def __del__(self): print('MyClass.__del__'); raise Exception('__del__()エラー。')
    def method(self): raise Exception('method()エラー。')
c = MyClass()
try: c.method()
except: print('except')
finally: c = None
time.sleep(2);
print('プログラム実行完了。')
