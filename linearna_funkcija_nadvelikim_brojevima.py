# У великом броју језика основни типови података (нпр. int) могу исправно да представе само ограничен
# распон бројева. Напиши програм који израчунава вредност функције a · x + b, ако су a, b и x јако велики
# цели бројеви.
#
# Улаз: Са стандардног улаза се учитавају три цела броја a, b и x (са најмање 3, а највише 100 цифара), сваки
# у посебној линији.
#
# Излаз: На стандардни излаз исписати вредност израза a · x + b.
#
# Пример
# Улаз
# 123456789
# 987654321
# 999999999
# Излаз
# 123456789864197532

def normalizuj(c):
    n = len(c)
    for k in range(n - 1):
        c[k + 1] += c[k] // 10
        c[k] %= 10
    if c[n - 1] == 0:
        del c[n - 1]

def saberi(a, b):
    na = len(a)
    nb = len(b)
    n = max(len(a), len(b))
    c = [0] * (n + 1)
    for i in range(n):
        c[i] = 0
        if i < na:
            c[i] += a[i]
        if i < nb:
            c[i] += b[i]
    normalizuj(c)
    return c

def pomnozi(a, b):
    na = len(a);
    nb = len(b)
    n = na + nb
    c = [0] * n
    for i in range(na):
        for j in range(nb):
            c[i + j] += a[i] * b[j]
    normalizuj(c)
    return c

def pisiBroj(broj):
    rez = []
    for i in range(len(broj) - 1, -1, -1):
        rez.append(chr(ord('0') + broj[i]))
    return "".join(rez)

def citajBroj():
    s = input("Unesi broj: ")
    n = len(s)
    rez = [ord(s[n - 1 - i]) - ord('0') for i in range(n)] # belezi pozicije u ASCII
    return rez

a = citajBroj()
b = citajBroj()
x = citajBroj()
print(pisiBroj(saberi(pomnozi(a, x), b)))
