numbers = input("Enter three digit number: ")
first_number = numbers[0]
second_number = numbers[1]
third_number = numbers[2]
sum = int(first_number) + int(second_number) + int(third_number)
print("sum: ", sum)

numbers = int(input("Enter three digit number: "))
print(numbers//100 + numbers//10%10 + numbers%10)
