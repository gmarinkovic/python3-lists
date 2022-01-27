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


# učitava niz parova koordinata tačaka
def ucitaj_tacke():
    n = int(input("Unesi broj tacaka: "))
    tacke = []
    for i in range(n):
        s = input("Unesi koordinate tacke: ").split()
        tacke.append([float(s[0]), float(s[1])])
    return tacke


# ispisuje niz koordinata tačaka
def ispisi_tacke(tacke):
    for tacka in tacke:
        print(f'{tacka[0]:.2f} {tacka[1]:.2f}')


# određuje težište niza tačaka
def teziste(tacke):
    xT = 0.0
    yT = 0.0
    for tacka in tacke:
        xT += tacka[0]
        yT += tacka[1]
    n = len(tacke)
    return (xT / n, yT / n)


# translira niz tačaka za vektor (vx, vy)
def transliraj(tacke, vx, vy):
    for tacka in tacke:
        tacka[0] += vx;
        tacka[1] += vy


tacke = ucitaj_tacke()
(xT, yT) = teziste(tacke)
transliraj(tacke, -xT, -yT)
ispisi_tacke(tacke)
