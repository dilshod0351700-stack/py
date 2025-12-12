juft_sonlar=[]
juft_sonlar=list(range(120,1200,2)) #120 dan 1200 gacha bo'lgan juft sonlar ro'yxati
print(juft_sonlar)
juft_sonlar_summasi=sum(juft_sonlar)
print('Ro\'xatdagi juft_sonlar yig\'indi SUM = ',juft_sonlar_summasi)
juft_sonlar_max=max(juft_sonlar)
juft_sonlar_min=min(juft_sonlar)
print(f'Ro\'yxatdagi juft sonlar max = {juft_sonlar_max}\n'
      f'Ro\'yxatdagi juft sonlar min = {juft_sonlar_min}\n'
      f' max - min = {juft_sonlar_max-juft_sonlar_min}\n'
      f'Ro\'yxatdagi juft_sonlar soni = {len(juft_sonlar)} dona')
urtadagi_sonlar=len(juft_sonlar)
print(f'juft_sonlar ro\'yxati boshidagi 20 ta sonlari={juft_sonlar[:20]}')
a=int(urtadagi_sonlar)
b=a/2-10
c=a/2+10
d=a-20
print(f'juft_sonlar ro\'yxatning o\'rtasidagi 20 ta soni={juft_sonlar[int(b):int(c)]}\n'
      f'juft_sonlar ro\'yxatidagi oxirgi 20 ta soni={juft_sonlar[int(d):]}')

