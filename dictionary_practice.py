d = {
    'name' : 'Ali',
    'age' : 22,
    'course' : 'Python'
}
print(d)
#Access value
print(d['name'])
print(d['age'])
print()

for n in d:
    print(n)   # only return keys
    print(d[n]) # return keys and values
    print()

# Dictionary Method
d['age'] = 25         # update age
d['city'] = 'Gujranwala' # add
d['semester'] = 5
d.pop("semester")   #remove


    # Loop through both keys and values simultaneously using the items() method
for key, value in d.items():
    print(key, ":", value)

