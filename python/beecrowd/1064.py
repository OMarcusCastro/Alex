# n1 = float(input())
# n2 = float(input())
# n3 = float(input())
# n4 = float(input())
# n5 = float(input())
# n6 = float(input())

# positivo = 0
# media = 0
# if n1>0:
#     positivo += 1 
#     media += n1

# if n2>0:
#     positivo += 1 
#     media += n2

# if n3>0:
#     positivo += 1 
#     media += n3

# if n4>0:
#     positivo += 1 
#     media += n4

# if n5>0:
#     positivo += 1 
#     media += n5

# if n6>0:
#     positivo += 1 
#     media += n6

# valor = media/positivo
# print(f"{positivo:.0f} valores positivos")
# print(valor)

quantia = 0
positivo = 0
valor = 0
valor2 = 0

while quantia<6:
    valor = float(input())

    if valor>0:
        positivo += 1
        valor2 += valor
    quantia+=1

valor_final = valor2/positivo

print(f"{positivo} valores positivos")
print(f"{valor_final:.1f}")