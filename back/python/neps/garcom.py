n = int(input())
soma =0

while n>0:
    n=n-1

    l,c = map(int,input().split())

    if l>c:
        soma = soma +c
print(soma)
