# Милица је направила списак рођендана својих другарица. Поређала је датуме њиховог рођења хронолошки
# (од најдавнијег до најскоријег). Напиши програм који проверава да ли је Милица то добро урадила.
#
# Улаз: Са стандардног улаза учитава се број n (1 ≤ n ≤ 100). У наредних n линија налази се n исправних,
# међусобно различитих датума. Датуми су записани тако што су записани дан, месец и година, раздвојени размацима.
#
# Излаз: У јединој линији стандардног излаза исписати DA ако су датуми исправно (растуће) поређани, тј. NE
# ако нису.
#
# Пример
# Улаз
# 3
# 3 7 2005
# 14 8 2006
# 10 5 2006
# Излаз
# NE

n = int(input("Unesi broj drugarica cije datuem rodjendana proverava Milica: "))
a = [(input("Unesi datum rodjenja Milicine drugarice: ")) for i in range(n)]

ispravnost = True
tekuce = a[0]

for i in range(1, n):
    if int(list(tekuce.split(" "))[2]) > int(list(a[i].split(" "))[2]):
        ispravnost = False
        break
    elif int(list(tekuce.split(" "))[1]) > int(list(a[i].split(" "))[1]):
        ispravnost = False
        break
    elif int(list(tekuce.split(" "))[0]) > int(list(a[i].split(" "))[0]):
        ispravnost = False
        break
    else:
        tekuce = a[i]

print("DA" if ispravnost else "NE")
