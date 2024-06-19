
def calcula_media():

    soma = 0
    i=0
    while i<2 :
        x = float(input())
        if x>=0 and x<=10:
            soma += x
            i += 1
        else:
            print("nota invalida")

    print(f"media = {soma/2:.2f}")


def continuar():
    while True:
        n = int(input("novo calculo (1-sim 2-nao)\n"))
        if n==1 or n==2:
            break
    
    if n==2:
        return False
    else:
        return True

while True:

   calcula_media()
   if not continuar():
    break