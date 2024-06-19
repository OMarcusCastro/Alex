total = int(input())

soma=0
dia =1

while total>0:
    total -=1

    acesso = int(input())
    soma+=acesso
    if soma <10**6:
        dia+=1

print(dia)