# temp = 30

# if temp > 30:
#     print("It's a hot day. ")
# if temp == 30:
#     print("It's a warm day. ")
# if temp <30:
#     print("It's a cold day. ")


# name

name = input('Enter a name: ')

if len(name) <= 3:
    print('name must be larger than 3 characters. ')
elif len(name) >= 50:
    print('name cannot be 50 characters. ')
else:
    print('name looks good')