# Написати програм којим се проверава да ли је датa реченица палиндром. Реченица је палиндром ако се
# једнако чита слево на десно и сдесна на лево, при чему се разматрају само слова и не прави се разлика између
# великих и малих слова.
#
# Улаз: Прва и једина линија стандардног улаза садржи реченицу (састављену од слова, празнина и интерпукцијских знакова).
#
# Излаз: На стандардном излазу приказати реч da ако реченица представља палиндром иначе приказати реч ne.
#
# Пример
# Улаз
# Ana voli Milovana!!!
# Излаз
# da

rec = input("Unesi palindromsku recenicu: ").split(" ")

rec2 = "".join(rec)  # spaja reci u jednu veliku rec
rec3 = rec2.lower()  # sve ih prebacuje u mala slova
slova = []
slova[:0] = rec3  # prebacuje sva slova u listu
n = len(slova)
uslov = True
for i in range(0, n // 2):
    if slova[i] != slova[n - 1 - i]:
        uslov = False
        break

print("da" if uslov else "ne")
