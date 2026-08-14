import module1
print(module1.sum(9 , 10))
print(module1.mul(10 , 9))
print()

import module1 as n
print(n.mul(3 , 5))
print(n.sum(3 , 6))
print()

from module1 import sum
print(sum(2 , 5))
print()

from module1 import *
print(sum(2 ,4))
print(mul(5 , 6))


