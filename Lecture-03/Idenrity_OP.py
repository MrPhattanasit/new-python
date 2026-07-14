#Example of the identity operator

# Two variable pointing to the same list object
a = [1,2,3]
b = a

# Two variable pointing to different list objects with the same content
c = [1,2,3]
d = [1,2,3]

#Using the identity Operator
print(a is b)
print(a is c)
print(c is d)


print(a == c)
print(c == d)