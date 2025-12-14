buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           't_yil':810,
           'v_yil':870,
           't_joy':'Buxoro'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           't_yil':1894,
           'v_yil':1938,
           't_joy':'Toshkent'
           }

vohidov = {'ism':'Erkin Vohidov',
           't_yil':1936,
           'v_yil':2016,
           't_joy':"Farg'ona"
           }

navoiy = {'ism':'Alisher Navoiy',
           't_yil':1441,
           'v_yil':1501,
           't_joy':"Xirot"
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs['ism']
    t_yil = shaxs['t_yil']
    v_yil = shaxs['v_yil']
    t_joy = shaxs['t_joy']
    print(f"{ism} {t_yil}-yilda {t_joy}da tavallud topgan. "
          f"{v_yil-t_yil} yil umr ko'rgan.")