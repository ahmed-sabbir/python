num = [1,2,3,4,5,6]
square = [x*x for x in num] # list comprehension
print(square)


square = (x*x for x in num) # creates a generator
print(square)
for x in square:
    print(x)

print('Sum is',sum(x*x for x in num)) # passing the generator expression directly to sum 

print('-------')
print(square)
for x in square:
    print(x)


