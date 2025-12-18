def aylana_info(radius,pi=3.14):
    aylana={
        'radius':radius,
        'diametr':2*radius,
        'perimetr':2*pi*radius,
        'yuzi':pi*radius**2
    }
    return aylana
print('Arlana radiusini kiriting: ')
radius=float(input('Radius: '))
print(aylana_info(radius,pi=3.14))
