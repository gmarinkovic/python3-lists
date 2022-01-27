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

n = int(input("Unesi broj n celih brojeva: "))
a = [int(input("Unesi cenu uredjaja: ")) for i in range(n)]

max_razlika = 0
element = a[0]

for i in range(1, n):
    if abs(a[i] - element) > max_razlika:
        max_razlika = abs(a[i] - element)
    element = a[i]

print("Najveca absolutna razlika je: ", max_razlika)
