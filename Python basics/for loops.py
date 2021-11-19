for item in 'python':
    print(item)

print('****************************')

for item in [1,2,'Harry']:
    print(item)

print('****************************')

for item in range(4):
    print(item)

print('****************************')

for item in range(0,2):
    print(item)

print('****************************')

for item in range(2,7,2):
    print(item)

print('****************************')

#exercise forloop calculate costs of shoppinglist

prices = [10, 20, 30]
total = 0
for price in (prices):
    total += price
print(f'the total price for shopping list is {total} kr. ')