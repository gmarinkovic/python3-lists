# Написати програм којим се проверава да ли је дата реч ӣалиндром, што значи да се једнако чита слево на
# десно и сдесна на лево.
#
# Улаз: Прва и једина линија стандардног улаза садржи реч која се састоји само од малих слова енглеске
# абецеде.
#
# Излаз: На стандардном излазу приказати реч da ако реч представља палиндром, тј. ne у супротном.
#
# Пример 1
# Улаз
# madam
# Излаз
# da
# Пример 2
# Улаз
# ranac
# Излаз
# ne

# provera da li je data niska palindrom
def palindrom(rec):
    n = len(rec)
    for i in range(n//2):
        if rec[i] != rec[n-1-i]:
            return False
    return True


rec = input("Unesi rec: ")

if palindrom(rec):
    print("da")
else:
    print("ne")
