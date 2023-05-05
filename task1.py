a = 3
b = 5
c = a
a = b
b = c
print ("a =",a , "b =",b)

a = 3
b = 5
a, b = b, a
print ("a =",a , "b =",b)

a = 3
b = 5
c = b - a
a = a + c
b = b - c
print ("a =",a , "b =",b)
