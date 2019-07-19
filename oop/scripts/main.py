from oop.sports import *
from oop.multihash import MultiHash
from random import randint
from oop.timefunc import timeit

@timeit
def findstr(str):
    for _ in range(10000):
        if str in mh:
            pass


p1=Player('Jan Kowalski', 1000)
p2=Player('Al Bo', 2000)
p3=Player('Joe Smith', 1500)
p4=Player('Jan Kowalski', 1000)
print(p1.__hash__())
print(p2.__hash__())
print(p3.__hash__())
print(p1==p4)
print(p1==p3)

print(''.join(map(lambda x:x.lower(), 'Hello World')))

mh=MultiHash()
for a in range(100):
    mh.add(chr(randint(65,90)))

print(mh)

findstr('T')