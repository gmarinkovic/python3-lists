# Aутомобил путује мењајући брзину током путовања. Познато је да се један део пута кретао равномерно
# брзином v1 km/h, затим се један део пута кретао равномерно брзином v2 km/h, и тако даље, све до последњег
# дела пута где се кретао равномерно брзином од vn km/h. Написати програм који одређује просечну брзину
# аутомобила на том путу и то:
# • ако се претпостави да је сваки део пута трајао исто време,
# • ако се претпостави да је на сваком делу пута аутомобил прешао исто растојање.
#
# Улаз: Са стандардног улаза уноси се n (2 ≤ n ≤ 10) позитивних реалних бројева: v1, v2, …, vn (za svako vi
# важи 30 ≤ vi ≤ 120), након чега следи крај улаза.
#
# Излаз: У првој линији стандардног излаза исписати реалан број заокружен на 2 децимале који представља
# просечну брзину под претпоставком да је сваки део пута трајао исто време, а у другом реду реалан број
# заокружен на 2 децимале који представља просечну брзину под претпоставком да је на сваком делу пута
# аутомобил прешао исто растојање.
#
# Пример
# Улаз
# 60
# 40
# Излаз
# 50.00
# 48.00

import sys

def aritmeticka_sredina(a):
    broj = 0                            # broj elemenata niza
    zbir = 0.0                          # zbir elemenata niza
    for x in a:                         # obrađujemo jedan po jedan element
        broj += 1
        zbir += x
    return zbir / broj                  # računamo aritmetičku sredinu

def harmonijska_sredina(a):
    broj = 0                            # broj elemenata niza
    zbir_reciprocnih = 0.0              # zbir reciprocnih vrednosti elemenata niza
    for x in a:                         # obrađujemo jedan po jedan element
        broj += 1
        zbir_reciprocnih += 1.0 / x
    return broj / zbir_reciprocnih      # računamo geometrijsku sredinu


a = []
for x in sys.stdin:
    a.append(float(x))
    
print(format(aritmeticka_sredina(a), '.2f'))
print(format(harmonijska_sredina(a), '.2f'))
