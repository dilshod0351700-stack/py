def kopaytma(*sonlar):
    son1=1
    for son in sonlar:
      son1*=son
    return son1

print(kopaytma(4,5))