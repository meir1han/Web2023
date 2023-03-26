from math import sqrt

a = int(input())
b = int(input())

for i in range(a, b):
    s = int(sqrt(i))
    if s*s==i:
        print(i, end=" ")