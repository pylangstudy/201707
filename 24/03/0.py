class Reader:
    async def readline(self): print('readline')
    def __aiter__(self): return self
    async def __anext__(self):
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

async for a in Reader():
    print(a)
else:
    print('else')
