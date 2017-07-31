print(''.join(['a','b','c']))
print(','.join(['a','b','c']))
#print(str.join(['a','b','c'])) #TypeError: descriptor 'join' requires a 'str' object but received a 'list'

import io
"""
with io.StringIO() as strio:
    for v in ['a','b','c']: strio.write(v)
    print(file=strio)
"""
strio = io.StringIO()
for v in ['aaa','b','c']: strio.write(v)
#print(file=strio)
print(strio.getvalue())
strio.close()
