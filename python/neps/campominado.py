n = int(input())
resp = []
l = []
for i in range(n):
    x = int(input())
    l.append(x)

for i in range(n):
    soma =0
    if l[i]==1:
        soma+=1
    if i>0 and l[i-1]==1:
        soma+=1
    if i<n-1 and l[i+1]==1 :
        soma+=1
    resp.append(soma)
    

for ele in resp:
    print(ele)