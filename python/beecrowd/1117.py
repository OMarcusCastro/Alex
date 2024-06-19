i = 0
soma = 0

while i<2 :
    x = float(input())
    if x>=0 and x<=10:
        soma += x
        i += 1
    else:
        print("nota invalida")

print(f"media = {soma/2:.2f}")