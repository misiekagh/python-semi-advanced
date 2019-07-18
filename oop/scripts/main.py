from oop.sports import *

p1=Player('Jan Kowalski', 1000)
p2=Player('Al Bo', 2000)
p3=Player('Joe Smith', 1500)
p4=Player('Jan Kowalski', 1000)
print(p1.__hash__())
print(p2.__hash__())
print(p3.__hash__())
print(p1==p4)
print(p1==p3)
