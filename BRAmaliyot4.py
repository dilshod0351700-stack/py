mahsulotlar=['olma','uzum','nok','ananas','banan','kivi','anjir','tarvuz','shaftoli','gilos']
savat=[]
for n in range(5):
    savat.append(input(f'{n+1} maxsulotni yozing : '))
for savat in mahsulotlar:
    if mahsulot in savat:
        print(f'{savat}  bor')
    else:print('rrrr')