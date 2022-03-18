# Написати програм којим се за n учитаних целих бројева одређује по апсолутној вредности највећа разлика
# два суседна елемента.
#
# Улаз: У првој улазној линији учитава се природан број n (2 ≤ n ≤ 100), a у следећим n целих бројева у
# интервалу [-100,100].
#
# Излаз: Исписује се тражени број који представља највећу апсолутну разлику два суседна броја.
#
# Пример
# Улаз
# 5
# -20
# 30
# 5
# 90
# 70
# Излаз
# 85

# broj elemenata koji se ucitava
n = int(input("Unesi broj elemenata: "))

# ucitavamo sve elemente u niz
a = [int(input()) for i in range(n)]

# kreiramo niz apsolutnih razlika početnog niza
razlike = [abs(a[i]-a[i-1]) for i in range(1, n)]

# određujemo i ispisujemo maksimalnu razliku
print(max(razlike))
