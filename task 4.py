numbers = int(input())
first_number = numbers//100
second_number = numbers//10%10
third_number = numbers%10
#print(first_number, second_number, third_number)
suma = first_number+second_number+third_number
print (suma)

numbers = int(input())
print (numbers//100+numbers//10%10+numbers%10)