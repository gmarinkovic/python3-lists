# Написати програм којим се уноси n целих бројева, а затим се унети бројеви приказују у обратном редоследу
# од редоследа уношења
#
# Улаз: У првој линији стандардног улаза налази се природан број n (1 ≤ n ≤ 1000). У следећих n линија
# налазе се цели бројеви између -1000 и 1000.
#
# Излаз: На стандардном излазу приказати унете бројеве, сваки у посебној линији, у обратном редоследу од
# редоследа уношења.
#
# Пример
# Улаз
# 5
# 10
# -123
# 67
# 14
# 987
# Излаз
# 987
# 14
# 67
# -123
# 10

n = int(input("Unesi broj elemenata liste: "))

lista = []

for i in range(n):
    lista.append(int(input()))

print()

for i in range(n-1,-1,-1):
    print(lista[i])
