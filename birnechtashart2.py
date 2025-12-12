yosh=int(input('Yoshingiz nechida? '))
if yosh<=4:
    price=0
elif yosh<=12:
    price=5000
else:
    price=10000
print(f'Sizga kirish {price} so\'m')