a = []

for i in range(20):
    n = int(input())
    a.append(n)

cont = 0
for j in a[::-1]:
    print(f"N[{cont}] = {j}")
    cont +=1