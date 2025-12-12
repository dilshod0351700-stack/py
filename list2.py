sonlar=[20,-16,2.0,1.5]
print(sonlar)
print(f"ro\'yxatning -1chi soni = {sonlar[-1]}")                        #index bo'yicha oxiridan oladi
print(f"{sonlar[0]} + {sonlar[1]} = {sonlar[0]+sonlar[1]}\n"            #ro'yxatdagi elementlarda amallar
      f"{sonlar[2]} - {sonlar[3]} = {sonlar[2]-sonlar[3]}\n"
      f"{sonlar[0]} * {sonlar[3]} = {sonlar[0]*sonlar[3]}\n"
      f"{sonlar[1]} / {sonlar[3]} = {sonlar[1]/sonlar[3]}")

sonlar.insert(1,25)    #ro'yxatga index bo'yicha element qo'shish
print("Ro\'yxatning [2] soniga yangi son qo'shildi:",sonlar)
del sonlar[1]
print("(del) ro\'yxatdan [2] soni o\'chirildi: ",sonlar)
sonlar.append(33)
print("Ro\'yxatga 33 soni qo\'shildi",sonlar)



