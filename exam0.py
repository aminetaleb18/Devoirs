### Exam0 ###

chaine = input("Saisissez une chaine : ")
lastWord = chaine.split()[-1]
res=0
for caractere in lastWord :
    res=res+1

print(res)

