# Ђаци увежбавају сабирање троцифрених бројева. Учитељица диктира задатак редом цифру по цифру.
# Напиши програм који на основу учитаних цифара израчунава и исписује тражени збир.
#
# Улаз: У шест линија стандардног улаза задато је шест цифара.
#
# Излаз: На стандардни излаз исписати један цео број - тражени збир.
# Пример
# Улаз
# 1
# 2
# 3
# 4
# 5
# 6
# Излаз
# 579

# ucitavamo sve cifre
a = [int(input("Unesi cifru prvog broja: ")) for i in range(3)]
a.reverse()

b = [int(input("Unesi cifru drugog broja: ")) for i in range(3)]
b.reverse()

z = [0, 0, 0, 0]

# sabiramo cifre odmah vrseci prenos
prenos = 0
for i in range(3):
    zbirCifara = a[i] + b[i] + prenos
    z[i] = zbirCifara % 10
    prenos = zbirCifara // 10

z[3] = prenos

# ispisujemo rezultat preskacuci vodece nule
j = 3
while j > 0 and z[j] == 0:
    j -= 1
while j >= 0:
    print(z[j], end="")
    j -= 1
print()
