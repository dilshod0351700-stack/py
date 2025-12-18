def fibonacci(x):
    sonlar=[]
    for n in range(x):
        if n == 0 or n == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[n - 1] + sonlar[n - 2])
    return sonlar


print('Fibonichchining nechinchi sonini ko\'rmoqchisiz:')
x=int(input('x: '))
print(fibonacci(x))
