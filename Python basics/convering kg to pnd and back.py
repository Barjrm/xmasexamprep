weight = int(input('Enter weight: '))
lbs_kg = input('Enter (L)bs or (K)g. ')

if lbs_kg.upper() == 'L':
    new_weight = weight * 0.45
    print(f'{weight} pounds, is {new_weight} kg. ')
    
elif lbs_kg.upper() == 'K':
    new_weight = weight / 0.45
    print(f'{weight} in kg, is {new_weight} pounds. ')