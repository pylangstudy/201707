import datetime
#print(int('100').__getattr__('abcdefg')) # AttributeError: 'int' object has no attribute '__getattr__'
#print(str('abc').__getattr__('abcdefg')) # AttributeError: 'str' object has no attribute '__getattr__'
#print(range(3).__getattr__('abcdefg')) # AttributeError: 'range' object has no attribute '__getattr__'
#print(datetime.datetime.now().__getattr__('abcdefg')) # AttributeError: 'datetime.datetime' object has no attribute '__getattr__'

