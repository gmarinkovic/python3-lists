# Написати програм којим се одређује збир n датих целих бројева.
#
# Улаз: У првој линији стандардног улаза налази се природан број n (1 ≤ n ≤ 1000). У свакој од наредних n
# линија налази се по један цео број xi.
#
# Излаз: У првој линији стандарног излаза приказати збир унетих n целих бројева x1, . . . , xn.
#
# Пример
# Улаз
# 4
# 10
# -3
# 2
# 4
# Излаз
# 13

n = int(input("Unesi broj elemenata liste: "))                        # broj brojeva
a = (int(input("Unesi elemenet: ")) for i in range(n))    # učitavamo n brojeva
zbir = sum(a)                           # određujemo i ispisujemo njihov zbir
print(zbir)
