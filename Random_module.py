import random
n = random.randint(3,9)
print(n)

n1 = random.randrange(2,8)
print(n1)

l = [100,200,300,400,500,600]
lc = random.choice(l)
print(lc)
# OR
print(random.choice(l))

r = random.random()
print(r)

l2 = [10,20,30,40,50]
random.shuffle(l2)
print(l2)

u = random.uniform(1,7)
print(u)