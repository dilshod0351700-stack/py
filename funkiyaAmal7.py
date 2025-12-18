def kvadrat_kub(son_1):
    for s in range(2,11):
        if not son_1 % s:
            print(f'{son_1}  {s}  ga qoldiqsiz bo\'linadi!')
son_1 = int(input('Istalgan butun son kiriting-'))

kvadrat_kub(son_1)