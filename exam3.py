I=1
V=5
X=10
L=50
C=100
D=500
M=1000
IV=4
IX=9
XL=40
XC=90
CD=400
CM=900

romain=input("Saisir nb romain :")

total = 0
i = 0

while i < len(romain):
    if i + 1 < len(romain):
        deux_caractere = romain[i] + romain[i+1]

        match deux_caractere:
            case "IV":
                total += 4
                i += 2
                continue
            case "IX":
                total += 9
                i += 2
                continue
            case "XL":
                total += 40
                i += 2
                continue
            case "XC":
                total += 90
                i += 2
                continue
            case "CD":
                total += 400
                i += 2
                continue
            case "CM":
                total += 900
                i += 2
                continue
    match romain[i]:
        case "I":
            total += 1
        case "V":
            total += 5
        case "X":
            total += 10
        case "L":
            total += 50
        case "C":
            total += 100
        case "D":
            total += 500
        case "M":
            total += 1000
    i += 1

print(total)