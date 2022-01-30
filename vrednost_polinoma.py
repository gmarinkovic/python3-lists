# Са стандардног улаза се уносе степен n и реални коефицијенти полинома y = an · x
# n + an−1 · x
# n−1 + . . . +
# x · a1 + a0. Напиши програм који израчунава вредност тог полинома у k равномерно распоређених тачака
# интервала [p, q].
#
# Улаз: У првој линији стандардног улаза унети n (2 ≤ n ≤ 9) - степен полинома, у следећих n + 1 линија
# реалне вредности коефицијената полинома (редом бројеви an, an−1, . . . a1, a0), затим, у наредној линији k
# (2 ≤ k ≤ 40) - број равномерно распоређених тачака на интервалу [p, q], у наредној линији реалну вредност
# p - почетак интервала, и у наредној линији реалну вредност q - крај интервала.
#
# Излаз: У k линија исписати вредност полинома у равномерно распоређеним тачакама интервала [p, q]
# заокружену на две децимале.
#
# Пример
# Улаз
# 2
# 1.0
# 2.0
# 1.0
# 7
# 1.0
# 7.0
# Излаз
# 4.00
# 9.00
# 16.00
# 25.00
# 36.00
# 49.00
# 64.00

# vrednost polinoma a[n] * x**n + ... + a[1] * x + a[0]
def vrednost_polinoma(a, n, x):
    # Hornerova shema
    y = 0.0
    for i in range(n, -1, -1):
        y = y*x + a[i]
    return y

# učitavamo stepen n i koeficijente polinoma a
n = int(input("Unesi stepen: "))

a = [float(input("Unesi koeficijent polinoma: ")) for i in range(n+1)]
a.reverse()         # koeficijente skladištimo u redosledu an, ..., a0

# učitavamo broj tačaka k i granice intervala p, q
k = int(input("Unesi broj tacaka u rasponu izmedju p i q :"))
p = float(input("Unesi pocetnu granicu intervala p: "))
q = float(input("Unesi krajnju granicu intervala q: "))

# razmak između susednih tačaka
h = (q - p) / (k - 1)

x = p                   # tekuća tacka, krećemo od levog kraja p
for i in range(k):      # izračunavamo vrednost u k tačaka
    print(format(vrednost_polinoma(a, n, x), '.2f'))
    x += h              # prelazimo na narednu tačku
