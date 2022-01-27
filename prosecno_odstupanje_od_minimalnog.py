# Дате су цене уређаја у n продавница. Написати програм којим се одређује колико су у просеку цене уређаја
# скупље од најмање цене уређаја у тим продавницама.
#
# Улаз: У првој линији стандардног улаза налази се природан број n (1 ≤ n ≤ 200). У следећих n линија
# налазе се позитивни реални бројеви који представљају цене уређаја у продавницама.
#
# Излаз: На стандардном излазу приказати на две децимале заокружено просечно одступање цена од минималне цене.
#
# Пример
# Улаз
# 4
# 100
# 95
# 120
# 95
# Излаз
# 7.50

n = int(input("Unesi broj cena za uredjaja koji se kontrolise po prodavnicama: "))
a = [int(input("Unesi cenu uredjaja: ")) for i in range(n)]

minimum = min(a)

suma = sum(a)
prosecna_cena = suma / n

prosecno_odstupanje_od_minimalne_cene = prosecna_cena - minimum

print("Prosecnòdstupanje od minimalne cene je: "+"{:.2f}".format(prosecno_odstupanje_od_minimalne_cene))
