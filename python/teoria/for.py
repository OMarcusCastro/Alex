# range(start,stop,step)
'''
range(10): 0->9
range(2,10):2->9
range(2,10,4)-> 2,6

'''
for i in range(10):
    print(i)

#Lista - armario
#index   0 1     2
l =     [1,2,['ola',4]]
print(l[0])
print(l[2][0])
#add no final:
l.append("x")
l.pop()# apaga ulimo elemento
len(l)# tamanho da lista

for i in range(len(l)):
    print(l[i])