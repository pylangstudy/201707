class NamedInt(int):
    __slots__ = ['name']
    def __init__(self, name='name'): self.name = name

i = NamedInt()
print(i.name)
