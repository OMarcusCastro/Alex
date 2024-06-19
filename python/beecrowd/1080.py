n = 0
pos =1
maior = -1
while n<100 :
    n += 1

    x = int(input())

    if x>maior:
        pos=n
        maior=x

print(maior)
print(pos)

