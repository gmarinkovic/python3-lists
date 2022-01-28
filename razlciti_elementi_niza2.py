# Написати програм који учитани низ целих бројева трансформише тако да се свака вредност појављује тачно
# једном у низу, при чему се чува редослед елемената (редослед њиховог првог појављивања).
#
# Улаз: У једној линији стандардног улаза налази се број елемената низа N (0 < N ≤ 10000), а затим се, у
# свакој од N наредних линија стандардног улаза, налази по један члан низа.
#
# Излаз: У свакој линији стандардног излаза исписује се по један елемент трансформисаног низа.
#
# Пример
# Улаз
# 6
# 1
# 3
# 1
# 2
# 3
# 2
# Излаз
# 1
# 3
# 2

# unos elemenata u listu
def unos_niza():
    n = int(input("Unesi broj elemenata niza: "))
    a = [int(input("Unesi element: ")) for i in range(n)]
    return (a, n)

# ispisuje prvih n elemenata liste a
def ispis_niza(a, n):
    for i in range(n):
        print(a[i])

# proverava da li se x nalazi među prvih n elemenata liste a
def pripada(x, a, n):
    for i in range(n):
        if a[i] == x:
            return True
    return False

(a, n) = unos_niza() # učitavamo dužinu i elemente niza
k = 0 # dužina početnog dela niza u koji se smešta rezultat

# sve elemente koji ne pripadaju početnom delu dopisujemo na kraj tog početnog dela
for i in range(n):
    if not(pripada(a[i], a, k)):
        a[k] = a[i]
        k += 1
n = k # dužina skraćenog niza

# ispisujemo konačni rezultat
ispis_niza(a, n)
