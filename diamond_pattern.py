r = 5
for i in range(1, r +1):
    #Print spaces
    for j in range(r - i):
        print(" ", end = " ")
        #Print Stars
    for k in range(2 * i - 1):
        print("*", end = " ")
    print()

for i in range(r - 1, 0, -1):
    #Print spaces
    for j in range(r -i):
        print(" ", end = " ")
        #Print Stars
    for k in range(2 * i - 1):
        print("*", end = " ")
    print()
