### exam4 ###

liste =[]
var=""
longueur = int(input("Saisissez la longueur : "))
for i in range(1, longueur + 1):
    val = input(f"Nombre {i} : ")
    var=var+val
nombre=int(var)+1
res=list(str(nombre))
print(res)
