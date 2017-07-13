import datetime
#print(int('100').__getattribute__('abcdefg')) # AttributeError: 'int' object has no attribute 'abcdefg'
#print(str('abc').__getattribute__('abcdefg')) # AttributeError: 'str' object has no attribute 'abcdefg'
#print(range(3).__getattribute__('abcdefg')) # AttributeError: 'range' object has no attribute 'abcdefg'
#print(datetime.datetime.now().__getattribute__('abcdefg')) # AttributeError: 'datetime.datetime' object has no attribute 'abcdefg'
print(datetime.datetime.now().__getattribute__('now')) # AttributeError: 'datetime.datetime' object has no attribute 'abcdefg'

