# 1 dars
# cars_0={'model':'ferrari','rang':'qizil'}
# print(cars_0['model'])
# print(cars_0['rang'])
#2dars
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")
# #3dars
# talaba_0['kurs']=4
# talaba_0['fakultet']='Informatika'
# print(talaba_0)
#4dars
# talaba_1={}
# talaba_1['ism']='qobil rasulov'
# talaba_1['kurs']=3
# talaba_1['yosh']=20
# print(talaba_1)
# print(f'{talaba_1['ism'].title()} {talaba_1["kurs"]}-kurs')
# talaba_1['kurs']=4
# print(f'{talaba_1['ism'].title()} {talaba_1["kurs"]}-kurs')
#5dars
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
# phone=telefonlar['ali']
# print(f'Alining telfoni  {phone}')
# phone=telefonlar['hasan']
# print(f'Hsanning telfoni  {phone}')
phone=telefonlar.get('hasan','Bunday ism mavjud emas')
print(phone)
