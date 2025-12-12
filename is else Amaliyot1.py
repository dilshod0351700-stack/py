cars=['tayota','mazda','hyundai','gm','kia']
print('Asl ro\'yxat>>>',cars)
# for car in cars:
#     if car=='gm': print('Natija>>>',car.upper())
#     else:print('Bosh xarf katta-',car.title())
for car in cars:
    if car != 'gm': print('!= teng emas natija-',car.upper())
    else: print('Tenglik natijasi-',car.title())