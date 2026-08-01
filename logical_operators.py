x = 10
y = 20

# and operator (Both conditions must be True)
print("Using AND:", (x < y) and (y > 15))
print("Using AND:", (x != 10) and (y > x))

# or operator ( At least one condition must be True)
print("Using OR:", (y > 20) or (x > y))
print("Using OR:", (x >= 15) or (y > 18))

# not operator (Reverse the result)
print("Using NOT:", not(x >= y))
print("Using NOT:", not(x <= y))

