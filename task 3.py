data = input()
data = data.split("*")
#print (type(name))
name = data[0]
born = data[1][0:4]
died = data[2][0:4]
age = int(died)-int(born)
#print (age)
#print(died)
print(f"Name: {name}")
print(f"Age: {age}")

