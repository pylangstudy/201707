s = [b'a', b'b', b'c']
print(s)
#print(bytes.join(s))#TypeError: descriptor 'join' requires a 'bytes' object but received a 'list'
print(b''.join(s))

import io
byteio = io.BytesIO()
for v in s: byteio.write(v)
print(byteio.getvalue())
byteio.close()
