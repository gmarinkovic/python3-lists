# Број је непожељан у низу целих бројева ако дели укупан број елемената (нпр. у низу дужине 10 су непожељни
# елементи који деле број 10, а то су 1, 2, 5 и 10). Потребно је пронаћи све непожељне елементе у низу и
# уклонити их. Након тога се број елемената може променити и неки други елементи могу постати непожељни.
# Поступак се понавља док се не добије низ без непожељних елемената. Напиши програм који за дати низ
# одређује збир преосталих елемената, након уклањања непожељних.
#
# Улаз: Са стандардног улаза се уноси број n (1 ≤ n ≤ 50000), а затим и n елемената низа из распона од 1 до
# 100.
#
# Излаз: На стандардни излаз исписати један цео број који представља збир преосталих елеманата у низу,
# након узастопног уклањања свих непожељних елемената.
#
# Пример
# Улаз
# 7
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# Излаз
# 9


# učitava niz
def ucitaj_niz():
    n = int(input("Unesi broj elemenata: "))
    a = [int(input("Unesi element: ")) for i in range(n)]
    return a

# izbacuje sve elemente niza koji dele broj x
def izbaci_delioce(a, x):
    b = []
    for y in a:
        if x % y != 0:
            b.append(y)
    return b

a = ucitaj_niz()  # učitavamo sve elemente u niz
while True:  # ponavljamo sledeći postupak
    n0 = len(a)  # pamtimo početnu dužinu niza
    a = izbaci_delioce(a, n0)  # izbacujemo sve delioce te dužine
    if n0 == len(a):  # ako se dužina nije promenila
        break;  # prekidamo petlju

print(sum(a))  # ispisujemo zbir preostalih elemenata
