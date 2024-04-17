n = int(input())

horas = n // (60*60)
n = n % (60*60)

minutos = n // 60
n = n % 60

print(f"{horas}:{minutos}:{n}")
