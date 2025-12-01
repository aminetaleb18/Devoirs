############# Exercice 1 #############

def test_distinct(seq):
    for x in seq:
        count = 0
        for y in seq:
            if x == y:
                count += 1
            if count > 1:
                return False
    return True

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))

############# Exercice 2 #############

a = int(input("Nombre 1: "))
b = int(input("Nombre 2: "))
c = int(input("Nombre 3: "))

liste = [a, b, c]

liste.sort()

print("Mediane :")
print(liste[1])