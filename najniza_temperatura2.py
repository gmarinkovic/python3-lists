# Дате су температуре у неколико градова. Написати програм којим се одређује, колика је температура у најхладнијем граду.
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

n = int(input("Unesi broj gradova cije temeprature ispitujemo: ")) 

# ucitavamo temperature u svim gradovima u listu 
temperature = [int(input()) for i in range(n)]

# algoritam odredjivanja minimuma
min_t = temperature[0]
for i in range(1, n):
    if temperature[i] < min_t:
        min_t = temperature[i]
 
print("Najniza temperatura je: ",min_t)
