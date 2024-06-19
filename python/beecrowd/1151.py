n=int(input())
n1=0
n2 = 1
resp="0 1"
i=0
while i<n-2:
    i+=1
    n3 = n2+n1
    resp=resp + " " + str(n3)  
    n1=n2
    n2=n3

print(resp)