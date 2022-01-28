# Написати програм који учитава низ целих бројева a затим га трансформише тако што се окрећу задати делови
# низа, од елемента са индексом p до елемента са индексом q, све док се не унесе пар бројева, p и q, у коме је
# p веће од q.
#
# Улаз: У једној линији стандардног улаза налази се број елемената низа, природан број N (2 ≤ N ≤ 10000), а
# затим се, у свакој од N наредних линија стандардног улаза, налази по један члан низа. У наредним редовима
# (њих највише N) се уносе по два цела броја p и q (0 ≤ p ≤ q < N), одвојена празнином док се не унесе ред
# у коме је први број већи од другог.
#
# Излаз: У свакој линији стандардног излаза исписује се по један елемент трансформисаног низа.
#
# Пример
# Улаз
# 4
# 1
# 2
# 3
# 4
# 0 1
# 2 3
# 0 3
# 1 0
# Излаз
# 3
# 4
# 1
# 2

def unos_niza():
    n = int(input("Unesi broj elmenata niza: "))
    return [int(input("Unesi element: ")) for i in range(n)]

def ispis_niza(a):
    for x in a:
        print(x)

# obrtanje dela niza izmedju pozicija p i q (ukljucujuci i njih)
def obrni(a, p, q):
    i = p
    j = q
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

# ucitavamo niz
a = unos_niza()

while True:
    # ucitavamo interval [p, q] koji treba obrnuti
    (p, q) = map(int, input("Unesi parove za mogucu rotaciju: ").split())
    # ako je interval prazan, prekidamo postupak
    if p > q:
        break;
    # vrsimo obrtanje
    obrni(a, p, q)

# ispisujemo rezultat
ispis_niza(a)
