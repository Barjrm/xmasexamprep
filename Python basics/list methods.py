# numbers = [1,2,3,4,6]
# numbers.append(24)
# print(numbers)

# numbers = [1,2,3,4,6]
# numbers.insert(0,55)
# print(numbers)

# numbers = [1,2,3,4,6]
# numbers.remove(6)
# print(numbers)

# numbers = [1,2,3,4,6]
# numbers.clear()
# print(numbers)

# numbers = [1,2,3,4,6]
# numbers.pop()
# print(numbers)

# numbers = [1,2,3,4,6]
# print(numbers.index(6))

# numbers = [1,2,3,4,6,6]
# print(numbers.count(6))

# numbers = [1,2,3,4,6,6]
# numbers.sort()
# print(numbers)

# numbers = [1,2,3,4,6,6]
# numbers.reverse()
# print(numbers)

# numbers = [1,2,3,4,6,6]
# numbers2 = numbers.copy()
# print(numbers2)

# exercise remove duplicates in a list

numbers = [1,2,3,4,6,6]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
        
print(uniques)