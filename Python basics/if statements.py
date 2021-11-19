# hot = False
# cold = False
# if hot:
#     print('Its a hot day')
#     print('Drink plenty of water. ')
# elif cold:
#     print('Its a cold day. ')
#     print('Wear warm clothes. ')

# else:
#     print('Its a lovely day. ')    
# print('Have a nice day. ')


#credit check if elif else

house = 1000000
house_good = 0.1 * house
house_bad = 0.2 * house
good_credit = True
bad_credit = False

if good_credit:
    print(f'The price is ${house} ')
    print(f'Your downpayment is  ${house_good}')
elif bad_credit:
    print(f'the price is ${house} ')
    print(f'Your downpayment is ${house_bad}')
print('The bank always wins. ')
