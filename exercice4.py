############# Exercice 4 #############

chaine = input("Saisissez une chaîne : ")

lettres_qte = 0
chiffres_qte = 0

for caractere in chaine:
    if caractere.isalpha():
        lettres_qte += 1
    elif caractere.isdigit():
        chiffres_qte += 1

print("Lettres :", lettres_qte)
print("Chiffres :", chiffres_qte)