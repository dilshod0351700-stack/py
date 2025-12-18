# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.
# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol='Istalgan sonni kiriting'
# savol+='Dasturni to\'xtatish uchun "exit" so\'zini yozing'
# qiymat=''
# while qiymat!='exit':
#     qiymat=input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")