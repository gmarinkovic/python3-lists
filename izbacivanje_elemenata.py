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

n = int(input("Unesi broj elemenata: "))
a = [int(input("Unesi element: ")) for i in range(n)]
# ponavljamo sledeći postupak
while True:
    # elemente koji ne dele dužinu liste prebacujemo na njen početak
    k = 0
    for i in range(n):
        if n % a[i] != 0:
            a[k] = a[i]
            k += 1
    # ako se lista nije skratila, prekidamo petlju
    if n == k:
        break;
    # izbacujemo elemente koji nisu prebačeni
    n = k

# izračunavamo i ispisujemo zbir preostalih elemenata
zbir = 0
for i in range(n):
    zbir += a[i]

print(zbir)
