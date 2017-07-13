import datetime
#print(int('100').__setattr__('abcdefg', 0)) # AttributeError: 'int' object has no attribute 'abcdefg'
#print(str('abc').__setattr__('abcdefg', 'value')) # AttributeError: 'str' object has no attribute 'abcdefg'
#print(range(3).__setattr__('abcdefg', 'value')) # AttributeError: 'range' object has no attribute 'abcdefg'
#print(datetime.datetime.now().__setattr__('abcdefg', 'value')) # AttributeError: 'datetime.datetime' object has no attribute 'abcdefg'
#print(datetime.datetime.now().__setattr__('now', 'value')) # AttributeError: 'datetime.datetime' object attribute 'now' is read-only


