# Написати програм који учитава низ целих бројева а затим га трансформише тако што се циклично померају
# задати делови низа од позиције p до позиције q све док се не унесу две једнаке позиције. При томе вршити
# циклично померање удесно ако је p < q, а померње улево вршити ако је p > q.
#
# Улаз: У једној линији стандардног улаза налази се број елемената низа n (1 < n ≤ 200), а затим се, у свакој
# од n наредних линија стандардног улаза, налази по један члан низа. У наредним редовима се уносе по два
# цела броја, p и q (0 ≤ p, q < n), одвојена празнином док се не унесе ред у коме су бројеви једнаки.
#
# Излаз: У свакој линији стандарног излаза исписује се по један елемент трансформисаног низа.
#
# Пример
# Улаз
# 4
# 1
# 2
# 3
# 4
# 2 3
# 2 0
# 1 2
# 0 0
# Излаз
# 2
# 1
# 4
# 3

def unos_niza():
    n = int(input("Unesi broj elmenata niza: "))
    return [int(input("Unesi element: ")) for i in range(n)]


def ispis_niza(a):
    for x in a:
        print(x)


# obrtanje dela niza izmedju pozicija p i q (ukljucujuci i njih)
def ciklicno_pomeri(a, p, q):
    m1 = p
    m2 = q

    if p < q:                       # pomeraj u desno
        pom = a[q]
        for i in range(m2, m1, -1):
            a[i] = a[i - 1]
        a[m1] = pom
    else:
        pom = a[q]                  # pomeraj u levo
        for i in range(m2, m1):
            a[i] = a[i + 1]
        a[m1] = pom


# ucitavamo niz
a = unos_niza()

while True:
    # ucitavamo interval [p, q] koji treba obrnuti
    (p, q) = map(int, input("Unesi parove za mogucu rotaciju: ").split())
    # ako je interval prazan, prekidamo postupak
    if p == q:
        break;
    # vrsimo obrtanje
    ciklicno_pomeri(a, p, q)

# ispisujemo rezultat
ispis_niza(a)
