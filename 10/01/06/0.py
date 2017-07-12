import datetime
print(int('100').__format__('+'))
print(int('-100').__format__('+'))
print(str('abc').__format__('>5'))
#print(range(3).__format__('='))
print(datetime.datetime.now().__format__('%Y-%m-%d %H:%M:%S'))
