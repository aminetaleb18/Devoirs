print("\nHello, Python !\n")

for i in range(5):
    print (i)
    continue

print("\n")

for caractere in "Python":
    print (caractere)

print("\n")

fruits=["pomme","poire","banane"]
for fruit in fruits:
    print(fruit)

print("\n")

personne ={"nom":"Dupont","age":30}
for cle,valeur in personne.items():
    print(cle,valeur)

print("\n")

def test_distinct(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j]:
                return False
    return True

print(test_distinct([1, 5, 7, 9]))          # True
print(test_distinct([2, 4, 5, 5, 7, 9]))    # False
