# Миља је енглеска историјска мера за дужину која износи 1609.344 m. Напиши програм који исписује таблицу
# прерачунавања миља у километре.
#
# Улаз: Са стандардног улаза се уносе цели бројеви a (1 ≤ a ≤ 10), b (10 ≤ b ≤ 100) и k (1 ≤ k ≤ 10).
#
# Излаз: На стандардни излаз исписати табелу конверзије миља у километре за сваки број миља из интервала
# [a, b], са кораком k. Број километара заокружити на 6 децимала, а табелу приказати у формату идентичном
# као у примеру.
#
# Пример
# Улаз
# 10
# 20
# 2
# Излаз
# 10 mi = 16.093440 km
# 12 mi = 19.312128 km
# 14 mi = 22.530816 km
# 16 mi = 25.749504 km
# 18 mi = 28.968192 km
# 20 mi = 32.186880 km

kilometara_u_milji = 1.609344
a = int(input("Unesi pocetnu vrednost intervala u miljama: "))
b = int(input("Unesi kranju vrednost intervala u miljama: "))
korak = int(input("Unesi korak: "))

milje = []
for i in range(a, b + 1, korak):
    milje.append(int(i))

print(milje)
print()
for i in range(len(milje)):
    print(f'{milje[i]} mi = {(milje[i] * kilometara_u_milji):.6f} km')
