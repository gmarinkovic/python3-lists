# За дати низ од n реалних бројева одредити вредност најмањег апсолутног одступања од просека вредности
# унетих бројева (то је најмања апсолутна вредност разлика између елемената и просека низа).
#
# Улаз: У првој линији стандардног улаза уноси се број елемената низа n (1 ≤ n ≤ 100), а затим у следећих n
# линија елементи низа −10000 ≤ ai ≤ 10000.
#
# Излаз: Реалан број на две децимале који представља вредност најмањег апсолутног одступања од средње
# вредности.
#
# Пример
# Улаз
# 6
# 2.8
# 19.3
# -4.2
# 7.5
# -11.1
# 7.17
# Излаз
# 0.78

n = int(input("Uneti broj elemenata niza: "))

a = [float(input("Uneti element niza: ")) for i in range(n)]

prosek = sum(a) / n

# izdvajanje elementa koji daje najmanju razliku u preradjenoj listi
najblizi = min(a, key = lambda x: abs(x - prosek))

min_rastojanje = abs(najblizi - prosek)

print(format(min_rastojanje, '.2f'))
