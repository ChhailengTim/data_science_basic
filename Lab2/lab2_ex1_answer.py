print('Kilograms\tPounds')
print('-' * 25)
for kg in range(1, 200, 2):
    print('{:<15} {:<10}'.format(kg, kg * 2.2))
