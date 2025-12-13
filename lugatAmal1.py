otam={'ism':'ravshan','t_yil':1962,'shaxar':'Toshkent shaxri'}
onam={'ism':'nodira','t_yil':1967,'shaxar':'Toshkent shaxri'}
ukam={'ism':'sherzod','t_yil':1987,'shaxar':'Toshkent shaxri'}
singil_1={'ism':'zilola','t_yil':1989,'shaxar':'Toshkent shaxri'}
singil_2={'ism':'komola','t_yil':1992,'shaxar':'Toshkent shaxri'}
print(f'Otam {otam['ism'].title()} {otam["t_yil"]} yilda, {otam['shaxar']}da tug\'ulgan\n'
       f'Onam {onam['ism'].title()} {onam["t_yil"]} yilda, {onam['shaxar']}da tug\'lgan\n'
      f'Ukam {ukam['ism'].title()} {ukam['t_yil']} yilda, {ukam['shaxar']}da tug\'ulgan\n')
taomlar = {
    'otam':'osh',
    'onam':'shashlik',
    'ukam':"lag'mon",
    'singil_1':"mastava",
    'singil_2':"somsa"
    }

taom = taomlar['otam']
print(f"Otamning sevimli taomi {taom}")


