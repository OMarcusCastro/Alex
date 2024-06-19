n = int(input())

l = list(map(int,input().split()))
soma = 0
for i in range(n-2):
    if l[i]==1 and l[i+1]==0 and l[i+2]==0:
        soma+=1

print(soma)