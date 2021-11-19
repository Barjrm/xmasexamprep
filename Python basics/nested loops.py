#create nested loop
#runs 1 outer loop for entire inner loop
#then outer loop moves up 1 and innter loop completes again
for x in range(4):
    for y in range(4):
        print(f'({x},{y})')


# exercise print letter F

numbers = [5,2,5,2,2]

for number in numbers:
    print(number * '*')

for counter in numbers:
    output = ''
    for count in range(counter):
        output += 'x'
    print(output)


numbers = [2,2,2,7]
for counter in numbers:
    output = ''
    for count in range(counter):
        output += 'L'
    print(output)