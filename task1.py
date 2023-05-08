a = 3
b = 5
c = a
a = b
b = c
print("a =", a, "b =", b)

a = 3
b = 5
a, b = b, a
print("a =", a, "b =", b)

a = 3
b = 5
a = a + b #8
b = a - b  #3
a = a - b
print("a =", a, "b =", b)
