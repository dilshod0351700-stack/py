def sonlar(x,y,z):
    son=x
    if son<y:
        son=y
    if son<z:
        son=z
    return son

print('Istalgan butun son kiriting: ')
x=int(input('1-sonni kiriting: '))
y=int(input('2-sonni kiriting: '))
z=int(input('3-sonni kiriting: '))
print(f'Eng katta son = {sonlar(x,y,z)}')