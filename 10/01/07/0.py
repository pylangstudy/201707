class Class:
    def __init__(self, class_=0): self.__class = class_
    def __str__(self):
        if 0 >= self.__class: return '平社員'
        elif 1 == self.__class: return '部長'
        else: return '社長'
    def __lt__(self, other): return self.__class < other._Class__class

c0 = Class(class_=0)
c1 = Class(class_=1)
c2 = Class(class_=2)
print(c0, c1, c2)
print(c0 < c1)
print(c1 < c0)
