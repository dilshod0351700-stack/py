def foydalanuvchi():
    malumot={
        'ism':ism,
        'familiya':familiya,
        't_yil':t_yil,
        't_joy':t_joy,
        'emel':emel,
        'tel':tel}
    return malumot
print('Foydalanuvchi ma\'lumotlarini shakillantirish')
f_malumot=[]
while True:
    print("\nQuydagi ma\'lumotlarni kiriting: \n")
    ism=input('Ismingiz: ')
    familiya=input('Familiyangiz: ')
    t_yil=input('Tug\'ulgan yilingiz: ')
    t_joy=input('Tug\'ulgan joyingiz: ')
    print('Emailingiz bormi?')
    h=input('H/Y')
    if h=='h':
        emel=input('Emelingiz: ')
    else:
        emel='yo\'q'
    print('Telfon raqamingiz bormi?')
    hh=input('H/Y')
    if hh=='h':
         tel=input('Telfon raqamingiz: ')
    else:
         tel='yo\'q'
    f_malumot.append(foydalanuvchi())
    javob=input('Yana foydalanuvchi kiritasizmi (H/Y)?:')
    if javob == 'y':
        break
print('Foydalanuvchilar:\n')
for mijoz in f_malumot:
    print(f'Ismi:{mijoz['ism'].title()}\n'
          f'Familiya:{mijoz["familiya"].title()}\n'
          f'Tug\'ulgan yil:{mijoz['t_yil']} yil\n'
          f'Emel:{mijoz["emel"]}\n'
          f'Telfon raqam:{mijoz["tel"]}')