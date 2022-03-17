# Три аутомобила стартних бројева 1, 2, 3 крећу са исте стартне позиције редом у тренуцима t1, t2, t3
# (0 ≤ t1 < t2 < t3), и крећу се константним брзинама v1, v2, v3.
# Написати програм којим одређујемо тренутак кад се деси последње претицање, или ако нема претицања исписати текст nema.
#
# Улаз: Са стандардног улаза учитава се 6 реалних бројева. Прва линија садржи бројеве t1, v1, друга бројеве
# t2, v2, а трећа бројеве t3, v3.
#
# Излаз: На стандардни излаз исписати један реалан број који представља време последњег претицања,
# заокружен на две децимале или текст nema ако претицања није било.
#
# Пример 1
# Улаз
# 1.6 20
# 2 12
# 7.4 2.1
# Излаз
# nema

# Пример 2
# Улаз
# 6.3 9
# 15 18
# 19 13
# Излаз
# 47.57

def vremePreticanja(tA, vA, tB, vB):
    return (vB*tB - vA*tA) / (vB - vA)

# ucitavamo podatke:
# vremena u kome su tri vozila krenula sa starta, brzine ta tri vozila
str = input("Unesi brzinu prvog vozila: ").split()
t1 = float(str[0])
v1 = float(str[1])

str = input("Unesi brzinu drugog vozila: ").split()
t2 = float(str[0])
v2 = float(str[1])

str = input("Unesi brzinu treceg vozila: ").split()
t3 = float(str[0])
v3 = float(str[1])

preticanja = []
if v2 > v1:
    preticanja.append(vremePreticanja(t1, v1, t2, v2))

if v3 > v1:
    preticanja.append(vremePreticanja(t1, v1, t3, v3))

if v3 > v2:
    preticanja.append(vremePreticanja(t2, v2, t3, v3))

if preticanja:
    print(format(max(preticanja), '.2f'))
else:
    print("nema")
