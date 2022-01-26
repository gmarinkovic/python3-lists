# Сеф се отвара тако што се унесе комбинација цифара.
# Напиши програм који проверава да ли је унета комбинација тачна и да ли сеф треба да се отвори.
#
# Улаз: Са стандардног улаза се учитава број n (1 ≤ n ≤ 100) а затим и тачна комбинација од n цифара
# (све цифре су задате у једном реду и раздвојене су размацима).
# Након тога се уноси комбинација од n цифара коју је корисник сефа унео (свака цифра задата је у посебном реду).
#
# Излаз: На стандардни излаз исписати da ако је комбинација тачно погођена, тј. ne у супротном.
#
# Пример
# Улаз
# 3
# 1 2 3
# 1
# 2
# 3
# Излаз
# da

def jednaki(a, b):
    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

n = int(input("Unesi koliko cifara ima sifra sefa: "))

a = list(map(int, input("Unesi sifru sefa u brojkama: ").split()))

b = [int(input("Unesi cifru: ")) for i in range(n)]

if jednaki(a, b):
    print("da")
else:
    print("ne")
