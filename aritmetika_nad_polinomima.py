# Дата су два полинома, P и Q степенима и низовима својих коефицијената. Oдредити њихов збир и производ.
#
# Улаз: У првој линији стандардног улаза налази се степен n (0 ≤ n ≤ 20) првог полинома, а у следећих n + 1
# линија реални коефицијенти првог полинома и то редом почев од коефицијента уз највећи степен. Затим се
# на стандардном улазу налази степен m (0 ≤ m ≤ 20) другог полинома, а у следећих m + 1 линија реални
# коефицијенти другог полинома и то редом почев од коефицијента уз највећи степен.
#
# Излаз: Приказати редом збир и производ, сваки у посебној линији. За сваки полином приказати у једној
# линији његове коефицијенте, на две децимале и то редом почев од коефицијента уз највећи степен.
#
# Пример
# Улаз
# 2
# 2
# 1
# 2
# 1
# 1
# -1
# Излаз
# 2.00 2.00 1.00
# 2.00 -1.00 1.00 -2.00

# ucitavanje stepena i koeficijenata polinoma
def unos():
    n = int(input("Unesi stepen polinoma: "))
    P = [float(input("Unesi koeficijent polinoma: ")) for i in range(n + 1)]
    P.reverse()
    return (P, n)


# prikaz koeficijenata polinoma
def prikaz(P, n):
    for i in range(n, -1, -1):
        print(format(P[i], '.2f'), end=" ")
    print()


# zbir polinoma P stepena n i Q stepena m
def zbir(P, n, Q, m):
    s = max(n, m)           # stepen rezultata
    R = [0] * (s + 1)       # koeficijenti rezultata
    for i in range(0, s + 1):
        if i <= n:
            R[i] += P[i]
        if i <= m:
            R[i] += Q[i]
    return (R, s)


# proizvod polinoma P stepena n i Q stepena m
def proizvod(P, n, Q, m):
    s = n + m               # stepen rezultata
    R = [0] * (s + 1)       # koeficijenti rezultata
    for i in range(n + 1):
        for j in range(m + 1):
            R[i + j] += P[i] * Q[j]
    return (R, s)


(P, n) = unos()         # unos prvog polinoma
(Q, m) = unos()         # unos drugog polinoma

# zbir polinoma
(R, s) = zbir(P, n, Q, m)
prikaz(R, s)

# proizvod polinoma
(R, s) = proizvod(P, n, Q, m)
prikaz(R, s)
