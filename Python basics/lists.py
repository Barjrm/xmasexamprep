names = ["Joey", "Chandler","Ross","Monica"]
print(names[0])
print(names[-1])
print(names[0:2])
print(*names)

names[0] = 'Stalin'
names[-1] = 'Churchill'
print(names)

print('************************')

#exercise find largest number in a list

numbers = [1,45,4,245]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number 
print(max)