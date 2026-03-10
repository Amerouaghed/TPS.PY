

print("\n Ex 1 ")

n = int(input("Entrer un nombre limite : "))
a, b = 0, 1

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

print()





print("\n Ex 2 ")

notes = []

while True:
    note = float(input("Entrer une note (négatif pour arrêter) : "))

    if note < 0:
        break

    notes.append(note)

    print("Nombre de notes :", len(notes))
    print("Max :", max(notes))
    print("Min :", min(notes))
    print("Moyenne :", sum(notes) / len(notes))
 





print("\n Ex 3 ")

# 1 // positif / négatif
def trier(classeur, valeur):
    if valeur < 0:
        classeur['négatifs'].append(valeur)
    else:
        classeur['positifs'].append(valeur)
    return classeur

classeur = {'négatifs': [], 'positifs': []}
trier(classeur, -5)
trier(classeur, 10)
print("Classement :", classeur)


# 2 Difference
def difference(L1, L2):
    diff1 = [x for x in L1 if x not in L2]
    diff2 = [x for x in L2 if x not in L1]
    return (diff1, diff2)

L1 = [1,2,3,4,5,6]
L2 = [5,6,7,8,9,10]
print("Difference :", difference(L1, L2))




print("\n Ex 4 ")

def selection(L1, L2):
    resultat = []
    for i in L2:
        if -len(L1) <= i < len(L1):
            resultat.append(L1[i])
        else:
            resultat.append(None)
    return resultat

L1 = [1,2,3,4,5,6,7,8,9,10]
L2 = [0,2,-1,9,100]
print("Résultat :", selection(L1, L2))





print("\n Ex 5 ")

def max_sum(L):
    return max(L, key=sum)

def max_len(L):
    return max(L, key=len)

def max_first(L):
    return max(L, key=lambda x: x[0])

def max_last(L):
    return max(L, key=lambda x: x[-1])

L = [[1,2,3,0,-1], [13,0], [10,11,12], [0,13]]

print("max_sum :", max_sum(L))
print("max_len :", max_len(L))
print("max_first :", max_first(L))
print("max_last :", max_last(L))





print("\n Ex 6 ")

def list_to_dict(L):
    d = {}
    for i in range(len(L)):
        d[i] = L[i]
    return d


def max_somme(liste_de_listes):
    """
    ترجع القائمة التي لها أكبر مجموع لعناصرها
    """
    if not liste_de_listes:  # إذا كانت القائمة فارغة
        return []
    
    # استخدام max مع key=sum لإيجاد القائمة ذات أكبر مجموع
    return max(liste_de_listes, key=sum)

def max_longueur(liste_de_listes):
    """
    ترجع أطول قائمة
    """
    if not liste_de_listes:
        return []
    
    # استخدام max مع key=len لإيجاد أطول قائمة
    return max(liste_de_listes, key=len)

def max_premier(liste_de_listes):
    """
    ترجع القائمة التي لها أكبر قيمة في أول عنصر
    """
    if not liste_de_listes:
        return []
    
    # تصفية القوائم الفارغة (التي ليس لها أول عنصر)
    listes_non_vides = [lst for lst in liste_de_listes if lst]
    
    if not listes_non_vides:
        return []
    
    # استخدام max مع key=lambda lst: lst[0] لمقارنة العناصر الأولى
    return max(listes_non_vides, key=lambda lst: lst[0])

def max_dernier(liste_de_listes):
    """
    ترجع القائمة التي لها أكبر قيمة في آخر عنصر
    """
    if not liste_de_listes:
        return []
    
    # تصفية القوائم الفارغة (التي ليس لها آخر عنصر)
    listes_non_vides = [lst for lst in liste_de_listes if lst]
    
    if not listes_non_vides:
        return []
    
    # استخدام max مع key=lambda lst: lst[-1] لمقارنة العناصر الأخيرة
    return max(listes_non_vides, key=lambda lst: lst[-1])

# اختبار
L = [[1, 2, 3, 0, -1], [13, 0], [10, 11, 12], [0, 13]]

print("max_somme:", max_somme(L))      # [10, 11, 12]
print("max_longueur:", max_longueur(L))  # [1, 2, 3, 0, -1]
print("max_premier:", max_premier(L))  # [13, 0]
print("max_dernier:", max_dernier(L))  # [0, 13]

L = [(1,2), (3,6), (9,0)]

print("Dictionnaire :", list_to_dict(L))
