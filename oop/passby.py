class A:
    def __init__(self):
        print(id('AAA'))


def to_upper(string):
    print(id(string))
    string=string.upper()
    print(id(string))

s='Hello World'
print(id(s))
to_upper(s)
class A:
    def __init__(self):
        print(id('AAA'))


def to_upper(string):
    print(id(string))
    string=string.upper()
    print(id(string))

s='Hello World'
print(id(s))
to_upper(s)
