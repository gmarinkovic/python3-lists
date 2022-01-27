# Дате су координате n тачака у равни. Транслирати тачке тако да им тежиште буде у координатном почетку.
#
# Улаз: У првој линији стандардног улаза налази се природан број n (1 ≤ n ≤ 100). У следећих n линија
# налазе се по два реална броја, који представљају x и y координате тачака.
#
# Излаз: На стандардном излазу приказати координате тачака после транслације, за сваку тачку у једној линији
# њену x па y координату, координате одвојити једном празнином и приказати их на две децимале.
#
# Пример
# Улаз
# 3
# 0 0
# 1 0
# 2 3
# Излаз
# -1.00 -1.00
# 0.00 -1.00
# 1.00 2.00

# učitavamo podatke o tačkama
n = int(input("Unesi broj tacaka: "))
x = []
y = []
for i in range(n):
    s = input("Unesi koordinate tacke: ").split()
    x.append(float(s[0]))
    y.append(float(s[1]))

# određujemo poziciju težišta
xT = 0
yT = 0
for i in range(n):
    xT += x[i]
    yT += y[i]
xT /= n  # Tezisna pozicija po x-osi
yT /= n  # Tezisna pozicija po y-osi

# transliramo tačke
for i in range(n):
    x[i] -= xT
    y[i] -= yT

# ispisujemo rezultat
for i in range(n):
    print(f'{x[i]:.2f} {y[i]:.2f}')
