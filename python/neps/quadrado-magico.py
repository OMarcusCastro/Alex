tamanho = int(input())

matriz = []
magico = 1

for i in range(tamanho):
    linha = list(map(int,input().split()))
    matriz.append(linha)

soma_padrao = sum(matriz[0])

#linha
for linha in matriz:
    if sum(linha)!= soma_padrao:
        magico=0

for i in range(tamanho):
    soma = 0
    for j in range(tamanho):

        soma+=matriz[j][i]
    if soma != soma_padrao:
        magico=0

#diagonal principal
soma =0
soma_secundaria=0
for i in range(tamanho):
    soma+=matriz[i][i]
    soma_secundaria+=matriz[i][tamanho-1-i]
    
if soma != soma_padrao:
    magico =0

if soma_secundaria != soma_padrao:
    magico=0

if magico==0:
    print(-1)
else:
    print(soma_padrao)