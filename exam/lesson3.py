# words = "hello world"

# print("good morning")
# print(words)
# print(type(words))

# words2 = 'hello world2'
# print(words2)

# riddle = 'what do you get when you cross hamburger and a computer?'
# answer = input(riddle)

stringphrase = "hello world"
stringlength = len(stringphrase)
print(stringlength)

stringoccorunce = stringphrase.count('h')
print(stringoccorunce)

statement = 'show me the code'
#1 display o
print(statement[13])
#2 display me
print(statement[5:7])

print(f'{stringphrase}{stringlength}')

print(stringphrase.upper())
print(stringphrase.lower())
print(stringphrase.capitalize())
print(stringphrase.title())
print(stringphrase.swapcase())