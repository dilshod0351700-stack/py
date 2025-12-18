def kvadrat_kub(son_1,son_2):
    if son_1>son_2:
                   print(f'{son_1} > {son_2}')
    elif son_1<son_2:
                   print(f'{son_1} < {son_2} ')
    else:
                   print(f'{son_1}={son_2}')


son_1 = int(input('Istalgan butun son kiriting-'))
son_2 = int(input('Istalgan butun son kiriting-'))
kvadrat_kub(son_1,son_2)