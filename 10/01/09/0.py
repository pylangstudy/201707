class Switch:
    def __init__(self, switch=False):
        self.__switch = switch
    def switch(self): self.__switch = not(self.__switch)
    def __bool__(self): return self.__switch

s = Switch()
print(s.__bool__())
s.switch()
print(s.__bool__())
