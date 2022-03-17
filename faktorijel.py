# Дате су цифре 1, 2, . . . , n.
# Напиши програм који израчунава колико се различитих n-тоцифрених бројева
# састављених од свих тих цифара може направити
# (на пример, од цифара 1, 2, 3 могу се направити бројеви 123, 132, 213, 231, 312 и 321).
#
# Напомена: Број пермутација скупа од n елемената једнак је факторијелу броја n тј. броју n! = 1 · 2 · . . . · n.
# Размисли зашто је баш тако.
#
# Улаз: Прва линија стандарног улаза садржи природан број n (1 ≤ n ≤ 9).
#
# Излаз: У првој линији стандарног излаза приказати број различитих бројева који се могу направити од
# цифара 1, 2, . . . , n.
#
# Пример 1
# Улаз
# 5
# Излаз
# 120
# Пример 2
# Улаз
# 9
# Излаз
# 362880

from functools import reduce

# proizvod dva broja
def prod_2(x, y):
    return x * y

# proizvod kolekcije
def prod(kolekcija):
    return reduce(prod_2, kolekcija)

n = int(input("Uneti broj elemenata liste: "))

faktorijel = prod(range(1, n+1))        # proizvod raspona brojeva [1, n+1)

print("Broj razlicitih brojeva sa ",n, "cifara je ",faktorijel)
