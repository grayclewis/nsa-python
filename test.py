print('Hello World')
print(dir())

a = [1, 2, 3, 4, 5]
print(a[3])

print(7 % 2)
print(7 ** 2)
print(min(2, 7))
print(max(2, 7))
print(dir("a"))
print(abs(-1))
print(round(1.2))
print(len("123456"))

from os import listdir
print(listdir())

import os
print(dir(os))
print(os.name)
print(os.listdir())

import sys
print(dir(sys))
print(sys.argv)

import random
print(random.randint(1, 10))

def add(a, b):
    return a + b

print(add(5, 6))




