# Написати програм који израчунава скаларни производ два вектора чије се координате уносе са стандардног
# улаза. Скаларни производ два вектора је збир производа њихових одговарајућих координата (скаларни производ вектора
# (a1, . . . , an) и (b1, . . . , bn) једнак је a1 · b1 + . . . + an · bn. Димензија вектора није унапред
# позната, али није већа од 50.
#
# Улаз: У првој линији стандардног улаза задата је димензија вектора n (2 ≤ n ≤ 50). Након тога, у n
# наредних линија се уносе координате првог вектора, а након тога, у n наредних линија се уносе координате
# другог вектора.
#
# Излаз: Исписати вредност скаларног производа првог и другог вектора на стандардни излаз.
#
# Пример 1
# Улаз
# 3
# 1
# 2
# 3
# 3
# 2
# 1
# Излаз
# 10

# dimenzija vektora
n = int(input())

a = [int(input()) for i in range(n)]    # ucitavanje prvog vektora
b = [int(input()) for i in range(n)]    # ucitavanje drugog vektora

# izracunavanje skalarnog proizvoda
skalarniProizvod = 0
for i in range(n):
    skalarniProizvod += a[i]*b[i]       # 1*3 + 2*2 + 3*1
    
# ispis resenja
print(skalarniProizvod)
