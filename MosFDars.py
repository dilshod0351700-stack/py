# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2))
#2dars
# def summa(*sonlar):
#     return sum(sonlar)
# print(summa(4,5,6,7))
#3dars
def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto2)