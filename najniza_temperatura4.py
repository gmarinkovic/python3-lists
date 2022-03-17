# Дате су температуре у неколико градова. Написати програм којим се одређује,
# колика је температура у најхладнијем граду.
#
# Улаз: Прва линија стандардног улаза садржи природан број n (3 ≤ n ≤ 50) који представља број градова,
# а у свакој од наредних n линија налази се цео број t (−20 ≤ t ≤ 40) који представља температуру у
# одговарајућем граду.
#
# Излаз: На стандардном излазу, у једној линији, приказати температуру у најхладнијем граду.
#
# Пример
# Улаз
# 5
# 10
# -12
# 22
# -13
# 15
# Излаз
# -13

n = int(input("Unei broj gradova: "))        # broj gradova

# ucitavamo sve temperature
temperature = (int(input("Temperatura u gradu je: ")) for i in range(n))

# određujemo i ispisujemo konačni rezultat
print("Minimalna temperatura medju gradovima je: ",min(temperature))
